import streamlit as st

DESIGN_SYSTEM = {
    "colors": {
        "primary": "#4A90E2",
        "secondary": "#2D8B72",
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
    st.markdown(f"""
    <style>
    /* 1) Importar DM Sans y DM Mono con fallback */
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Mono:wght@400&display=swap');

    /* ========= FUENTE GLOBAL (DM Sans) ========== */
    /* Si quieres que todo lo "general" esté en DM Sans */
    html, body, [class^="st"] {{
        font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, 
                      "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
        color: {DESIGN_SYSTEM["colors"]["text"]};
        background-color: {DESIGN_SYSTEM["colors"]["background"]};
    }}

    /* ========= HEADERS ========== */
    .stMarkdown h1 {{
        font: 700 2rem/1.2 'DM Sans', sans-serif !important;
        color: {DESIGN_SYSTEM["colors"]["primary"]} !important;
        margin-bottom: 1.2rem !important;
        border-bottom: 2px solid {DESIGN_SYSTEM["colors"]["primary"]};
        padding-bottom: 0.4rem;
    }}
    .stMarkdown h2 {{
        font: 500 1.5rem/1.3 'DM Sans', sans-serif !important;
        color: {DESIGN_SYSTEM["colors"]["secondary"]} !important;
        margin-bottom: 0.8rem !important;
    }}

    /* ========= FORMULARIOS en DM Mono ========== */
    [data-testid="stTextInput"] input,
    [data-testid="stTextArea"] textarea {{
        font-family: 'DM Mono', Menlo, 'DejaVu Sans Mono', 'Liberation Mono', monospace !important;
        font-size: 0.9rem !important;
        padding: 0.8rem !important;
        border: 1px solid {DESIGN_SYSTEM["colors"]["subtle"]} !important;
        border-radius: 8px !important;
        background: {DESIGN_SYSTEM["colors"]["background_secondary"]} !important;
        margin-bottom: 0.4rem !important;
        transition: all 0.2s ease !important;
    }}
    .prompt-editor textarea {{
        min-height: 100px !important;
    }}

    /* SELECT: Forzamos DM Mono también en todo su contenido (opciones, label) */
    [data-testid="stSelectbox"] * {{
        font-family: 'DM Mono', Menlo, 'DejaVu Sans Mono', 'Liberation Mono', monospace !important;
    }}
    [data-testid="stSelectbox"] select {{
        font-size: 0.9rem !important;
        padding: 0.8rem !important;
        border: 1px solid {DESIGN_SYSTEM["colors"]["subtle"]} !important;
        border-radius: 8px !important;
        background: {DESIGN_SYSTEM["colors"]["background_secondary"]} !important;
        margin-bottom: 0.4rem !important;
        transition: all 0.2s ease !important;
    }}

    /* FOCO en campos */
    [data-testid="stTextInput"] input:focus,
    [data-testid="stTextArea"] textarea:focus,
    [data-testid="stSelectbox"] select:focus {{
        outline: none !important;
        border-color: {DESIGN_SYSTEM["colors"]["primary"]} !important;
        background: #FFFFFF !important;
    }}

    /* ========= BOTONES en DM Mono ========== */
    /* Quitar width: 100% para que no se extiendan a lo ancho del contenedor */
    .stButton > button,
    .stButton > button * {{
        font-family: 'DM Mono', Menlo, 'DejaVu Sans Mono', 'Liberation Mono', monospace !important;
    }}
    .stButton > button {{
        font-weight: 500;
        font-size: 1rem !important;
        padding: 0.8rem 1.2rem !important;
        background: {DESIGN_SYSTEM["colors"]["secondary"]} !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        margin-top: 1.2rem !important;
        transition: opacity 0.2s !important;
        width: auto !important; /* Ajuste a su contenido en Desktop */
    }}
    .stButton > button:hover {{
        opacity: 0.9 !important;
    }}

    /* ========= HELPER TEXT (en DM Sans, si quieres conservarlo) ========== */
    .stMarkdown small,
    .helper-text {{
        font: 400 0.9rem 'DM Sans', sans-serif !important;
        color: {DESIGN_SYSTEM["colors"]["text"]} !important;
        opacity: 0.8 !important;
    }}

    /* ========= VISTA MÓVIL ========== */
    @media (max-width: 768px) {{
        /* Ajustamos tamaños en móvil para que no se vean gigantes */
        .stMarkdown h1 {{
            font-size: 1.6rem !important;
            margin-bottom: 0.8rem !important;
        }}
        .stMarkdown h2 {{
            font-size: 1.3rem !important;
            margin-bottom: 0.6rem !important;
        }}

        /* Hacemos que el botón ocupe 100% solo en pantallas pequeñas */
        .stButton > button {{
            width: 100% !important;
            font-size: 0.95rem !important;
        }}

        /* Reducir un poco la fuente en inputs/selects en móvil */
        [data-testid="stTextInput"] input,
        [data-testid="stTextArea"] textarea,
        [data-testid="stSelectbox"] select {{
            font-size: 0.85rem !important;
        }}
    }}
    </style>
    """, unsafe_allow_html=True)

def init_page_config():
    st.set_page_config(
        page_title="Generador de Prompts",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
