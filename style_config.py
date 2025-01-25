import streamlit as st

STYLE_CONFIG = {
    "primary_color": "#4A90E2",
    "secondary_color": "#2D8B72",
    "text_color": "#333333",
    "background_color": "#FFFFFF",
    "background_secondary": "#F7F7F7"
}

def configure_page_style():
    """
    Configura estilos globales para la aplicación de Streamlit con un enfoque mínimo y alineado al demo.
    """
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;700&family=DM+Mono:wght@400&display=swap');

        /* Aplicar fuente global */
        html, body, [class*="css"] {{
            font-family: 'DM Sans', sans-serif !important;
            color: {STYLE_CONFIG["text_color"]} !important;
            background-color: {STYLE_CONFIG["background_color"]} !important;
        }}

        /* Encabezados */
        h1 {{
            font-size: 1.8rem !important;
            margin-bottom: 0.4rem !important;
        }}
        h2 {{
            font-size: 1.5rem !important;
            margin-bottom: 0.3rem !important;
        }}

        /* Campos de entrada */
        input, textarea {{
            font-family: 'DM Mono', monospace !important;
            font-size: 0.9rem !important;
            padding: 0.4rem !important;
        }}

        /* Botones */
        .stButton > button {{
            padding: 0.3rem 0.8rem !important;
            font-size: 0.9rem !important;
        }}
        </style>
    """, unsafe_allow_html=True)
