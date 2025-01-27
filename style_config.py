import streamlit as st

def configure_page_style():
    DESIGN_SYSTEM = {
        "colors": {
            "primary": "#4A90E2",
            "secondary": "#2D8B72",
            "text": "#333333",
            "subtle": "#E0E0E0",
            "background": "#FFFFFF",
            "background_secondary": "#F7F7F7"
        }
    }

    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Mono:wght@400&display=swap');

        [data-testid="stAppViewContainer"], 
        [data-testid="stHeader"] {{
            background-color: white !important;
        }}

        .stMarkdown h1 {{
            font-family: 'DM Sans', sans-serif !important;
            font-size: 1.8rem !important;
            color: {DESIGN_SYSTEM["colors"]["primary"]} !important;
            margin-bottom: 0.4rem !important;
            border-bottom: 2px solid {DESIGN_SYSTEM["colors"]["primary"]};
            padding-bottom: 0.2rem;
        }}

        .stMarkdown h2 {{
            font-family: 'DM Sans', sans-serif !important;
            font-size: 1.5rem !important;
            color: {DESIGN_SYSTEM["colors"]["secondary"]} !important;
            margin-bottom: 0.3rem !important;
        }}

        [data-testid="stTextInput"] input,
        [data-testid="stTextArea"] textarea,
        [data-testid="stSelectbox"] select {{
            font-family: 'DM Mono', monospace !important;
            font-size: 0.9rem !important;
            padding: 0.4rem !important;
            border: 1px solid {DESIGN_SYSTEM["colors"]["subtle"]} !important;
            border-radius: 5px !important;
            margin-bottom: 0.5rem !important;
            background-color: {DESIGN_SYSTEM["colors"]["background_secondary"]} !important;
        }}

        .stButton > button {{
            font-family: 'DM Sans', sans-serif !important;
            background-color: {DESIGN_SYSTEM["colors"]["secondary"]} !important;
            color: white !important;
            padding: 0.4rem 1rem !important;
            font-size: 1rem !important;
            border-radius: 8px !important;
            border: none !important;
            transition: opacity 0.2s ease !important;
        }}

        .stButton > button:hover {{
            opacity: 0.9 !important;
        }}

        .prompt-editor {{
            font-family: 'DM Mono', monospace !important;
            min-height: 150px !important;
            padding: 1rem !important;
            border-radius: 5px !important;
            border: 1px solid {DESIGN_SYSTEM["colors"]["subtle"]} !important;
            background-color: {DESIGN_SYSTEM["colors"]["background_secondary"]} !important;
        }}

        .tool-section {{
            padding: 1rem !important;
            border: 1px solid {DESIGN_SYSTEM["colors"]["subtle"]} !important;
            border-radius: 8px !important;
            background-color: {DESIGN_SYSTEM["colors"]["background_secondary"]} !important;
            margin-top: 1rem !important;
        }}
        </style>
    """, unsafe_allow_html=True)
    
