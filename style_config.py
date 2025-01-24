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
    Configura estilos globales para la aplicación de Streamlit usando CSS inline.
    """
    st.markdown(f"""
        <style>
        /* Títulos */
        div.stMarkdown h1 {{
            color: {STYLE_CONFIG["text_color"]} !important;
            border-bottom: 2px solid {STYLE_CONFIG["primary_color"]} !important;
        }}
        
        div.stMarkdown h2 {{
            color: {STYLE_CONFIG["secondary_color"]} !important;
            border-left: 3px solid {STYLE_CONFIG["secondary_color"]} !important;
            padding-left: 8px !important;
        }}
        
        /* Botones */
        .stButton > button {{
            background-color: {STYLE_CONFIG["primary_color"]} !important;
            color: white !important;
            border-radius: 8px !important;
            padding: 0.5rem 1rem !important;
        }}
        </style>
    """, unsafe_allow_html=True)
