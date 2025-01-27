```python
import streamlit as st

DESIGN_SYSTEM = {
    "colors": {
        "primary": "#4A90E2",
        "secondary": "#2D8B72",
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
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Mono:wght@400&display=swap');

        /* Headers */
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

        /* Form */
        [data-testid="stTextInput"] input,
        [data-testid="stTextArea"] textarea,
        [data-testid="stSelectbox"] select {{
            font: 400 0.9rem 'DM Mono', monospace !important;
            padding: 0.8rem !important;
            border: 1px solid {DESIGN_SYSTEM["colors"]["subtle"]} !important;
            border-radius: 8px !important;
            background: {DESIGN_SYSTEM["colors"]["background_secondary"]} !important;
            margin-bottom: 0.4rem !important;
            transition: all 0.2s ease !important;
        }}

        .prompt-editor textarea {{
            min-height: 100px !important;
        }}

        /* Buttons */
        .stButton > button {{
            width: 100% !important;
            font: 500 1rem 'DM Sans', sans-serif !important;
            padding: 0.8rem 1.2rem !important;
            background: {DESIGN_SYSTEM["colors"]["secondary"]} !important;
            color: white !important;
            border-radius: 8px !important;
            border: none !important;
            margin-top: 1.2rem !important;
            transition: opacity 0.2s !important;
        }}

        .stButton > button:hover {{
            opacity: 0.9 !important;
        }}

        /* Helper Text */
        .stMarkdown small,
        .helper-text {{
            font: 400 0.9rem 'DM Sans', sans-serif !important;
            color: {DESIGN_SYSTEM["colors"]["text"]} !important;
            opacity: 0.8 !important;
        }}

        /* Mobile */
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
        }}
        </style>
    """, unsafe_allow_html=True)

def init_page_config():
    st.set_page_config(
        page_title="Generador de Prompts",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
```
