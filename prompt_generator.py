from typing import Dict

class PromptGenerator:
    """
    Clase para generar prompts optimizados para generación de imágenes con IA.
    
    Esta clase procesa diferentes parámetros de entrada y los transforma en 
    un prompt coherente y descriptivo para plataformas de generación de imágenes.
    """

    # Definiciones necesarias
    TEMPLATE_BASE = {
        "inicio": "Imagina",
        "representar": "que represente",
        "proposito": "creada para",
        "subproposito": "orientada hacia",
        "estilo": "con el estilo visual del",
        "iluminacion": "La imagen debe iluminarse con",
        "plano": "capturada desde un",
        "composicion": "siguiendo una composición de",
        "paleta": "Debe tener una paleta de colores",
        "textura": "y una textura",
        "resolucion": "Finalmente, la resolución debe ser",
        "aspecto": "con una relación de aspecto de"
    }

    TIPOS_MAPPING = {
        "Fotografía": "una fotografía",
        "Ilustración": "una ilustración", 
        "Render 3D": "un render 3D",
        "Pintura digital": "una pintura digital",
        "Arte conceptual": "una pieza de arte conceptual",
        "Collage surrealista": "un collage surrealista",
        "Dibujo técnico": "un dibujo técnico",
        "Fotografía conceptual": "una fotografía conceptual"
    }

    PROPOSITOS_MAPPING = {
        "Comercial y Marketing": {
            "base": "uso comercial y marketing",
            "subpropositos": {
                "Publicidad": "publicidad visual",
                "Branding Visual": "branding visual",
                "Campañas Digitales": "campañas digitales"
            }
        },
        "Arte y Decoración": {
            "base": "arte y decoración",
            "subpropositos": {
                "Arte Conceptual": "arte conceptual",
                "Diseño Ambiental": "diseño ambiental",
                "Arte Personalizado": "arte personalizado"
            }
        },
        "Innovación y Experimentación": {
            "base": "innovación y experimentación",
            "subpropositos": {
                "Proyectos Futuristas": "proyectos futuristas", 
                "Exploraciones Técnicas": "exploraciones técnicas"
            }
        },
        "Técnico y Educativo": {
            "base": "uso técnico y educativo",
            "subpropositos": {
                "Infografías STEM": "infografías STEM",
                "Material Educativo": "material educativo",
                "Diagramas Técnicos": "diagramas técnicos"
            }
        },
        "Entretenimiento Digital": {
            "base": "entretenimiento digital",
            "subpropositos": {
                "Storyboarding": "storyboarding",
                "Diseño de Personajes": "diseño de personajes", 
                "Arte Conceptual": "arte conceptual"
            }
        }
    }

    @staticmethod
    def _normalizar_texto(texto: str) -> str:
        """
        Normaliza el texto, manteniendo términos técnicos en mayúsculas.
        
        Args:
            texto (str): Texto a normalizar
        
        Returns:
            str: Texto normalizado
        """
        if not texto:
            return ""
        if any(x in texto for x in ["STEM", "3D", "HD", "px"]):
            return texto
        return texto.lower().strip()

    @staticmethod
    def _capitalizar_despues_de_punto(texto: str) -> str:
        """
        Capitaliza la primera letra después de cada punto en un texto.

        Args:
            texto (str): Texto a ajustar

        Returns:
            str: Texto ajustado con mayúsculas después de puntos
        """
        oraciones = [oracion.strip().capitalize() for oracion in texto.split('.') if oracion]
        return '. '.join(oraciones) + ('.' if texto.endswith('.') else '')

    def generar_prompt(self, params: Dict) -> str:
        """
        Genera un prompt completo basado en los parámetros proporcionados.
        
        Args:
            params (Dict): Diccionario de parámetros para generar el prompt
        
        Returns:
            str: Prompt generado
        """
        try:
            partes = []

            # 1. Tipo de imagen con idea inicial
            if tipo := self.TIPOS_MAPPING.get(params.get("tipo_de_imagen")):
                prompt_inicial = f"{self.TEMPLATE_BASE['inicio']} {tipo}"
                if idea := params.get('idea_inicial'):
                    prompt_inicial += f" {self.TEMPLATE_BASE['representar']} {self._normalizar_texto(idea)}"
                if not prompt_inicial.endswith('.'):
                    prompt_inicial += '.'
                partes.append(prompt_inicial)
            
            # 2. Propósito y subproposito
            if categoria := self.PROPOSITOS_MAPPING.get(params.get('proposito_categoria')):
                proposito = f"{self.TEMPLATE_BASE['proposito']} {categoria['base']}"
                if subproposito := categoria['subpropositos'].get(params.get('subproposito')):
                    proposito += f", {self.TEMPLATE_BASE['subproposito']} {subproposito}"
                if not proposito.endswith('.'):
                    proposito += '.'
                partes.append(proposito)
            
            # 3. Estilo artístico
            if estilo := params.get('estilo_artístico'):
                estilo_frase = f"{self.TEMPLATE_BASE['estilo']} {self._normalizar_texto(estilo)}"
                if not estilo_frase.endswith('.'):
                    estilo_frase += '.'
                partes.append(estilo_frase)
            
            # 4. Aspectos técnicos
            aspectos_tecnicos = []
            if iluminacion := params.get('iluminación'):
                aspectos_tecnicos.append(f"{self.TEMPLATE_BASE['iluminacion']} {self._normalizar_texto(iluminacion)}")
            if plano := params.get('plano_fotográfico'):
                aspectos_tecnicos.append(f"{self.TEMPLATE_BASE['plano']} {self._normalizar_texto(plano)}")
            if composicion := params.get('composicion'):
                aspectos_tecnicos.append(f"{self.TEMPLATE_BASE['composicion']} {self._normalizar_texto(composicion)}")
            if aspectos_tecnicos:
                partes.append(", ".join(aspectos_tecnicos) + '.')
            
            # 5. Aspectos visuales
            aspectos_visuales = []
            if paleta := params.get('paleta_de_colores'):
                aspectos_visuales.append(f"{self.TEMPLATE_BASE['paleta']} {self._normalizar_texto(paleta)}")
            if textura := params.get('textura'):
                aspectos_visuales.append(f"{self.TEMPLATE_BASE['textura']} {self._normalizar_texto(textura)}")
            if aspectos_visuales:
                partes.append(" y ".join(aspectos_visuales) + '.')
            
            # 6. Resolución y aspecto
            specs = []
            if resolucion := params.get('resolucion'):
                specs.append(f"{self.TEMPLATE_BASE['resolucion']} {resolucion.split(' (')[0]}")
            if aspecto := params.get('aspecto'):
                specs.append(f"{self.TEMPLATE_BASE['aspecto']} {aspecto.split(' (')[0]}")
            if specs:
                partes.append(". ".join(specs) + '.')
            
            # Construir el prompt final como un solo párrafo
            prompt = " ".join(partes)
            prompt = self._capitalizar_despues_de_punto(prompt.strip())
            if not prompt.endswith('.'):
                prompt += '.'
            
            return prompt
            
        except Exception as e:
            print(f"Error al generar prompt: {str(e)}")
            return "Error al generar el prompt. Por favor, verifica los parámetros."
