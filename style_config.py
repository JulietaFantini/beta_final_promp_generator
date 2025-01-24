def configure_page_style():
   st.set_page_config(
       page_title="Generador de Imágenes con IA",
       layout="centered",
       initial_sidebar_state="collapsed"
   )
   
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
