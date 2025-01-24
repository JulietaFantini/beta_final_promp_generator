import streamlit as st

def configure_page_style():
   # Configuración inicial de la página
   st.set_page_config(
       page_title="Generador de Imágenes con IA",
       layout="centered",
       initial_sidebar_state="collapsed"
   )

   # Variables de estilo
   STYLE_CONFIG = {
       "primary_color": "#4A90E2",
       "secondary_color": "#2D8B72",
       "text_color": "#333333",
       "color_subtle": "#E0E0E0",
       "background_color": "#FFFFFF",
       "background_secondary": "#F7F7F7"
   }
   
   # Estilos CSS mínimos que funcionan en Streamlit Cloud
   st.markdown("""
       <style>
       div.stMarkdown h1 {
           color: #333333 !important;
           border-bottom: 2px solid #4A90E2 !important;
       }
       
       div.stMarkdown h2 {
           color: #2D8B72 !important;
           border-left: 3px solid #2D8B72 !important;
           padding-left: 8px !important;
       }
       
       .stButton > button {
           background-color: #4A90E2 !important;
           color: white !important;
       }
       </style>
   """, unsafe_allow_html=True)

if __name__ == "__main__":
   configure_page_style()
   
