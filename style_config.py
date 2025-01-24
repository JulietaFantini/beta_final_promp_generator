import streamlit as st

STYLE_CONFIG = {
   "primary_color": "#E26728",      # Poppy
   "secondary_color": "#F69593",    # Flamingo
   "accent_color": "#AEA434",       # Olive
   "background_color": "#FFFFFF",   
   "subtle_color": "#CBCADC",       # Baby Blue
   "text_primary": "#2D2B3F",       # Dark purple
   "text_secondary": "#4A4860",     # Medium purple
   "base_spacing": 12,
   "border_radius": 8,
   "font_mono": "DM Mono, monospace",
   "font_primary": "DM Sans, system-ui, sans-serif",
   "fw_normal": 400,
   "fw_medium": 500,
   "fw_bold": 700,
}

@st.cache_resource
def configure_page_style():
   st.markdown("""
       <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Mono:wght@300;400;500&display=swap" rel="stylesheet">
   """, unsafe_allow_html=True)
   
   st.markdown(f"""
       <style>
       :root {{
           --color-primary: {STYLE_CONFIG["primary_color"]};
           --color-secondary: {STYLE_CONFIG["secondary_color"]};
           --color-accent: {STYLE_CONFIG["accent_color"]};
           --color-subtle: {STYLE_CONFIG["subtle_color"]};
           --color-text-primary: {STYLE_CONFIG["text_primary"]};
           --color-text-secondary: {STYLE_CONFIG["text_secondary"]};
           --font-primary: {STYLE_CONFIG["font_primary"]};
           --font-mono: {STYLE_CONFIG["font_mono"]};
       }}

       .stApp {{
           font-family: var(--font-primary);
           color: var(--color-text-primary);
       }}

       /* Títulos */
       .stMarkdown h1 {{
           font-family: var(--font-primary);
           font-weight: 700;
           font-size: 2rem;
           line-height: 1.2;
           letter-spacing: -0.02em;
           color: var(--color-text-primary);
           margin-bottom: 1.5rem;
       }}

       .stMarkdown h2 {{
           font-family: var(--font-primary);
           font-weight: 500;
           font-size: 1.6rem;
           letter-spacing: -0.01em;
           color: var(--color-text-primary);
           margin-bottom: 1rem;
       }}

       /* Text Areas */
       .stTextArea textarea,
       .stCodeEditor > div {{
           font-family: var(--font-mono);
           font-size: 0.9375rem;
           line-height: 1.5;
       }}

       /* Botones */
       .stButton > button {{
           font-family: var(--font-primary);
           font-weight: 500;
           background-color: var(--color-primary) !important;
           color: white !important;
           padding: 0.75rem 1.5rem;
           border: none;
           border-radius: 8px;
           transition: opacity 0.3s ease;
       }}

       .stButton > button:hover {{
           opacity: 0.9;
       }}

       /* Selectores */
       .stSelectbox > div > div > select {{
           font-family: var(--font-mono);
           color: var(--color-text-primary);
           background-color: var(--color-background);
           border: 1px solid var(--color-subtle);
           border-radius: 8px;
           padding: 0.75rem;
       }}

       .stSelectbox > div > div > select:focus {{
           border-color: var(--color-secondary);
           box-shadow: 0 0 4px rgba(246, 149, 147, 0.3);
       }}

       /* Inputs */
       .stTextInput > div > div > input,
       .stTextArea > div > div > textarea {{
           font-family: var(--font-mono);
           color: var(--color-text-primary);
           background-color: white;
           border: 1px solid var(--color-subtle);
           border-radius: 8px;
           padding: 0.75rem;
           transition: border-color 0.3s ease, box-shadow 0.3s ease;
       }}

       .stTextInput > div > div > input:focus,
       .stTextArea > div > div > textarea:focus {{
           border-color: var(--color-secondary);
           box-shadow: 0 0 4px rgba(246, 149, 147, 0.3);
       }}

       /* Alertas */
       .stAlert {{
           font-family: var(--font-primary);
           border-left: 4px solid var(--color-primary);
           background-color: white;
           border-radius: 8px;
           padding: 1rem;
           margin: 1rem 0;
           box-shadow: 0 2px 4px rgba(0,0,0,0.1);
       }}

       /* Texto informativo */
       .info-text {{
           font-family: var(--font-mono);
           font-size: 0.875rem;
           color: var(--color-text-secondary);
           margin-bottom: 0.5rem;
       }}

       /* Enlaces */
       a {{
           color: var(--color-primary);
           text-decoration: none;
           transition: opacity 0.3s ease;
       }}

       a:hover {{
           opacity: 0.8;
       }}

       /* Pie de página */
       .footnote {{
           font-family: var(--font-mono);
           font-size: 0.75rem;
           color: var(--color-text-secondary);
           border-top: 1px solid var(--color-subtle);
           padding-top: 1rem;
           margin-top: 2rem;
       }}

       hr {{
           border: none;
           border-top: 1px solid var(--color-subtle);
           margin: 1.5rem 0;
       }}
       </style>
   """, unsafe_allow_html=True)
