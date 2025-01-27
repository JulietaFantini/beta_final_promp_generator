import streamlit as st
from styles_config import configure_page_style  # Ajusta el nombre si tu archivo se llama distinto

# 1) Configura la página (título, layout, etc.)
st.set_page_config(
    page_title="Generador de Imágenes con IA",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2) Resto de imports
from pathlib import Path
import os
from pantalla1 import configurar_pantalla1
from pantalla2 import configurar_pantalla2

# 3) Inyecta tu CSS personalizado
configure_page_style()

# 4) Inicializa variables de sesión si no existen
if "mostrar_pantalla2" not in st.session_state:
    st.session_state.mostrar_pantalla2 = False

if "params" not in st.session_state:
    st.session_state.params = {}

# 5) Control de pantallas
try:
    if st.session_state.mostrar_pantalla2:
        configurar_pantalla2()
    else:
        configurar_pantalla1()
except Exception as e:
    st.error(f"Error en la aplicación: {str(e)}")
    print(f"Error detectado: {str(e)}")
