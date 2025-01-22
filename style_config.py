import streamlit as st

STYLE_CONFIG = {
    "primary_color": "#4A90E2",  # Color primario (azul)
    "secondary_color": "#50E3C2",  # Color secundario (turquesa)
    "background_color": "#FFFFFF",  # Fondo blanco
    "secondary_background_color": "#F4F4F4",  # Fondo gris claro
    "text_color": "#333333",  # Color de texto (gris oscuro)
    "base_spacing": 12,  # Espaciado base
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
            --color-background: #F4F4F4; /* Fondo gris claro */
            --color-background-secondary: #FFFFFF; /* Fondo secundario blanco */
            --font-primary: 'DM Sans', sans-serif;
            --font-mono: 'DM Mono', monospace;
            --border-radius: 8px;
            --spacing-base: 12px;
        }

        /* Ajustar tamaños de encabezados */
        .stSubheader {
            font-size: 22px !important;
            margin-bottom: var(--spacing-base);
            color: var(--color-primary);
        }

        /* Ajustar texto general */
        .stMarkdown {
            font-size: 16px !important;
            line-height: 1.5;
        }

        /* Ajustar campos de entrada */
        .stTextInput, .stSelectbox {
            font-size: 14px !important;
            padding: 0.5rem !important;
            border-radius: var(--border-radius) !important;
        }

        /* Botones primarios */
        .stButton>button {
            background-color: var(--color-primary) !important;
            color: white !important;
            font-size: 14px;
            padding: 10px 20px;
            border: none;
            border-radius: var(--border-radius);
            cursor: pointer;
        }

        .stButton>button:hover {
            background-color: var(--color-secondary) !important;
        }

        /* Divisores */
        hr {
            border: none;
            height: 1px;
            background-color: var(--color-subtle);
            margin: var(--spacing-base) 0;
        }
        </style>
    """, unsafe_allow_html=True)

# Llamar a la función para aplicar los estilos
configure_page_style()

# Aquí va el resto de tu aplicación Streamlit
st.title("Mi Aplicación de Streamlit")
