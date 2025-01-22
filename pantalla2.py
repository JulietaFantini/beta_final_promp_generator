import streamlit as st
import streamlit.components.v1 as components
from googletrans import Translator
from prompt_generator import PromptGenerator

def boton_copiar(text, label="Copiar texto"):
    """
    Muestra un botón (mediante st.components.html) que, al hacer clic,
    copia 'text' al portapapeles del navegador.
    """
    # Escapar caracteres conflictivos para incrustar en HTML + JavaScript
    text_escaped = (
        text
        .replace("\\", "\\\\")
        .replace("\n", "\\n")
        .replace("'", "\\'")
        .replace('"', '\\"')
    )

    # HTML con un botón que llama a navigator.clipboard.writeText(...)
    # Al hacer clic, se muestra una alerta o un aviso de copiado exitoso
    html_code = f"""
    <html>
    <head></head>
    <body>
        <button onclick="navigator.clipboard.writeText('{text_escaped}');
                         alert('¡Texto copiado al portapapeles!');
                "
                style="cursor:pointer;">
            {label}
        </button>
    </body>
    </html>
    """

    # st.components.v1.html 'inyecta' este HTML/JS en un iframe
    components.html(html_code, height=40)


def configurar_pantalla2():
    # Verificar si se proporcionaron datos de la Pantalla 1
    if "params" not in st.session_state or not st.session_state["params"]:
        st.warning("No se han proporcionado datos de la Pantalla 1. Volvé y completá los campos obligatorios.")
        if st.button("Volver a Pantalla 1"):
            st.session_state.mostrar_pantalla2 = False
            st.experimental_rerun()
        return

    # Generar el prompt si no está en session_state
    if "prompt_editado" not in st.session_state:
        generator = PromptGenerator()
        st.session_state["prompt_editado"] = generator.generar_prompt(st.session_state["params"])

    st.subheader("Editá tu prompt directamente en este cuadro")
    st.session_state["prompt_editado"] = st.text_area(
        "Ajustálo según lo que necesites:",
        value=st.session_state["prompt_editado"],
        height=200
    )

    st.divider()

    # Copiar en español
    st.subheader("¿Querés copiarlo en español?")
    boton_copiar(
        text=st.session_state["prompt_editado"], 
        label="📋 Copiar en español"
    )

    # Traducir y copiar al inglés
    st.subheader("¿Preferís usarlo en inglés?")
    st.markdown(
        "Algunas herramientas funcionan mejor con prompts en inglés. "
        "Traducilo y copialo directamente desde acá."
    )

    if st.button("Traducir al inglés"):
        if st.session_state["prompt_editado"].strip():
            try:
                translator = Translator()
                traduccion = translator.translate(
                    st.session_state["prompt_editado"], src='es', dest='en'
                ).text
                st.session_state["traduccion_ingles"] = traduccion

                st.text_area(
                    "Traducción al inglés:", 
                    value=traduccion, 
                    height=200,
                    disabled=True
                )
            except Exception as e:
                st.error(f"Error al traducir el texto: {e}")
        else:
            st.warning("El texto está vacío. No hay nada que traducir.")

    if "traduccion_ingles" in st.session_state:
        boton_copiar(
            text=st.session_state["traduccion_ingles"], 
            label="📋 Copiar traducción al inglés"
        )

    st.divider()

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

    st.divider()

    # Botón para generar un nuevo prompt
    if st.button("Generar un nuevo prompt"):
        st.session_state.mostrar_pantalla2 = False
        st.experimental_rerun()

    # Pie de página
    st.markdown(
        """
        ---
        Este trabajo es parte de un proyecto final de un curso de IA. 
        Para consultas, escribí a **julietafantini@gmail.com**.
        """
    )

# --------------------------------------------------------------------------------
# Ejecución local de prueba
# --------------------------------------------------------------------------------
if __name__ == "__main__":
    configurar_pantalla2()

