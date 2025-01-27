import streamlit as st

DESIGN_SYSTEM = {
    "colors": {
        "primary": "#4A90E2",         # Azul principal
        "secondary": "#2D8B72",       # Verde secundario
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
    Inyecta CSS para:
    - Importar DM Sans y DM Mono (con fallbacks).
    - Ajustar encabezados (h1, h2), formularios, botones y vista móvil.
    - Mejorar accesibilidad con focus en inputs.
    - Mantener la paleta del DESIGN_SYSTEM.
    """
    st.markdown(f"""
        <style>
        /* 1) Importar fuentes desde Google Fonts + fallbacks */
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Mono:wght@400&display=swap');

        /* ========= GLOBAL ========== */
        /* Si Streamlit no aplica la fuente global, forzamos con !important 
           y agregamos fallbacks nativas para DM Sans. */
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

        /* Opcional: si deseas h3 o h4, puedes anadirlos:
        .stMarkdown h3 {{
            font: 500 1.3rem/1.3 'DM Sans', sans-serif !important;
            color: {DESIGN_SYSTEM["colors"]["text"]};
            margin-bottom: 0.6rem !important;
        }}
        */

        /* ========= FORMS ========== */
        [data-testid="stTextInput"] input,
        [data-testid="stTextArea"] textarea,
        [data-testid="stSelectbox"] select {{
            font: 400 0.9rem 'DM Mono', Menlo, "DejaVu Sans Mono", "Liberation Mono", monospace !important;
            padding: 0.8rem !important;
            border: 1px solid {DESIGN_SYSTEM["colors"]["subtle"]} !important;
            border-radius: 8px !important;
            background: {DESIGN_SYSTEM["colors"]["background_secondary"]} !important;
            margin-bottom: 0.4rem !important;
            transition: border-color 0.2s ease, background-color 0.2s ease !important;
        }}

        /* Efecto "focus": mejora accesibilidad, 
           indicando claramente cuál input está activo */
        [data-testid="stTextInput"] input:focus,
        [data-testid="stTextArea"] textarea:focus,
        [data-testid="stSelectbox"] select:focus {{
            outline: none !important;
            border-color: {DESIGN_SYSTEM["colors"]["primary"]} !important;
            background-color: #FFFFFF !important; /* contrasta con el secundario */
        }}

        .prompt-editor textarea {{
            min-height: 100px !important;
        }}

        /* Podrías añadir estilos de "error" o "success" si en algún 
           momento quieres señalizar estados de los campos:
        .has-error input {{
            border-color: #FF5A5F !important; /* Ejemplo: rojo error */
        }}
        .has-success input {{
            border-color: #2D8B72 !important; /* Ej: verde secundario */
        }}
        */

        /* ========= BUTTONS ========== */
        .stButton > button {{
            width: 100% !important;
            font: 500 1rem 'DM Sans', sans-serif !important;
            padding: 0.8rem 1.2rem !important;
            background: {DESIGN_SYSTEM["colors"]["secondary"]} !important;
            color: white !important;
            border-radius: 8px !important;
            border: none !important;
            margin-top: 1.2rem !important;
            transition: opacity 0.2s, background-color 0.2s !important;
        }}

        .stButton > button:hover {{
            opacity: 0.9 !important;
        }}

        /* Si quieres que el boton principal sea "primary" y uno secundario, 
           podrías crear una clase .btn-primary o .btn-secondary y 
           luego asignarlas manualmente, pero en Streamlit no es trivial 
           sin hacks de HTML. */

        /* ========= HELPER TEXT ========== */
        .stMarkdown small,
        .helper-text {{
            font: 400 0.9rem 'DM Sans', sans-serif !important;
            color: {DESIGN_SYSTEM["colors"]["text"]} !important;
            opacity: 0.8 !important;
        }}

        /* ========= RESPONSIVE (MOBILE) ========== */
        @media (max-width: 768px) {{
            .stMarkdown h1 {{ 
                font-size: 1.75rem !important;
                margin-bottom: 0.8rem !important;
            }}
            .stMarkdown h2 {{ 
                font-size: 1.25rem !important;
                margin-bottom: 0.4rem !important;
            }}
            .stButton > button {{ 
                padding: 0.8rem !important;
            }}
            /* Podrías ajustar aún más las fuentes en inputs si lo deseas:
            [data-testid="stTextInput"] input,
            [data-testid="stTextArea"] textarea,
            [data-testid="stSelectbox"] select {{
                font-size: 0.85rem !important;
            }}
            */
        }}
        </style>
    """, unsafe_allow_html=True)

def init_page_config():
    st.set_page_config(
        page_title="Generador de Prompts",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
