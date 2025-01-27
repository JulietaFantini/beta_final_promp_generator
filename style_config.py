import streamlit as st

# Diccionario con tus colores y espaciados
DESIGN_SYSTEM = {
    "colors": {
        "primary": "#4A90E2",          # Azul principal
        "secondary": "#2D8B72",        # Verde secundario
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
    Inyecta CSS de forma sencilla:
    - DM Sans como fuente global.
    - Botones al 100% de ancho en color "secondary".
    - Puedes agregar más reglas (h1, h2, forms, etc.) si lo deseas.
    """
    st.markdown("""
    <style>
    /* 1) Fuente Global: DM Sans */
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap');

    /* Aplica DM Sans a todo el contenido Streamlit */
    html, body, [class^="st"] {
        font-family: 'DM Sans', -apple-system, BlinkMacSystemFont,
                      "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
        color: #333333 !important; /* Ajusta si deseas, o usa un color del dict */
        background-color: #FFFFFF !important; /* Fondo blanco */
    }

    /* 2) Botones ocupando todo el ancho, con fondo verde "secondary" */
    .stButton > button {
        width: 100% !important;
        font: 500 1rem 'DM Sans', sans-serif !important;
        padding: 0.8rem 1.2rem !important;
        background-color: #2D8B72 !important; /* Verde secondary */
        color: #FFFFFF !important;
        border-radius: 8px !important;
        border: none !important;
        margin-top: 1.2rem !important;
        transition: opacity 0.2s !important;
        cursor: pointer !important;
    }

    .stButton > button:hover {
        opacity: 0.9 !important;
    }
    </style>
    """, unsafe_allow_html=True)
