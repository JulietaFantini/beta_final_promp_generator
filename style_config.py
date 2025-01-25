import streamlit as st

STYLE_CONFIG = {
   "primary": "#4A90E2",
   "secondary": "#2D8B72", 
   "text": "#333333",
   "subtle": "#E0E0E0",
   "background": "#FFFFFF",
   "background_secondary": "#F7F7F7"
}

def configure_page_style():
   st.markdown("""
       <style>
       @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Mono:wght@400&display=swap');

       /* Reset Streamlit */
       [data-testid="stAppViewContainer"], 
       [data-testid="stHeader"] {
           background-color: white !important;
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
       }

       /* Button */
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

       /* Links */
       a {
           color: var(--primary) !important;
           text-decoration: none !important;
       }

       a:hover {
           text-decoration: underline !important;
       }

       /* Prompt Area */
       .prompt-area {
           font-family: 'DM Mono', monospace !important;
           background-color: var(--background-secondary) !important;
           padding: 1rem !important;
           border-radius: 5px !important;
           border: 1px solid var(--subtle) !important;
       }

       /* Labels */
       label {
           font-family: 'DM Mono', monospace !important;
           color: var(--text) !important;
           font-size: 0.9rem !important;
       }

       /* Expanders */
       .streamlit-expanderHeader {
           font-family: 'DM Sans', sans-serif !important;
           color: var(--text) !important;
       }

       /* Tool Section */
       .tool-section {
           padding: 1rem !important;
           border: 1px solid var(--subtle) !important;
           border-radius: 8px !important;
           background-color: var(--background-secondary) !important;
           margin-top: 1rem !important;
       }

       :root {
           --primary: """ + STYLE_CONFIG["primary"] + """;
           --secondary: """ + STYLE_CONFIG["secondary"] + """;
           --text: """ + STYLE_CONFIG["text"] + """;
           --subtle: """ + STYLE_CONFIG["subtle"] + """;
           --background: """ + STYLE_CONFIG["background"] + """;
           --background-secondary: """ + STYLE_CONFIG["background_secondary"] + """;
       }
       </style>
   """, unsafe_allow_html=True)

def init_page_config():
   st.set_page_config(
       page_title="Generador de Prompts",
       layout="wide",
       initial_sidebar_state="collapsed"
   )
