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

def configurar_pantalla1():
    st.title("Creá imágenes con IA")
    st.markdown("Generá las imágenes describiendo lo que querés ver. Empecemos con lo básico.")

    params = st.session_state.get("params", {})

    def render_selectbox(label, key, opciones, descripciones):
        params[key] = st.selectbox(" ", ["Elegí una opción..."] + opciones, key=key, label_visibility="collapsed")
        if params[key] != "Elegí una opción...":
            st.markdown(descripciones.get(params[key], ""))

    st.subheader("¿Qué tipo de imagen querés?")
    st.markdown(
        "Fotografía para realismo, ilustración para libertad creativa, render 3D para productos, arte conceptual para ideas abstractas."
    )
    render_selectbox(
        "",
        "tipo_de_imagen",
        list(TIPO_IMAGEN_DESCRIPCIONES.keys()),
        TIPO_IMAGEN_DESCRIPCIONES
    )

    st.subheader("¿Qué te imaginás?")
    st.markdown(
        "Describí los elementos principales y el ambiente deseado."
    )
    params["idea_inicial"] = st.text_input(
        "Idea Inicial",
        value=params.get("idea_inicial", ""),
        placeholder="Ej.: 'Una ciudad flotante al amanecer'"
    )

    st.subheader("Estilo Artístico")
    st.markdown(
        "Digital para efectos modernos, clásico para elegancia tradicional, minimalista para simpleza, surrealista para combinaciones oníricas."
    )
    render_selectbox(
        "",
        "estilo_artístico",
        list(ESTILO_DESCRIPCIONES.keys()),
        ESTILO_DESCRIPCIONES
    )

    st.subheader("Propósito")
    st.markdown(
        "Marketing requiere claridad, arte permite experimentación. El propósito influye en la composición y el enfoque final."
    )
    render_selectbox(
        "",
        "proposito_categoria",
        list(PROPUESTA_PROPOSITO.keys()),
        {}
    )
    if params.get("proposito_categoria") and params["proposito_categoria"] != "Elegí una opción...":
        subpropositos = PROPUESTA_PROPOSITO[params["proposito_categoria"]]
        st.markdown(
            "Seleccioná un subpropósito que se alinee con tu propósito principal."
        )
        render_selectbox(
            "",
            "subproposito",
            subpropositos,
            {}
        )

    st.subheader("Iluminación")
    st.markdown(
        "Natural para realismo, artificial para control creativo. Las sombras dramáticas añaden profundidad."
    )
    render_selectbox(
        "",
        "iluminación",
        list(ILUMINACION_DESCRIPCIONES.keys()),
        ILUMINACION_DESCRIPCIONES
    )

    st.subheader("Plano Fotográfico")
    st.markdown(
        "Primer plano destaca detalles, plano general muestra contexto, cenital ofrece vista superior."
    )
    render_selectbox(
        "",
        "plano_fotográfico",
        list(PLANO_DESCRIPCIONES.keys()),
        PLANO_DESCRIPCIONES
    )

    st.subheader("Composición")
    st.markdown(
        "Simetría para equilibrio, regla de tercios para dinamismo, líneas dominantes guían la mirada."
    )
    render_selectbox(
        "",
        "composicion",
        list(COMPOSICION_DESCRIPCIONES.keys()),
        COMPOSICION_DESCRIPCIONES
    )

    st.subheader("Paleta de Colores")
    st.markdown(
        "Monocromático para elegancia, complementarios para contraste, análogos para armonía."
    )
    render_selectbox(
        "",
        "paleta_de_colores",
        list(PALETA_DESCRIPCIONES.keys()),
        PALETA_DESCRIPCIONES
    )

    st.subheader("Textura")
    st.markdown(
        "Suave para delicadeza, rugosa para carácter, metálica para modernidad."
    )
    render_selectbox(
        "",
        "textura",
        list(TEXTURA_DESCRIPCIONES.keys()),
        TEXTURA_DESCRIPCIONES
    )

    st.subheader("Tamaño y Forma")
    st.markdown(
        "Mayor resolución permite más detalle. Formato cuadrado para balance, panorámico para paisajes, vertical para móvil."
    )
    col1, col2 = st.columns(2)
    with col1:
        render_selectbox(
            "",
            "resolucion",
            list(RESOLUCION_DESCRIPCIONES.keys()),
            RESOLUCION_DESCRIPCIONES
        )
    with col2:
        render_selectbox(
            "",
            "aspecto",
            list(ASPECTO_DESCRIPCIONES.keys()),
            ASPECTO_DESCRIPCIONES
        )

    st.session_state["params"] = params

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
