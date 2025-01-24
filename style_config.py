import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Diseño Conservador", layout="centered")

# Títulos (tipografía nativa de Streamlit)
st.title("Título Principal")  # H1
st.subheader("Subtítulo Secundario")  # H2

# Texto Regular
st.text("Texto regular para contenido informativo.")

# Botones
st.button("Botón Primario")  # Acción principal
st.button("Botón Secundario")  # Acción secundaria

# Campo de Entrada
user_input = st.text_input(
    label="Campo de Entrada", 
    placeholder="Escribe algo aquí...",
    help="Un campo de texto simple para entrada de usuario."
)

# Alerta Informativa
st.info("Este es un mensaje informativo.")

# Layout con columnas
col1, col2 = st.columns(2)
col1.button("Acción en Columna 1")
col2.button("Acción en Columna 2")
