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

    def render_selectbox(label, key, opciones, descripciones):
        """
        Renderiza un selectbox y muestra una descripción opcional.
        """
        params[key] = st.selectbox(label, ["Elegí una opción..."] + opciones)
        if params[key] != "Elegí una opción...":
            st.markdown(descripciones.get(params[key], ""))

    # Tipo de Imagen
    st.subheader("¿Qué tipo de imagen querés?")
    render_selectbox(
        "Tipo de Imagen",
        "tipo_de_imagen",
        list(TIPO_IMAGEN_DESCRIPCIONES.keys()),
        TIPO_IMAGEN_DESCRIPCIONES
    )

    # Idea Inicial
    st.subheader("¿Qué te imaginás?")
    params["idea_inicial"] = st.text_input(
        "Idea Inicial",
        value=params.get("idea_inicial", ""),
        placeholder="Ej.: 'Una ciudad flotante al amanecer'"
    )

    # Propósito y Subpropósito
    st.subheader("Propósito de la Imagen")
    render_selectbox(
        "Seleccioná un propósito:",
        "proposito_categoria",
        list(PROPUESTA_PROPOSITO.keys()),
        {}
    )
    if params["proposito_categoria"] != "Elegí una opción...":
        subpropositos = PROPUESTA_PROPOSITO[params["proposito_categoria"]]
        render_selectbox(
            "Seleccioná un subpropósito:",
            "subproposito",
            subpropositos,
            {}
        )

    # Estilo Artístico
    st.subheader("Estilo")
    render_selectbox(
        "Estilo",
        "estilo_artístico",
        list(ESTILO_DESCRIPCIONES.keys()),
        ESTILO_DESCRIPCIONES
    )

    # Iluminación
    st.subheader("Iluminación")
    render_selectbox(
        "Seleccioná la iluminación",
        "iluminación",
        list(ILUMINACION_DESCRIPCIONES.keys()),
        ILUMINACION_DESCRIPCIONES
    )

    # Plano Fotográfico
    st.subheader("Plano Fotográfico")
    render_selectbox(
        "Seleccioná el plano fotográfico",
        "plano_fotográfico",
        list(PLANO_DESCRIPCIONES.keys()),
        PLANO_DESCRIPCIONES
    )

    # Composición
    st.subheader("Composición")
    render_selectbox(
        "Seleccioná la composición",
        "composicion",
        list(COMPOSICION_DESCRIPCIONES.keys()),
        COMPOSICION_DESCRIPCIONES
    )

    # Paleta de Colores
    st.subheader("Paleta de Colores")
    render_selectbox(
        "Seleccioná la paleta de colores",
        "paleta_de_colores",
        list(PALETA_DESCRIPCIONES.keys()),
        PALETA_DESCRIPCIONES
    )

    # Textura
    st.subheader("Textura")
    render_selectbox(
        "Seleccioná la textura",
        "textura",
        list(TEXTURA_DESCRIPCIONES.keys()),
        TEXTURA_DESCRIPCIONES
    )

    # Resolución y Formato
    st.subheader("Resolución y Formato")
    col1, col2 = st.columns(2)
    with col1:
        render_selectbox(
            "Seleccioná una resolución",
            "resolucion",
            list(RESOLUCION_DESCRIPCIONES.keys()),
            RESOLUCION_DESCRIPCIONES
        )
    with col2:
        render_selectbox(
            "Seleccioná una proporción",
            "aspecto",
            list(ASPECTO_DESCRIPCIONES.keys()),
            ASPECTO_DESCRIPCIONES
        )

    # Guardar parámetros en session_state
    st.session_state["params"] = params

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

