import streamlit as st

DESIGN_SYSTEM = {
    "colors": {
        "primary": "#4A90E2",          # azul
        "secondary": "#2D8B72",        # verde
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
    Inyecta un CSS 'agresivo' para sobreescribir 
    cualquier hoja de estilo que fuerce otra fuente.
    
    - DM Sans como fuente global (con !important y selectores potentes).
    - DM Mono para formularios y botones (opcional).
    - Colores 'primary' y 'secondary' para h1, h2 y botones, 
      con !important.
    - Incluimos un test en body para color de fondo (amarillo) 
      que podrás cambiar una vez confirmes que se aplica.
    """
    st.markdown(f"""
    <style>
    /* 1) Importar DM Sans y DM Mono con fallback */
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Mono:wght@400&display=swap');

    /* 2) ESTILO GLOBAL */
    /* Selectores potentes: html, body, .block-container, [class^="st"] */
    /* Forzamos DM Sans y un color de fondo vistoso para confirmar. */
    html, body, .block-container, [class^="st"], #root {{
        font-family: 'DM Sans', -apple-system, BlinkMacSystemFont,
                      "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
        color: {DESIGN_SYSTEM["colors"]["text"]} !important;
        background-color: {DESIGN_SYSTEM["colors"]["background"]} !important;
    }}

    /* (Opcional) Test de color de fondo global 
       para comprobar que SE aplica tu CSS. */
    /* body {{
        background-color: yellow !important;
    }} */

    /* 3) HEADERS */
    .stMarkdown h1, h1 {{
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 700 !important;
        font-size: 2rem !important;
        line-height: 1.2 !important;
        color: {DESIGN_SYSTEM["colors"]["primary"]} !important;
        margin-bottom: 1.2rem !important;
        border-bottom: 2px solid {DESIGN_SYSTEM["colors"]["primary"]} !important;
        padding-bottom: 0.4rem !important;
    }}
    .stMarkdown h2, h2 {{
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 600 !important;
        font-size: 1.5rem !important;
        line-height: 1.3 !important;
        color: {DESIGN_SYSTEM["colors"]["secondary"]} !important;
        margin-bottom: 0.8rem !important;
    }}

    /* 4) FORMULARIOS (en DM Mono) */
    [data-testid="stTextInput"] input,
    [data-testid="stTextArea"] textarea,
    [data-testid="stSelectbox"] select {{
        font-family: 'DM Mono', Menlo, monospace !important;
        font-size: 0.9rem !important;
        padding: 0.8rem !important;
        border: 1px solid {DESIGN_SYSTEM["colors"]["subtle"]} !important;
        border-radius: 8px !important;
        background: {DESIGN_SYSTEM["colors"]["background_secondary"]} !important;
        margin-bottom: 0.4rem !important;
        transition: all 0.2s ease !important;
    }}

    /* FOCO en formularios */
    [data-testid="stTextInput"] input:focus,
    [data-testid="stTextArea"] textarea:focus,
    [data-testid="stSelectbox"] select:focus {{
        outline: none !important;
        border-color: {DESIGN_SYSTEM["colors"]["primary"]} !important;
        background: #FFFFFF !important;
    }}

    /* Forzar DM Mono también para el contenido interno del select */
    [data-testid="stSelectbox"] * {{
        font-family: 'DM Mono', Menlo, monospace !important;
    }}

    /* 5) BOTONES (en DM Mono). Ocupan ancho automático en Desktop */
    .stButton > button,
    .stButton > button * {{
        font-family: 'DM Mono', Menlo, monospace !important;
    }}
    .stButton > button {{
        display: inline-block !important; 
        width: auto !important; /* Ajuste a su contenido */
        font-size: 1rem !important;
        font-weight: 500 !important;
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

    /* 6) TEXTO AUXILIAR (DM Sans) */
    .stMarkdown small,
    .helper-text {{
        font: 400 0.9rem 'DM Sans', sans-serif !important;
        color: {DESIGN_SYSTEM["colors"]["text"]} !important;
        opacity: 0.8 !important;
    }}

    /* 7) VISTA MÓVIL */
    @media (max-width: 768px) {{
        /* Ajuste de titulares */
        .stMarkdown h1, h1 {{
            font-size: 1.7rem !important;
        }}
        .stMarkdown h2, h2 {{
            font-size: 1.3rem !important;
            margin-bottom: 0.6rem !important;
        }}
        /* Botones a 100% de ancho en móvil */
        .stButton > button {{
            width: 100% !important;
        }}
        /* Inputs/Select un poco más chicos */
        [data-testid="stTextInput"] input,
        [data-testid="stTextArea"] textarea,
        [data-testid="stSelectbox"] select {{
            font-size: 0.85rem !important;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True)

def init_page_config():
    st.set_page_config(
        page_title="Mi App con Estilos Reforzados",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
