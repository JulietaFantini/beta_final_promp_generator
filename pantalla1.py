import streamlit as st
from descripciones import (
    TIPO_IMAGEN_DESCRIPCIONES,
    ESTILO_DESCRIPCIONES,
    ILUMINACION_DESCRIPCIONES,
    PLANO_DESCRIPCIONES,
    COMPOSICION_DESCRIPCIONES,
    PALETA_DESCRIPCIONES,
    TEXTURA_DESCRIPCIONES,
    RESOLUCION_DESCRIPCIONES,
    ASPECTO_DESCRIPCIONES,
    PROPUESTA_PROPOSITO
)

# Pantalla 1: Configuración inicial
def configurar_pantalla1():
    st.title("Creá imágenes con IA")
    st.markdown("Generá las imágenes describiendo lo que querés ver. Empecemos con lo básico.")

    params = st.session_state.get("params", {})

    # Tipo de Imagen
    st.subheader("¿Qué tipo de imagen querés?")
    params["tipo_de_imagen"] = st.selectbox(
        "Tipo de Imagen",
        ["Elegí una opción..."] + list(TIPO_IMAGEN_DESCRIPCIONES.keys())
    )
    if params["tipo_de_imagen"] != "Elegí una opción...":
        st.markdown(TIPO_IMAGEN_DESCRIPCIONES.get(params["tipo_de_imagen"], ""))

    # Idea Inicial
    st.subheader("¿Qué te imaginás?")
    params["idea_inicial"] = st.text_input(
        "Idea Inicial",
        value=params.get("idea_inicial", ""),
        placeholder="Ej.: 'Una ciudad flotante al amanecer'"
    )

    # Propósito y Subpropósito
    st.subheader("Propósito de la Imagen")
    params["proposito_categoria"] = st.selectbox(
        "Seleccioná un propósito:",
        ["Elegí una opción..."] + list(PROPUESTA_PROPOSITO.keys())
    )
    if params["proposito_categoria"] != "Elegí una opción...":
        subpropositos = PROPUESTA_PROPOSITO[params["proposito_categoria"]]
        params["subproposito"] = st.selectbox(
            "Seleccioná un subpropósito:",
            ["Elegí una opción..."] + subpropositos
        )

    # Estilo Artístico
    st.subheader("Estilo")
    params["estilo_artístico"] = st.selectbox(
        "Estilo",
        ["Elegí una opción..."] + list(ESTILO_DESCRIPCIONES.keys())
    )
    if params["estilo_artístico"] != "Elegí una opción...":
        st.markdown(ESTILO_DESCRIPCIONES.get(params["estilo_artístico"], ""))

    # Iluminación
    st.subheader("Iluminación")
    params["iluminación"] = st.selectbox(
        "Seleccioná la iluminación",
        ["Elegí una opción..."] + list(ILUMINACION_DESCRIPCIONES.keys())
    )
    if params["iluminación"] != "Elegí una opción...":
        st.markdown(ILUMINACION_DESCRIPCIONES.get(params["iluminación"], ""))

    # Plano Fotográfico
    st.subheader("Plano Fotográfico")
    params["plano_fotográfico"] = st.selectbox(
        "Seleccioná el plano fotográfico",
        ["Elegí una opción..."] + list(PLANO_DESCRIPCIONES.keys())
    )
    if params["plano_fotográfico"] != "Elegí una opción...":
        st.markdown(PLANO_DESCRIPCIONES.get(params["plano_fotográfico"], ""))

    # Composición
    st.subheader("Composición")
    params["composicion"] = st.selectbox(
        "Seleccioná la composición",
        ["Elegí una opción..."] + list(COMPOSICION_DESCRIPCIONES.keys())
    )
    if params["composicion"] != "Elegí una opción...":
        st.markdown(COMPOSICION_DESCRIPCIONES.get(params["composicion"], ""))

    # Paleta de Colores
    st.subheader("Paleta de Colores")
    params["paleta_de_colores"] = st.selectbox(
        "Seleccioná la paleta de colores",
        ["Elegí una opción..."] + list(PALETA_DESCRIPCIONES.keys())
    )
    if params["paleta_de_colores"] != "Elegí una opción...":
        st.markdown(PALETA_DESCRIPCIONES.get(params["paleta_de_colores"], ""))

    # Textura
    st.subheader("Textura")
    params["textura"] = st.selectbox(
        "Seleccioná la textura",
        ["Elegí una opción..."] + list(TEXTURA_DESCRIPCIONES.keys())
    )
    if params["textura"] != "Elegí una opción...":
        st.markdown(TEXTURA_DESCRIPCIONES.get(params["textura"], ""))

    # Resolución y Formato
    st.subheader("Resolución y Formato")
    col1, col2 = st.columns(2)
    with col1:
        params["resolucion"] = st.selectbox(
            "Seleccioná una resolución",
            ["Elegí una opción..."] + list(RESOLUCION_DESCRIPCIONES.keys())
        )
        if params["resolucion"] != "Elegí una opción...":
            st.markdown(RESOLUCION_DESCRIPCIONES.get(params["resolucion"], ""))
    with col2:
        params["aspecto"] = st.selectbox(
            "Seleccioná una proporción",
            ["Elegí una opción..."] + list(ASPECTO_DESCRIPCIONES.keys())
        )
        if params["aspecto"] != "Elegí una opción...":
            st.markdown(ASPECTO_DESCRIPCIONES.get(params["aspecto"], ""))

    # Guardar parámetros en session_state
    st.session_state["params"] = params

    # Mostrar los parámetros capturados (solo en modo depuración)
    if st.session_state.get("modo_debug", False):
        st.write("Parámetros Capturados (Pantalla 1):", params)

    # Validar y pasar a la siguiente pantalla
    if st.button("Continuar"):
        errores = []
        if params["tipo_de_imagen"] == "Elegí una opción...":
            errores.append("⚠️ Seleccioná un tipo de imagen válido.")
        if not params["idea_inicial"].strip():
            errores.append("⚠️ Completa la idea inicial para continuar.")
        if params["proposito_categoria"] == "Elegí una opción...":
            errores.append("⚠️ Seleccioná un propósito válido.")
        elif params.get("subproposito", "Elegí una opción...") == "Elegí una opción...":
            errores.append("⚠️ Seleccioná un subpropósito válido.")

        if errores:
            for error in errores:
                st.error(error)
        else:
            st.session_state.mostrar_pantalla2 = True
            st.rerun()

if __name__ == "__main__":
    configurar_pantalla1()
