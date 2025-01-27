class PromptGenerator:
    # ...

    def generar_prompt(self, params: Dict) -> str:
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
            
            # 2. Propósito y subpropósito
            if params.get('proposito_categoria') not in valores_invalidos:
                categoria = params['proposito_categoria']
                mapping = self.PROPOSITOS_MAPPING.get(categoria, {})
                
                proposito = f"{self.TEMPLATE_BASE['proposito']} {mapping.get('base', self._normalizar_texto(categoria))}"
                if params.get('subpropósito') not in valores_invalidos:
                    subproposito = params['subpropósito']
                    subproposito_mapped = mapping.get('subpropositos', {}).get(
                        subproposito, 
                        self._normalizar_texto(subproposito)
                    )
                    proposito += f" {self.TEMPLATE_BASE['subproposito']} {subproposito_mapped}"
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
                tecnicos = ". ".join(aspectos_tecnicos)
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
                visuales = ". ".join(aspectos_visuales)
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
