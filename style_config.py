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

           /* Resetear tema Streamlit */
           [data-testid="stAppViewContainer"], 
           [data-testid="stHeader"],
           section[data-testid="stSidebar"],
           div[class*="css"] {{
               background-color: var(--color-background) !important;
               color: var(--color-text) !important;
           }}

           #MainMenu {{visibility: hidden !important;}}
           footer {{visibility: hidden !important;}}
           header {{visibility: hidden !important;}}

           /* Sistema Tipográfico */
           div.stMarkdown h1 {{
               font-family: var(--font-primary);
               font-weight: var(--fw-bold);
               font-size: 2rem;
               margin-bottom: 1.25rem;
               border-bottom: 2px solid var(--color-primary);
               padding-bottom: 0.5rem;
           }}

           div.stMarkdown h2 {{
               font-family: var(--font-primary);
               font-weight: var(--fw-medium);
               font-size: 1.5rem;
               color: var(--color-secondary);
               margin-bottom: var(--base-spacing);
               border-left: 3px solid var(--color-secondary);
               padding-left: 8px;
           }}

           div.stMarkdown h3 {{
               font-family: var(--font-primary);
               font-weight: var(--fw-medium);
               font-size: 1.25rem;
               margin-bottom: 0.75rem;
           }}

           /* Todo contenido UI en DM Mono */
           div.stMarkdown p,
           .stText,
           div.stTextInput > div,
           div.stTextArea > div,
           div.stSelectbox select,
           div.stAlert {{  
               font-family: var(--font-mono);
               color: var(--color-text);
               line-height: 1.6;
           }}

           /* Campos de Formulario */
           div.stTextInput > div,
           div.stTextArea > div {{
               background-color: var(--color-background-secondary);
               border: 1px solid var(--color-subtle);
               border-radius: var(--border-radius); 
               padding: calc(var(--base-spacing) / 2);
               transition: all 0.2s ease-in-out;
           }}

           div.stTextInput > div:focus-within,
           div.stTextArea > div:focus-within {{
               border-color: var(--color-primary);
               box-shadow: 0 0 0 2px rgba(74, 144, 226, 0.2);
           }}

           /* Botones */
           .stButton > button {{
               font-family: var(--font-mono);
               font-weight: var(--fw-medium);
               background-color: var(--color-primary);
               color: white;
               border: none;
               border-radius: var(--border-radius);
               padding: var(--base-spacing);
               transition: all 0.2s ease-in-out;
           }}

           .stButton > button:hover {{
               background-color: var(--color-primary-hover);
               transform: translateY(-1px);
           }}

           /* Selectores */
           div.stSelectbox select {{
               background-color: var(--color-background-secondary);
               border: 1px solid var(--color-primary);
               border-radius: var(--border-radius);
               padding: calc(var(--base-spacing) / 2);
               transition: all 0.2s ease-in-out;
           }}

           /* Alertas y Estados */
           div.stAlert {{
               background-color: var(--color-background-secondary);
               border-left: 4px solid var(--color-primary);
               border-radius: var(--border-radius);
               padding: var(--base-spacing);
               margin: var(--base-spacing) 0;
               box-shadow: 0 2px 4px rgba(0,0,0,0.05);
           }}

           /* Variantes de Alertas */
           .alert-error {{
               border-left-color: var(--color-error) !important;
           }}

           .alert-warning {{
               border-left-color: var(--color-warning) !important;
           }}

           .alert-success {{
               border-left-color: var(--color-success) !important;
           }}

           /* Estados deshabilitados */
           .stButton > button:disabled {{
               opacity: 0.6;
               cursor: not-allowed;
               pointer-events: none;
           }}

           /* Responsive */
           @media (max-width: 768px) {{
               div.stMarkdown h1 {{
                   font-size: 1.75rem;
               }}
               
               div.stMarkdown h2 {{
                   font-size: 1.25rem;
               }}

               div.stMarkdown h3 {{
                   font-size: 1.1rem;
               }}

               :root {{
                   --base-spacing: 8px;
               }}
               
               .stButton > button {{
                   width: 100%;
               }}
           }}

           /* Prevenir tema oscuro */
           @media (prefers-color-scheme: dark) {{
               [data-testid="stAppViewContainer"], 
               [data-testid="stHeader"],
               section[data-testid="stSidebar"],
               div[class*="css"] {{
                   background-color: var(--color-background) !important;
                   color: var(--color-text) !important;
               }}
           }}

       </style>
   """, unsafe_allow_html=True)
