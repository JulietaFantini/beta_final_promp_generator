import streamlit as st

STYLE_CONFIG = {
    "primary_color": "#4A90E2",
    "secondary_color": "#50E3C2",
    "background_color": "#FFFFFF",
    "secondary_background_color": "#F7F7F7",
    "text_color": "#333333",
    "base_spacing": 12,
    "border_radius": 8,
    "color_subtle": "#E0E0E0",
    "font_mono": "DM Mono, monospace",
    "font_primary": "DM Sans, sans-serif",
    "fw_normal": 400,
    "fw_medium": 500,
    "fw_bold": 700,
    "hover_offset": 8,
}

def get_hover_color(base_color):
    color = base_color.lstrip("#")
    rgb = [int(color[i:i+2], 16) for i in (0, 2, 4)]
    dimmed_rgb = [max(0, c - 20) for c in rgb]
    return "#" + "".join([f"{c:02x}" for c in dimmed_rgb])

@st.cache_resource
def configure_page_style():
    st.markdown(f"""
        <style>
        {{{{
            :root {{
                --color-primary: {STYLE_CONFIG["primary_color"]};
                --color-secondary: {STYLE_CONFIG["secondary_color"]};
                --color-subtle: {STYLE_CONFIG["color_subtle"]};  
                --color-primary-hover: {get_hover_color(STYLE_CONFIG["primary_color"])};
                --color-secondary-hover: {get_hover_color(STYLE_CONFIG["secondary_color"])};
                --color-text: {STYLE_CONFIG["text_color"]};
                --color-background: {STYLE_CONFIG["background_color"]};
                --color-background-secondary: {STYLE_CONFIG["secondary_background_color"]};
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
                margin-bottom: calc(var(--base-spacing) * 2);
            }}
            
            div.stMarkdown h2 {{
                font-family: var(--font-primary);
                font-weight: var(--fw-medium);
                margin-bottom: var(--base-spacing);
            }}
            
            div.stMarkdown p,
            .stText {{  
                font-family: var(--font-primary);
                font-weight: var(--fw-normal);
                color: var(--color-text);
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
            div.stButton > button {{
                font-family: var(--font-primary);
                font-weight: var(--fw-medium);
                background-color: var(--color-primary);
                color: white;
                border: none;
                border-radius: var(--border-radius);
                padding: var(--base-spacing);
                transition: all 0.2s ease-in-out;
            }}
            div.stButton > button:hover {{
                background-color: var(--color-primary-hover);
            }}
            
            /* Selectores */
            div.stSelectbox select {{
                font-family: var(--font-mono);
                color: var(--color-text);
                background-color: var(--color-background-secondary);
                border: 1px solid var(--color-subtle);
                border-radius: var(--border-radius);
                padding: calc(var(--base-spacing) / 2);  
            }}
            div.stSelectbox:hover select {{
                border-color: var(--color-primary-hover);
            }}
            
            /* Mensajes de Error */
            div.stAlert {{
                font-family: var(--font-primary);
                border-left: 4px solid var(--color-primary);
                border-radius: var(--border-radius);
                background-color: var(--color-background-secondary);
                padding: var(--base-spacing);
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            div.stAlert p {{
                font-weight: var(--fw-medium); 
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
    
