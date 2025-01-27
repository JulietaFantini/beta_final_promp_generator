import streamlit as st

# Diccionario de diseño
DESIGN_SYSTEM = {
    "colors": {
        "primary": "#4A90E2",  # Azul principal
        "secondary": "#2D8B72",  # Verde secundario
        "text": "#333333", 
        "subtle": "#E0E0E0",
        "background": "#FFFFFF",
        "background_secondary": "#F7F7F7"
    }
}

def configure_page_style():
    """
    Inyecta estilos personalizados:
      - DM Sans como fuente global.
      - DM Mono para botones y campos.
      - Colores de DESIGN_SYSTEM en texto, fondo, botones, etc.
    """
    st.markdown(f"""
    <style>
    /* ===== 1. Fuentes ===== */
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Mono:wght@400&display=swap');

    /* Fuente global */
    html, body, [class^="st"] {{
        font-family: 'DM Sans', sans-serif !important;
        color: {DESIGN_SYSTEM["colors"]["text"]};
        background-color: {DESIGN_SYSTEM["colors"]["background"]};
    }}

    /* ===== 2. Títulos ===== */
    .stMarkdown h1 {{
        font: 700 2rem/1.2 'DM Sans', sans-serif !important;
        color: {DESIGN_SYSTEM["colors"]["primary"]};
        margin-bottom: 1.2rem !important;
        border-bottom: 2px solid {DESIGN_SYSTEM["colors"]["primary"]};
        padding-bottom: 0.4rem;
    }}
    .stMarkdown h2 {{
        font: 500 1.5rem/1.3 'DM Sans', sans-serif !important;
        color: {DESIGN_SYSTEM["colors"]["secondary"]};
        margin-bottom: 0.8rem !important;
    }}

    /* ===== 3. Botones ===== */
    .stButton > button {{
        font-family: 'DM Mono', monospace !important;  /* Usa DM Mono */
        font-size: 1rem !important;
        font-weight: 500 !important;
        padding: 0.8rem 1.2rem !important;
        background-color: {DESIGN_SYSTEM["colors"]["secondary"]};
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        cursor: pointer !important;
        text-align: center !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        transition: opacity 0.2s ease-in-out !important;
    }}
    .stButton > button:hover {{
        opacity: 0.9 !important;
    }}

    /* ===== 4. Campos de texto y selectores ===== */
    [data-testid="stTextInput"] input,
    [data-testid="stTextArea"] textarea,
    [data-testid="stSelectbox"] select {{
        font-family: 'DM Mono', monospace !important;
        font-size: 0.9rem !important;
        padding: 0.8rem !important;
        border: 1px solid {DESIGN_SYSTEM["colors"]["subtle"]};
        border-radius: 8px !important;
        background: {DESIGN_SYSTEM["colors"]["background_secondary"]};
        margin-bottom: 0.4rem !important;
    }}
    [data-testid="stTextInput"] input:focus,
    [data-testid="stTextArea"] textarea:focus,
    [data-testid="stSelectbox"] select:focus {{
        border-color: {DESIGN_SYSTEM["colors"]["primary"]};
        background: white !important;
        outline: none !important;
    }}

    /* ===== 5. Mensajes de error ===== */
    .stAlert {{
        font-family: 'DM Sans', sans-serif !important;
        color: #E53935 !important;
        font-size: 0.9rem !important;
        margin: 0.5rem 0 !important;
    }}
    </style>
    """, unsafe_allow_html=True)

