import streamlit as st

DESIGN_SYSTEM = {
    "colors": {
        "primary": "#4A90E2",       # Azul principal 
        "secondary": "#2D8B72",     # Verde secundario
        "text": "#333333",          # Texto principal
        "subtle": "#E0E0E0",        # Gris suave
        "background": "#FFFFFF",     # Fondo principal
        "background_secondary": "#F7F7F7"  # Fondo secundario
    }
}

def configure_page_style():
    """
    Configura los estilos de la aplicación Streamlit.
    Usa selectores específicos de Streamlit y mantiene la consistencia del diseño.
    """
    st.markdown(f"""
    <style>
    /* 1. Importar fuentes */
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Mono:wght@400&display=swap');

    /* 2. Estilos base */
    .stApp {{
        background-color: {DESIGN_SYSTEM["colors"]["background"]};
    }}

    /* 3. Títulos y texto */
    .stMarkdown h1 {{
        font-family: 'DM Sans', sans-serif !important;
        color: {DESIGN_SYSTEM["colors"]["primary"]} !important;
        font-weight: 700 !important;
        font-size: 2rem !important;
        border-bottom: 2px solid {DESIGN_SYSTEM["colors"]["primary"]};
        padding-bottom: 0.5rem;
        margin-bottom: 1rem;
    }}

    .stMarkdown h2 {{
        font-family: 'DM Sans', sans-serif !important;
        color: {DESIGN_SYSTEM["colors"]["secondary"]} !important;
        font-weight: 500 !important;
        font-size: 1.5rem !important;
        margin-top: 1.5rem !important;
    }}

    /* 4. Campos de entrada y texto */
    /* Inputs */
    div[data-baseweb="input"] input,
    div[data-baseweb="textarea"] textarea {{
        font-family: 'DM Mono', monospace !important;
        font-size: 0.9rem !important;
        background-color: {DESIGN_SYSTEM["colors"]["background_secondary"]} !important;
        border: 1px solid {DESIGN_SYSTEM["colors"]["subtle"]} !important;
        transition: all 0.2s ease !important;
    }}

    div[data-baseweb="input"] input:focus,
    div[data-baseweb="textarea"] textarea:focus {{
        border-color: {DESIGN_SYSTEM["colors"]["primary"]} !important;
        background-color: {DESIGN_SYSTEM["colors"]["background"]} !important;
    }}

    /* Selectores */
    div[data-baseweb="select"] .stSelectbox {{
        font-family: 'DM Mono', monospace !important;
    }}

    div[data-baseweb="select"] select {{
        font-family: 'DM Mono', monospace !important;
        font-size: 0.9rem !important;
        background-color: {DESIGN_SYSTEM["colors"]["background_secondary"]} !important;
        border: 1px solid {DESIGN_SYSTEM["colors"]["subtle"]} !important;
    }}

    /* 5. Botones */
    .stButton > button {{
        font-family: 'DM Mono', monospace !important;
        font-weight: 500 !important;
        background-color: {DESIGN_SYSTEM["colors"]["secondary"]} !important;
        color: white !important;
        padding: 0.5rem 1rem !important;
        border-radius: 0.375rem !important;
        border: none !important;
        transition: opacity 0.2s ease !important;
    }}

    .stButton > button:hover {{
        opacity: 0.9 !important;
    }}

    /* 6. Radio buttons y Checkboxes */
    .stRadio label,
    .stCheckbox label {{
        font-family: 'DM Sans', sans-serif !important;
        color: {DESIGN_SYSTEM["colors"]["text"]} !important;
    }}

    /* 7. Sliders y número inputs */
    .stSlider div[data-baseweb="slider"],
    div[data-baseweb="spinbutton"] {{
        font-family: 'DM Mono', monospace !important;
    }}

    /* 8. Mensajes de error y advertencia */
    .stAlert {{
        font-family: 'DM Sans', sans-serif !important;
        border-radius: 0.375rem !important;
        padding: 0.75rem 1rem !important;
    }}

    /* 9. Elementos de navegación */
    .stSidebar {{
        background-color: {DESIGN_SYSTEM["colors"]["background_secondary"]} !important;
    }}

    /* 10. Ocultar elementos si es necesario */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}

    </style>
    """, unsafe_allow_html=True)
    
