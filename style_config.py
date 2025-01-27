import streamlit as st

# Diccionario de diseño ampliado
DESIGN_SYSTEM = {
    "colors": {
        "primary": "#4A90E2",
        "secondary": "#2D8B72",
        "text": "#333333", 
        "subtle": "#E0E0E0",
        "background": "#FFFFFF",
        "background_secondary": "#F7F7F7",
        "error": "#E53935"
    },
    "fonts": {
        "primary": "'DM Sans', sans-serif",
        "secondary": "'DM Mono', monospace"
    },
    "shadows": {
        "soft": "0 2px 8px rgba(0, 0, 0, 0.1)",
        "hard": "0 4px 12px rgba(0, 0, 0, 0.2)"
    }
}

def configure_page_style():
    """
    Inyecta estilos personalizados con mejoras de especificidad y rendimiento
    """
    st.markdown(f"""
    <style>
    /* ===== 1. Fuentes Globales ===== */
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Mono:wght@400&display=swap');
    
    *:not(pre):not(code) {{
        font-family: {DESIGN_SYSTEM["fonts"]["primary"]} !important;
        color: {DESIGN_SYSTEM["colors"]["text"]} !important;
    }}
    
    /* ===== 2. Componentes Principales ===== */
    /* ----- Títulos ----- */
    [data-testid="stMarkdown"] h1 {{
        font: 700 2rem/1.2 {DESIGN_SYSTEM["fonts"]["primary"]} !important;
        color: {DESIGN_SYSTEM["colors"]["primary"]} !important;
        border-bottom: 2px solid {DESIGN_SYSTEM["colors"]["primary"]} !important;
        padding-bottom: 0.4rem !important;
        margin-bottom: 1.5rem !important;
    }}
    
    [data-testid="stMarkdown"] h2 {{
        font: 500 1.5rem/1.3 {DESIGN_SYSTEM["fonts"]["primary"]} !important;
        color: {DESIGN_SYSTEM["colors"]["secondary"]} !important;
        margin-bottom: 1rem !important;
    }}
    
    /* ----- Botones (Primary) ----- */
    [data-testid="baseButton-primary"] {{
        font-family: {DESIGN_SYSTEM["fonts"]["secondary"]} !important;
        background: {DESIGN_SYSTEM["colors"]["secondary"]} !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.8rem 1.5rem !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: {DESIGN_SYSTEM["shadows"]["soft"]} !important;
    }}
    
    [data-testid="baseButton-primary"]:hover {{
        transform: translateY(-1px) !important;
        box-shadow: {DESIGN_SYSTEM["shadows"]["hard"]} !important;
        opacity: 0.95 !important;
    }}
    
    /* ----- Campos de Entrada ----- */
    [data-testid="stTextInput"] > div > div,
    [data-testid="stTextArea"] > div > div,
    [data-testid="stSelectbox"] > div {{
        background: {DESIGN_SYSTEM["colors"]["background_secondary"]} !important;
        border: 1px solid {DESIGN_SYSTEM["colors"]["subtle"]} !important;
        border-radius: 8px !important;
        transition: border-color 0.3s !important;
    }}
    
    [data-testid="stTextInput"] input,
    [data-testid="stTextArea"] textarea {{
        font-family: {DESIGN_SYSTEM["fonts"]["secondary"]} !important;
        padding: 0.8rem !important;
    }}
    
    /* Focus State */
    [data-testid="stTextInput"] > div > div:focus-within,
    [data-testid="stTextArea"] > div > div:focus-within {{
        border-color: {DESIGN_SYSTEM["colors"]["primary"]} !important;
        box-shadow: 0 0 0 2px {DESIGN_SYSTEM["colors"]["primary"]}20 !important;
    }}
    
    /* ===== 3. Layout y Utilidades ===== */
    /* Sidebar */
    section[data-testid="stSidebar"] > div {{
        background: {DESIGN_SYSTEM["colors"]["background_secondary"]} !important;
        border-right: 1px solid {DESIGN_SYSTEM["colors"]["subtle"]} !important;
    }}
    
    /* Espaciado entre componentes */
    .stHorizontalBlock, .stVerticalBlock {{
        gap: 1rem !important;
    }}
    
    /* ===== 4. Mensajes de Error ===== */
    [data-testid="stNotification"] {{
        font-family: {DESIGN_SYSTEM["fonts"]["primary"]} !important;
        background: {DESIGN_SYSTEM["colors"]["error"]}15 !important;
        border-left: 4px solid {DESIGN_SYSTEM["colors"]["error"]} !important;
        color: {DESIGN_SYSTEM["colors"]["error"]} !important;
    }}
    </style>
    """, unsafe_allow_html=True)
    
