import streamlit as st

STYLE_CONFIG = {
    "primary_color": "#4A90E2",
    "secondary_color": "#2D8B72",
    "text_color": "#333333",
    "color_subtle": "#E0E0E0",
    "background_color": "#FFFFFF",
    "background_secondary": "#F7F7F7"
}

def configure_page_style():
    """
    Configura estilos globales para la aplicación de Streamlit.
    """
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;700&family=DM+Mono:wght@400&display=swap');

        /* Estilo global */
        html, body, [class*="css"] {{
            font-family: 'DM Sans', sans-serif !important;
            color: {STYLE_CONFIG["text_color"]} !important;
            background-color: {STYLE_CONFIG["background_color"]} !important;
        }}

        /* Títulos */
        h1 {{
            font-size: 1.8rem !important;
            color: {STYLE_CONFIG["primary_color"]} !important;
            margin-bottom: 0.4rem !important;
            border-bottom: 2px solid {STYLE_CONFIG["primary_color"]};
            padding-bottom: 0.2rem;
        }}

        h2 {{
            font-size: 1.5rem !important;
            color: {STYLE_CONFIG["secondary_color"]} !important;
            margin-bottom: 0.3rem !important;
        }}

        /* Campos de entrada */
        input, textarea {{
            font-family: 'DM Mono', monospace !important;
            font-size: 0.9rem !important;
            padding: 0.4rem !important;
            border: 1px solid {STYLE_CONFIG["color_subtle"]} !important;
            border-radius: 5px !important;
            margin-bottom: 0.5rem !important;
            background-color: {STYLE_CONFIG["background_secondary"]} !important;
        }}

        input:focus, textarea:focus {{
            border: 1px solid {STYLE_CONFIG["primary_color"]} !important;
            box-shadow: 0 0 4px rgba(74, 144, 226, 0.5);
            outline: none !important;
        }}

        /* Botones */
        .stButton > button {{
            background-color: {STYLE_CONFIG["primary_color"]} !important;
            color: white !important;
            padding: 0.4rem 1rem !important;
            font-size: 1rem !important;
            border-radius: 8px !important;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.2s ease;
        }}

        .stButton > button:hover {{
            background-color: {STYLE_CONFIG["secondary_color"]} !important;
            transform: scale(1.02);
        }}

        /* Área de texto grande en Pantalla 2 */
        textarea.large-textarea {{
            height: 150px !important;
        }}

        /* Sección de herramientas (Pantalla 2) */
        .tool-section {{
            margin-top: 1rem !important;
            padding: 1rem !important;
            border: 1px solid {STYLE_CONFIG["color_subtle"]} !important;
            border-radius: 8px !important;
            background-color: {STYLE_CONFIG["background_secondary"]} !important;
        }}

        /* Enlaces */
        a {{
            color: {STYLE_CONFIG["primary_color"]} !important;
            text-decoration: none !important;
        }}

        a:hover {{
            text-decoration: underline !important;
        }}

        </style>
    """, unsafe_allow_html=True)
