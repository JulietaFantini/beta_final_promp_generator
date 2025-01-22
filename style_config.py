import streamlit as st

STYLE_CONFIG = {
    "primary_color": "#4A90E2",  # Color primario (azul)
    "secondary_color": "#50E3C2",  # Color secundario (turquesa)
    "background_color": "#FFFFFF",  # Fondo blanco
    "secondary_background_color": "#FFFFFF",  # Fondo secundario blanco
    "text_color": "#333333",  # Color de texto (gris oscuro)
    "base_spacing": 10,  # Espaciado base
    "border_radius": 8,  # Radio de bordes
    "color_subtle": "#E0E0E0",  # Borde sutil (gris suave)
    "font_mono": "DM Mono, monospace",  # Fuente Mono
    "font_primary": "DM Sans, sans-serif"  # Fuente principal
}

def configure_page_style():
    """Configura los estilos personalizados para la aplicación Streamlit."""
    st.markdown("""
        <style>
        :root {
            --color-primary: #4A90E2; /* Principal - Azul */
            --color-secondary: #50E3C2; /* Secundario - Turquesa */
            --color-subtle: #E0E0E0; /* Sutil - Para bordes */
            --color-primary-hover: #357ABD; /* Hover para principal */
            --color-secondary-hover: #3DBFA3; /* Hover para secundario */
            --color-text: #333333; /* Texto principal */
            --color-placeholder: #A9A9A9; /* Placeholder */
            --color-background: #FFFFFF; /* Fondo blanco */
            --color-background-secondary: #FFFFFF; /* Fondo secundario blanco */
            --font-primary: 'DM Sans', sans-serif;
            --font-mono: 'DM Mono', monospace;
            --border-radius: 8px;
        }

        /* Ajustar el tamaño del select */
        .stSelectbox > div > div > select {
            font-family: var(--font-mono) !important; /* Forzar fuente DM Mono */
            font-size: 14px !important; /* Tamaño compacto */
            color: var(--color-text) !important; /* Texto gris oscuro */
            background-color: var(--color-background-secondary) !important; /* Fondo blanco */
            border: 1px solid var(--color-subtle) !important; /* Borde sutil */
            border-radius: var(--border-radius) !important; /* Bordes redondeados */
            padding: 0.25rem !important; /* Padding ajustado */
        }

        /* Texto descriptivo como 'Ideal para imágenes realistas' */
        .stMarkdown, .stTextInput + div {
            font-family: var(--font-mono) !important; /* Fuente DM Mono */
            font-size: 14px !important; /* Tamaño consistente */
            color: var(--color-primary) !important; /* Color primario */
            margin-top: 0.5rem !important; /* Espaciado adecuado */
        }

        /* Mensajes de error */
        .stAlert {
            background-color: #FEE2E2 !important; /* Fondo rosa pastel */
            color: #B91C1C !important; /* Texto rojo oscuro */
            font-family: var(--font-primary) !important; /* Fuente principal */
            font-size: 14px !important; /* Tamaño de texto */
            border-left: 4px solid #EF4444 !important; /* Borde rojo */
            padding: 12px !important;
            border-radius: var(--border-radius) !important; /* Bordes redondeados */
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra ligera */
        }

        /* Neutralización selectiva para botones y campos */
        .stButton, .stTextInput, .stTextArea, .stSelectbox {
            box-sizing: border-box !important;
            margin: 0 !important;
            padding: 0 !important;
            border: 1px solid var(--color-subtle) !important;
        }

        /* Ajuste de campos con bordes sutiles */
        .stTextInput > div, .stTextArea > div {
            font-family: var(--font-mono) !important; /* Fuente DM Mono */
            color: var(--color-text) !important;
            background-color: var(--color-background-secondary) !important;
            border: 1px solid var(--color-subtle) !important;
        }

        /* Ajuste de tooltips */
        .stTooltip {
            background-color: var(--color-secondary) !important;
            color: white !important;
            font-size: 14px !important;
            padding: 8px !important;
            border-radius: 5px !important;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        </style>
    """, unsafe_allow_html=True)

# Llamar a la función para aplicar los estilos
configure_page_style()

# Aquí va el resto de tu aplicación Streamlit
st.title("Mi Aplicación de Streamlit")
