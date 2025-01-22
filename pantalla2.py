import streamlit as st
from googletrans import Translator
import pyperclip
from prompt_generator import PromptGenerator

def configurar_pantalla2():
    # Validar que los parámetros de Pantalla 1 existan
    if "params" not in st.session_state or not st.session_state["params"]:
        st.warning("No se han proporcionado datos de la Pantalla 1. Volvé y completá los campos obligatorios.")
        if st.button("Volver a Pantalla 1"):
            st.session_state.mostrar_pantalla2 = False
            st.rerun()
        return

    # Inicializar el prompt si no está en el estado de sesión
    if "prompt_editado" not in st.session_state:
        generator = PromptGenerator()
        st.session_state["prompt_editado"] = generator.generar_prompt(st.session_state["params"])

    st.subheader("Editá tu prompt directamente en este cuadro")
    st.session_state["prompt_editado"] = st.text_area(
        "Ajustálo según lo que necesites:",
        value=st.session_state["prompt_editado"],
        height=200
    )

    st.divider()  # Separador visual nativo

    # Copiar la descripción en español
    def copiar_al_portapapeles(texto):
        if texto.strip():
            try:
                pyperclip.copy(texto)
                st.success("¡Texto copiado al portapapeles! ✅")
            except pyperclip.PyperclipException:
                st.error("Hubo un error al copiar el texto. Esta función puede no estar disponible en este entorno.")
        else:
            st.warning("El texto está vacío. No hay nada que copiar.")

    st.subheader("¿Querés copiarlo en español?")
    if st.button("📋 Copiar en español", use_container_width=True):
        copiar_al_portapapeles(st.session_state["prompt_editado"])

    # Traducir y mostrar opción para copiar al inglés
    st.subheader("¿Preferís usarlo en inglés?")
    st.markdown(
        "Algunas herramientas funcionan mejor con prompts en inglés. "
        "Traducilo y copialo directamente desde acá."
    )

    try:
        translator = Translator()
        if st.button("Traducir al inglés"):
            if st.session_state["prompt_editado"].strip():
                traduccion = translator.translate(
                    st.session_state["prompt_editado"], src='es', dest='en'
                ).text
                st.session_state["traduccion_ingles"] = traduccion
                st.text_area(
                    "Traducción al inglés:", value=traduccion, height=200, disabled=True
                )
            else:
                st.warning("El texto está vacío. No hay nada que traducir.")
    except Exception:
        st.error("Error al traducir el texto. Por favor, intentá nuevamente.")

    if "traduccion_ingles" in st.session_state:
        if st.button("📋 Copiar traducción al inglés"):
            copiar_al_portapapeles(st.session_state["traduccion_ingles"])

    # Herramientas recomendadas
    st.subheader("¿Dónde lo podés usar?")
    st.markdown(
        """
        Estas son las principales herramientas donde podés pegar tu prompt generado para crear imágenes:
        
        - [**DALL-E**](https://openai.com/dall-e): Pegá tu prompt para generar imágenes con precisión **realista**.
        - [**MidJourney**](https://www.midjourney.com): Usalo para crear arte **detallado** y estético.
        - [**Grok**](https://x.com/i/grok?focus=1&mx=2): Aplicá tu prompt para conectarte con tendencias actuales en redes sociales.
        - [**Claude**](https://claude.ai/new): Pegalo para analizar y mejorar resultados complejos.
        - [**Copilot**](https://copilot.microsoft.com/chats/TdFWATF4rK5SLC6Lfo3qN): Una herramienta para potenciar la generación rápida de imágenes.
        """
    )

    st.divider()  # Separador visual nativo

    # Botón para generar un nuevo prompt
    if st.button("Generar un nuevo prompt"):
        st.session_state.mostrar_pantalla2 = False
        st.rerun()

    # Pie de página
    st.markdown(
        """
        ---
        Este trabajo es parte de un proyecto final de un curso de IA. Para consultas, escribí a **julietafantini@gmail.com**.
        """
    )

# --------------------------------------------------------------------------------
# Ejecución local para pruebas
# --------------------------------------------------------------------------------
if __name__ == "__main__":
    configurar_pantalla2()

