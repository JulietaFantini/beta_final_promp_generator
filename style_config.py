import streamlit as st

DESIGN_SYSTEM = {
    "colors": {
        "primary": "#4A90E2",       # Azul principal
        "secondary": "#2D8B72",     # Verde secundario
        "text": "#333333",
        "subtle": "#E0E0E0",
        "background": "#FFFFFF",
        "background_secondary": "#F7F7F7"
    },
    "spacing": {
        "xs": "0.4rem",
        "sm": "0.8rem",
        "md": "1.2rem",
        "lg": "2rem"
    }
}

def configure_page_style():
    """
    Inyecta CSS que:
      - Usa DM Sans para todo,
      - Toma 'text' y 'background' de DESIGN_SYSTEM,
      - Define botones con 'secondary' y texto blanco,
      - Ocupan todo el ancho y tienen un sutil hover.
    """
    st.markdown(f"""
    <style>
    /* 1) Importar DM Sans */
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap');

    /* 2) Fuente global y fondo */
    html, body, [class^="st"] {{
        font-family: 'DM Sans', -apple-system, BlinkMacSystemFont,
                      "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
        color: {DESIGN_SYSTEM["colors"]["text"]} !important;
        background-color: {DESIGN_SYSTEM["colors"]["background"]} !important;
    }}

    /* 3) Botones al 100% con color "secondary" */
    .stButton > button {{
        width: 100% !important;
        font: 500 1rem 'DM Sans', sans-serif !important;
        padding: 0.8rem 1.2rem !important;
        background-color: {DESIGN_SYSTEM["colors"]["secondary"]} !important;
        color: #FFFFFF !important;
        border-radius: 8px !important;
        border: none !important;
        margin-top: 1.2rem !important;
        transition: opacity 0.2s !important;
        cursor: pointer !important;
    }}
    .stButton > button:hover {{
        opacity: 0.9 !important;
    }}
    </style>
    """, unsafe_allow_html=True)
