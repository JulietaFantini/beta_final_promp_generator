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
            valores_invalidos = {"Elegí una opción...", "", None}

            # 1. Tipo de imagen con idea inicial
            if params.get("tipo_de_imagen") not in valores_invalidos:
                tipo = (params.get('tipo_de_imagen_personalizado', '')
                        if params["tipo_de_imagen"] == "Otro"
                        else self.TIPOS_MAPPING.get(params["tipo_de_imagen"], 
                                                  f"una {params['tipo_de_imagen'].lower()}"))
                
                prompt_inicial = f"{self.TEMPLATE_BASE['inicio']} {tipo}"
                if params.get('idea_inicial') not in valores_invalidos:
                    prompt_inicial += f" {self.TEMPLATE_BASE['representar']} {self._normalizar_texto(params['idea_inicial'])}"
                if not prompt_inicial.endswith('.'):
                    prompt_inicial += '.'
                partes.append(prompt_inicial)
            
            # 2. Propósito y subproposito
            if params.get('proposito_categoria') not in valores_invalidos:
                categoria = params['proposito_categoria']
                mapping = self.PROPOSITOS_MAPPING.get(categoria, {})
                
                proposito = f"{self.TEMPLATE_BASE['proposito']} {mapping.get('base', self._normalizar_texto(categoria))}"
                if params.get('subproposito') not in valores_invalidos:
                    subproposito = params['subproposito'].split(":")[0].strip()  # Extraer solo la parte antes de ':'
                    subproposito_mapped = mapping.get('subpropositos', {}).get(
                        subproposito, 
                        self._normalizar_texto(subproposito)
                    )
                    proposito += f", {self.TEMPLATE_BASE['subproposito']} {subproposito_mapped}"
                if not proposito.endswith('.'):
                    proposito += '.'
                partes.append(proposito)
            
            # 3. Estilo artístico
            if params.get('estilo_artístico') not in valores_invalidos:
                estilo = (params.get('estilo_artístico_personalizado', '')
                         if params['estilo_artístico'] == "Otro"
                         else params['estilo_artístico'])
                estilo_frase = f"{self.TEMPLATE_BASE['estilo']} {self._normalizar_texto(estilo)}"
                if not estilo_frase.endswith('.'):
                    estilo_frase += '.'
                partes.append(estilo_frase)
            
            # 4. Aspectos técnicos
            aspectos_tecnicos = []
            if params.get('iluminación') not in valores_invalidos:
                aspectos_tecnicos.append(
                    f"{self.TEMPLATE_BASE['iluminacion']} {self._normalizar_texto(params['iluminación'])}"
                )
            if params.get('plano_fotográfico') not in valores_invalidos:
                aspectos_tecnicos.append(
                    f"{self.TEMPLATE_BASE['plano']} {self._normalizar_texto(params['plano_fotográfico'])}"
                )
            if params.get('composicion') not in valores_invalidos:
                aspectos_tecnicos.append(
                    f"{self.TEMPLATE_BASE['composicion']} {self._normalizar_texto(params['composicion'])}"
                )
            if aspectos_tecnicos:
                tecnicos = ", ".join(aspectos_tecnicos)
                if not tecnicos.endswith('.'):
                    tecnicos += '.'
                partes.append(tecnicos)
            
            # 5. Aspectos visuales
            aspectos_visuales = []
            if params.get('paleta_de_colores') not in valores_invalidos:
                aspectos_visuales.append(
                    f"{self.TEMPLATE_BASE['paleta']} {self._normalizar_texto(params['paleta_de_colores'])}"
                )
            if params.get('textura') not in valores_invalidos:
                aspectos_visuales.append(
                    f"{self.TEMPLATE_BASE['textura']} {self._normalizar_texto(params['textura'])}"
                )
            if aspectos_visuales:
                visuales = " y ".join(aspectos_visuales)
                if not visuales.endswith('.'):
                    visuales += '.'
                partes.append(visuales)
            
            # 6. Resolución y aspecto
            specs = []
            if params.get('resolucion') not in valores_invalidos:
                resolucion = params['resolucion'].split(" (")[0]
                specs.append(f"{self.TEMPLATE_BASE['resolucion']} {resolucion}")
            if params.get('aspecto') not in valores_invalidos:
                aspecto = params['aspecto'].split(" (")[0]
                specs.append(f"{self.TEMPLATE_BASE['aspecto']} {aspecto}")
            if specs:
                specs_str = ". ".join(specs)
                if not specs_str.endswith('.'):
                    specs_str += '.'
                partes.append(specs_str)
            
            # Construir el prompt final como un solo párrafo
            prompt = " ".join(partes)
            prompt = prompt.strip()
            
            if not prompt.endswith('.'):
                prompt += '.'
            
            return prompt
            
        except Exception as e:
            print(f"Error al generar prompt: {str(e)}")
            return "Error al generar el prompt. Por favor, verifica los parámetros."
