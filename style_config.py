Agregamos la importación de streamlit al inicio del archivo:

```python
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
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;700&family=DM+Mono:wght@400&display=swap');
        
        /* Global */
        .stApp, [data-testid="stAppViewContainer"] {{
            background-color: {STYLE_CONFIG["background_color"]} !important;
        }}

        /* Headers - DM Sans */
        h1, .stMarkdown h1 {{
            font-family: 'DM Sans', sans-serif !important;
            font-size: 1.8rem !important;
            color: {STYLE_CONFIG["primary_color"]} !important;
            margin-bottom: 0.4rem !important;
        }}

        h2, .stMarkdown h2 {{
            font-family: 'DM Sans', sans-serif !important;
            font-size: 1.5rem !important;
            color: {STYLE_CONFIG["secondary_color"]} !important;
            margin-bottom: 0.3rem !important;
        }}

        /* Text - DM Sans */
        .stMarkdown p {{
            font-family: 'DM Sans', sans-serif !important;
            color: {STYLE_CONFIG["text_color"]} !important;
        }}

        /* Inputs - DM Mono */
        .stTextInput input, .stTextArea textarea, .stSelectbox select {{
            font-family: 'DM Mono', monospace !important;
            font-size: 0.9rem !important;
            padding: 0.4rem !important;
            border: 1px solid {STYLE_CONFIG["color_subtle"]} !important;
            border-radius: 5px !important;
            margin-bottom: 0.5rem !important;
            background-color: {STYLE_CONFIG["background_secondary"]} !important;
        }}

        .stTextInput input:focus, .stTextArea textarea:focus, .stSelectbox select:focus {{
            border-color: {STYLE_CONFIG["primary_color"]} !important;
            box-shadow: 0 0 4px rgba(74, 144, 226, 0.5) !important;
            outline: none !important;
        }}

        /* Buttons */
        .stButton > button {{
            font-family: 'DM Sans', sans-serif !important;
            background-color: {STYLE_CONFIG["secondary_color"]} !important;
            color: white !important;
            padding: 0.4rem 1rem !important;
            font-size: 1rem !important;
            border-radius: 8px !important;
            border: none !important;
            transition: background-color 0.3s ease !important;
        }}

        .stButton > button:hover {{
            background-color: #1B6F56 !important;
        }}

        /* Links */
        a {{
            color: {STYLE_CONFIG["primary_color"]} !important;
            text-decoration: none !important;
        }}
        
        a:hover {{
            text-decoration: underline !important;
        }}
        </style>
    """, unsafe_allow_html=True)
```
