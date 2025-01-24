import streamlit as st

STYLE_CONFIG = {
    "primary_color": "#4A90E2",  # Azul (Color primario)
    "secondary_color": "#50E3C2",  # Verde (Color secundario)
    "background_color": "#FFFFFF",  # Blanco (Color de fondo)
    "secondary_background_color": "#F7F7F7",  # Gris muy claro (Fondo secundario)
    "text_color": "#333333",  # Gris oscuro (Texto principal)
    "color_subtle": "#E0E0E0",  # Gris claro (Color sutil)
    "base_spacing": 12,
    "border_radius": 8,
    "font_mono": "DM Mono, monospace",
    "font_primary": "DM Sans, sans-serif",
    "fw_normal": 400,
    "fw_medium": 500,
    "fw_bold": 700,
    "hover_offset": 8,
}

@st.cache_resource
def configure_page_style():
    st.markdown(f"""
        <style>
        {{
            :root {{
                --color-primary: {STYLE_CONFIG["primary_color"]};  /* Azul: #4A90E2 */
                --color-secondary: {STYLE_CONFIG["secondary_color"]};  /* Verde: #50E3C2 */
                --color-subtle: {STYLE_CONFIG["color_subtle"]};  /* Gris claro: #E0E0E0 */
                --color-primary-hover: {get_hover_color(STYLE_CONFIG["primary_color"])};  /* Hover sobre el color primario */
                --color-secondary-hover: {get_hover_color(STYLE_CONFIG["secondary_color"])};  /* Hover sobre el color secundario */
                --color-text: {STYLE_CONFIG["text_color"]};  /* Gris oscuro: #333333 */
                --color-background: {STYLE_CONFIG["background_color"]};  /* Blanco: #FFFFFF */
                --color-background-secondary: {STYLE_CONFIG["secondary_background_color"]};  /* Gris muy claro: #F7F7F7 */
                --font-primary: {STYLE_CONFIG["font_primary"]};
                --font-mono: {STYLE_CONFIG["font_mono"]};
                --border-radius: {STYLE_CONFIG["border_radius"]}px;
                --base-spacing: {STYLE_CONFIG["base_spacing"]}px;
                --fw-normal: {STYLE_CONFIG["fw_normal"]};
                --fw-medium: {STYLE_CONFIG["fw_medium"]};
                --fw-bold: {STYLE_CONFIG["fw_bold"]};
            }}
            
            /* Arquitectura Visual */
            div.element-container {{
                margin-bottom: var(--base-spacing);
            }}

            /* Sistema Tipográfico */
            div.stMarkdown h1 {{
                font-family: var(--font-primary);
                font-weight: var(--fw-bold);
                font-size: 3rem;
                margin-bottom: 1.5rem;
            }}
            
            div.stMarkdown h2 {{
                font-family: var(--font-primary);
                font-weight: var(--fw-medium);
                font-size: 2rem;
                color: var(--color-secondary); /* Color secundario aplicado a h2 */
                margin-bottom: var(--base-spacing);
            }}
            
            div.stMarkdown p,
            .stText {{  
                font-family: var(--font-primary);
                font-weight: var(--fw-normal);
                color: var(--color-text); /* Color texto primario */
                line-height: 1.6;
            }}
            
            /* Campos de Formulario */
            div.stTextInput > div,
            div.stTextArea > div {{
                font-family: var(--font-mono);
                color: var(--color-text);
                background-color: var(--color-background-secondary);
                border: 1px solid var(--color-subtle);
                border-radius: var(--border-radius); 
                padding: calc(var(--base-spacing) / 2);
            }}
            
            /* Botones */
            button[kind="primary"] {{
                font-family: var(--font-primary);
                font-weight: var(--fw-medium);
                background-color: var(--color-primary);
                color: white;
                border: none;
                border-radius: var(--border-radius);
                padding: var(--base-spacing);
                transition: all 0.2s ease-in-out;
            }}
            button[kind="primary"]:hover {{
                background-color: var(--color-primary-hover);
            }}
            
            /* Selectores */
            div.stSelectbox select {{
                font-family: var(--font-mono);
                color: var(--color-text);
                background-color: var(--color-background-secondary);
                border: 1px solid var(--color-primary); /* Borde con color primario */
                border-radius: var(--border-radius);
                padding: calc(var(--base-spacing) / 2);
                box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
            }}
            div.stSelectbox:hover select {{
                border-color: var(--color-primary-hover);
                background-color: var(--color-secondary-hover); /* Fondo dinámico con hover */
            }}
            
            /* Mensajes de Error */
            div.stAlert {{
                font-family: var(--font-primary);
                border-left: 4px solid var(--color-primary);
                border-radius: var(--border-radius);
                background-color: var(--color-background-secondary);
                padding: var(--base-spacing);
                box-shadow: 0 2px 4px rgba(0,0,0,0.15);
                margin-top: var(--base-spacing);
                margin-bottom: var(--base-spacing);
            }}
            div.stAlert p {{
                font-weight: var(--fw-medium);
                color: var(--color-primary); /* Texto en color primario */
            }}
            
            /* Jerarquía Informativa */
            .info-text {{
                font-family: var(--font-mono);
                font-size: 0.875rem;
                color: var(--color-text);
                opacity: 0.8;
                margin-bottom: calc(var(--base-spacing) / 2);
            }}
            .highlight-text {{
                color: var(--color-primary);
                font-weight: var(--fw-medium);
            }} 
        }}}}
        </style>
    """, unsafe_allow_html=True)
