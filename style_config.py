import streamlit as st

def get_hover_color(base_color):
    color = base_color.lstrip("#")
    rgb = [int(color[i:i+2], 16) for i in (0, 2, 4)]
    dimmed_rgb = [max(0, c - 20) for c in rgb]
    return "#" + "".join([f"{c:02x}" for c in dimmed_rgb])

STYLE_CONFIG = {
    "primary_color": "#4A90E2",
    "secondary_color": "#2D8B72",
    "background_color": "#FFFFFF", 
    "secondary_background_color": "#F7F7F7",
    "text_color": "#333333",
    "color_subtle": "#E0E0E0",
    "error_color": "#DC2626",
    "warning_color": "#F59E0B",
    "success_color": "#10B981",
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
    # Cargar Google Fonts
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Mono:wght@300;400;500&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)
    
    # Definir variables CSS en :root
    st.markdown(f"""
        <style>
        {{
            :root {{
                --color-primary: {STYLE_CONFIG["primary_color"]} !important;
                --color-secondary: {STYLE_CONFIG["secondary_color"]} !important;
                --color-subtle: {STYLE_CONFIG["color_subtle"]} !important;
                --color-primary-hover: {get_hover_color(STYLE_CONFIG["primary_color"])} !important;
                --color-secondary-hover: {get_hover_color(STYLE_CONFIG["secondary_color"])} !important;
                --color-text: {STYLE_CONFIG["text_color"]} !important;
                --color-background: {STYLE_CONFIG["background_color"]} !important;
                --color-background-secondary: {STYLE_CONFIG["secondary_background_color"]} !important;
                --color-error: {STYLE_CONFIG["error_color"]} !important;
                --color-warning: {STYLE_CONFIG["warning_color"]} !important;
                --color-success: {STYLE_CONFIG["success_color"]} !important;
                --font-primary: {STYLE_CONFIG["font_primary"]};
                --font-mono: {STYLE_CONFIG["font_mono"]};
                --border-radius: {STYLE_CONFIG["border_radius"]}px;
                --base-spacing: {STYLE_CONFIG["base_spacing"]}px;
                --fw-normal: {STYLE_CONFIG["fw_normal"]};
                --fw-medium: {STYLE_CONFIG["fw_medium"]};
                --fw-bold: {STYLE_CONFIG["fw_bold"]};
            }}

            .stApp {{
                background-color: var(--color-background);
                color: var(--color-text);
                font-family: var(--font-primary);
            }}

            div.stMarkdown h1 {{
                font-family: var(--font-primary);
                font-weight: var(--fw-bold);
                font-size: 2rem;
                margin-bottom: 1.25rem;
                border-bottom: 2px solid var(--color-primary);
            }}

            div.stMarkdown h2 {{
                font-family: var(--font-primary);
                font-weight: var(--fw-medium);
                font-size: 1.5rem;
                color: var(--color-secondary);
                margin-bottom: 1rem;
                border-left: 3px solid var(--color-secondary);
                padding-left: 8px;
            }}

            div.stMarkdown h3 {{
                font-family: var(--font-primary);
                font-weight: var(--fw-medium);
                font-size: 1.25rem;
                margin-bottom: 0.75rem;
            }}

            div.stTextInput > div, div.stTextArea > div {{
                font-family: var(--font-mono);
                color: var(--color-text);
                background-color: var(--color-background);
                border: 1px solid var(--color-subtle);
                border-radius: var(--border-radius);
                padding: calc(var(--base-spacing) / 2);
            }}

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

            button[kind="secondary"] {{
                font-family: var(--font-primary);
                font-weight: var(--fw-medium);
                background-color: transparent;
                color: var(--color-primary);
                border: 1px solid var(--color-primary);
                border-radius: var(--border-radius);
                padding: var(--base-spacing);
            }}

            button[kind="secondary"]:hover {{
                background-color: var(--color-background-secondary);
                color: var(--color-primary);
            }}

            div.stAlert {{
                font-family: var(--font-primary);
                border-left: 4px solid var(--color-primary);
                border-radius: var(--border-radius);
                background-color: var(--color-background);
                padding: var(--base-spacing);
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                margin-top: var(--base-spacing);
                margin-bottom: var(--base-spacing);
            }}

            div.stAlert p {{
                font-weight: var(--fw-medium);
                color: var(--color-primary);
            }}

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
        }}
        </style>
    """, unsafe_allow_html=True)
