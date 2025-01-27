Let me validate and check for integration completeness:

```python
# style_config.py
import streamlit as st

DESIGN_SYSTEM = {
    "colors": {
        "primary": "#4A90E2",
        "secondary": "#2D8B72", 
        "text": "#333333",
        "subtle": "#E0E0E0",
        "background": "#FFFFFF",
        "background_secondary": "#F7F7F7",
        "success": "#059669",
        "error": "#DC2626",
        "warning": "#D97706"
    },
    "spacing": {
        "xs": "0.4rem",
        "sm": "0.75rem",
        "md": "1rem",
        "lg": "1.5rem",
        "xl": "2rem"
    }
}

def configure_style():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Mono:wght@400&display=swap');

        /* Reset & Base */
        [data-testid="stAppViewContainer"], 
        [data-testid="stHeader"],
        [data-testid="stToolbar"] {
            background-color: white !important;
        }
        
        /* Typography */
        [data-testid="stMarkdownContainer"] {
            color: var(--text) !important;
        }

        /* Headers */
        .stMarkdown h1 {
            font-family: 'DM Sans', sans-serif !important;
            font-size: 1.8rem !important;
            color: var(--primary) !important;
            margin-bottom: 0.4rem !important;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.2rem;
        }

        .stMarkdown h2 {
            font-family: 'DM Sans', sans-serif !important;
            font-size: 1.5rem !important;
            color: var(--secondary) !important;
            margin-bottom: 0.3rem !important;
        }

        /* Form Elements */
        [data-testid="stTextInput"] input,
        [data-testid="stTextArea"] textarea,
        [data-testid="stSelectbox"] select {
            font-family: 'DM Mono', monospace !important;
            font-size: 0.9rem !important;
            padding: 0.4rem !important;
            border: 1px solid var(--subtle) !important;
            border-radius: 5px !important;
            margin-bottom: 0.5rem !important;
            background-color: var(--background-secondary) !important;
            transition: all 0.2s ease !important;
        }

        /* Focus States */
        [data-testid="stTextInput"] input:focus,
        [data-testid="stTextArea"] textarea:focus,
        [data-testid="stSelectbox"] select:focus {
            border-color: var(--primary) !important;
            box-shadow: 0 0 0 2px rgba(74,144,226,0.2) !important;
        }

        /* Buttons */
        .stButton > button {
            font-family: 'DM Sans', sans-serif !important;
            background-color: var(--secondary) !important;
            color: white !important;
            padding: 0.4rem 1rem !important;
            font-size: 1rem !important;
            border-radius: 8px !important;
            border: none !important;
            transition: opacity 0.2s ease !important;
        }

        .stButton > button:hover {
            opacity: 0.9 !important;
        }

        /* Prompt Editor */
        .prompt-editor {
            font-family: 'DM Mono', monospace !important;
            background-color: var(--background-secondary) !important;
            padding: 1rem !important;
            border-radius: 5px !important;
            border: 1px solid var(--subtle) !important;
            min-height: 150px !important;
        }

        /* Labels */
        label {
            font-family: 'DM Mono', monospace !important;
            color: var(--text) !important;
            font-size: 0.9rem !important;
        }

        /* Tool Section */
        .tool-section {
            padding: 1rem !important;
            border: 1px solid var(--subtle) !important;
            border-radius: 8px !important;
            background-color: var(--background-secondary) !important;
            margin-top: 1rem !important;
            transition: transform 0.2s ease !important;
        }

        .tool-section:hover {
            transform: translateY(-2px) !important;
            border-color: var(--primary) !important;
        }

        /* Messages */
        .message {
            padding: 0.75rem !important;
            border-radius: 4px !important;
            margin: 1rem 0 !important;
            font-family: 'DM Sans', sans-serif !important;
        }

        .message.success { background: rgba(5,150,105,0.1) !important; }
        .message.error { background: rgba(220,38,38,0.1) !important; }
        .message.info { background: rgba(74,144,226,0.1) !important; }

        /* Responsive */
        @media (max-width: 768px) {
            .stMarkdown h1 { font-size: 1.5rem !important; }
            .stMarkdown h2 { font-size: 1.25rem !important; }
            .prompt-editor { min-height: 120px !important; }
        }

        :root {
            --primary: """ + DESIGN_SYSTEM["colors"]["primary"] + """;
            --secondary: """ + DESIGN_SYSTEM["colors"]["secondary"] + """;
            --text: """ + DESIGN_SYSTEM["colors"]["text"] + """;
            --subtle: """ + DESIGN_SYSTEM["colors"]["subtle"] + """;
            --background: """ + DESIGN_SYSTEM["colors"]["background"] + """;
            --background-secondary: """ + DESIGN_SYSTEM["colors"]["background_secondary"] + """;
        }
        </style>
    """, unsafe_allow_html=True)

def init_page_config():
    st.set_page_config(
        page_title="Generador de Prompts",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
```

Config.toml:
```toml
[theme]
primaryColor = "#4A90E2"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F7F7F7"
textColor = "#333333"
font = "DM Sans"

[server]
port = 8501
enableCORS = false
fileWatcherType = "poll"
headless = true
```
