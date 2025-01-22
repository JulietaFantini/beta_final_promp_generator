import streamlit as st
from googletrans import Translator
from prompt_generator import PromptGenerator

def boton_copiar(text, label="Copiar texto"):
    """
    Muestra un botón que, al hacer clic, copia 'text'
    al portapapeles del navegador usando JavaScript.
    """
    # Escapar comillas simples y dobles para no romper el HTML
    text = text.replace("'", "\\'").replace('"', '\\"')
    import uuid
    btn_id = str(uuid.uuid4()).replace('-', '')

    # HTML + JS: al hacer clic, se invoca la API del navegador para copiar
    html_code = f"""
        <button id="copy-btn-{btn_id}"
                onclick="navigator.clipboard.writeText('{text}');
                         var tooltip = document.getElementById('tooltip-{btn_id}');
                         tooltip.innerHTML = '¡Copiado!';
                "
                style="cursor:pointer;"
        >
            {label}
        </button>
        <span id="tooltip-{btn_id}" style="margin-left:8px;color:green"></span>
    """
    st.markdown(html_code, unsafe_allow_html=True)


def configurar_pantalla2():
    # Validar que los parámetros de Pantalla 1 existan
    if "params" not in st.session_state or not st.session_state["params"]:
        st.warning("No se han proporcionado datos de la Pantalla 1. Volvé y completá los campos obligatorios.")
        if st.button("Volver a Pantalla 1"):
            st.session_state.mostrar_pantalla2 = False
            st.experimental_rerun()
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

    # Sección para copiar en español
    st.subheader("¿Querés copiarlo en español?")
    boton_copiar(st.session_state["prompt_editado"], label="📋 Copiar en español")

    # Sección para traducir y copiar al inglés
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
                st.text_area("Traducción al inglés:", value=traduccion, height=200, disabled=True)
            except Exception as e:
                st.error(f"Error al traducir el texto: {e}")
        else:
            st.warning("El texto está vacío. No hay nada que traducir.")

    if "traduccion_ingles" in st.session_state:
        boton_copiar(st.session_state["traduccion_ingles"], label="📋 Copiar traducción al inglés")

    st.divider()  # Separador visual nativo

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
        st.experimental_rerun()

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
