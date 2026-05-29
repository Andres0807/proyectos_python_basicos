import streamlit as st
import pandas as pd

categorias = ["Comidas", "Transporte", "Salud", "Ocio", "Hogar", "Otros"]


def inicializar_estado():
    if "transacciones" not in st.session_state:
        st.session_state.transacciones = []

def mostrar_titulos():
    st.title("Tracker de Finanzas Personales")
    st.write("Lleva el control de tus gastos e ingresos de manera simple y visual")
    st.caption("Version 1.0")

def mostrar_formulario():
    with st.form("nueva_transaccion"):
        descripcion = st.text_input(
            "Descripcion del gasto o ingreso",
            placeholder="Escribe la descripcion de la operacion"
        )
        monto = st.number_input(
            "Monto",
            step=1.0,
            min_value=0.0,
            format="%0.2f"
        )
        fecha = st.date_input("Fecha", format="DD/MM/YYYY")
        categoria = st.selectbox("Categoria", categorias)
        tipo = st.radio("Tipo", ["Ingreso", "Gasto"], horizontal=True)
        enviado = st.form_submit_button("Enviar")

    if enviado:
        st.session_state.transacciones.append({
            "Descripcion": descripcion,
            "Monto": monto,
            "Fecha": fecha,
            "Categoria": categoria,
            "Tipo": tipo
        })
        st.success("Transaccion agregada correctamente")


def mostrar_resumen():
    if not st.session_state.transacciones:
        st.info("No hay transacciones registradas")
        return

    ingresos = sum(
        transaccion["Monto"]
        for transaccion in st.session_state.transacciones
        if transaccion["Tipo"] == "Ingreso"
    )

    gastos = sum(
        transaccion["Monto"]
        for transaccion in st.session_state.transacciones
        if transaccion["Tipo"] == "Gasto"
    )

    balance = ingresos - gastos

    lista_gastos = [
        transaccion["Monto"]
        for transaccion in st.session_state.transacciones
        if transaccion["Tipo"] == "Gasto"
    ]

    gasto_promedio = (
        sum(lista_gastos) / len(lista_gastos)
        if lista_gastos else 0
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Ingresos", f"${ingresos:.2f}")
    col2.metric("Gastos", f"${gastos:.2f}")
    col3.metric("Balance", f"${balance:.2f}")
    col4.metric("Gasto promedio", f"${gasto_promedio:.2f}")


def mostrar_transacciones():
    st.subheader("Transacciones registraadas")

    if st.session_state.transacciones:
        df = pd.DataFrame(st.session_state.transacciones)
        st.dataframe(df)
    else:
        st.info("No hay transacciones registradas")


def mostrar_analisis():
    gastos = []

    for transaccion in st.session_state.transacciones:
        if transaccion["Tipo"] == "Gasto":
            gastos.append(transaccion)

    if not gastos:
        st.info("No hay transacciones de tipo Gasto")
        return

    gastos_por_categoria = {}

    for gasto in gastos:
        categoria = gasto["Categoria"]
        monto = gasto["Monto"]

        if categoria not in gastos_por_categoria:
            gastos_por_categoria[categoria] = 0

        gastos_por_categoria[categoria] += monto

    datos_categorias = {
        "Categoria": [],
        "Total": []
    }

    for categoria, total in gastos_por_categoria.items():
        datos_categorias["Categoria"].append(categoria)
        datos_categorias["Total"].append(total)

    df_categorias = pd.DataFrame(datos_categorias)

    st.subheader("Gastos por categoria")
    st.bar_chart(df_categorias.set_index("Categoria"))

    gastos_por_fecha = {}

    for gasto in gastos:
        fecha = gasto["Fecha"]
        monto = gasto["Monto"]

        if fecha not in gastos_por_fecha:
            gastos_por_fecha[fecha] = 0

        gastos_por_fecha[fecha] += monto

    datos_fechas = {
        "Fecha": [],
        "Total": []
    }

    for fecha, total in gastos_por_fecha.items():
        datos_fechas["Fecha"].append(fecha)
        datos_fechas["Total"].append(total)

    df_fechas = pd.DataFrame(datos_fechas)

    st.subheader("Gastos por fecha")
    st.line_chart(df_fechas.set_index("Fecha"))


mostrar_titulos()

inicializar_estado()

with st.sidebar:
    mostrar_formulario()

tab_resumen, tab_movimientos, tab_analisis = st.tabs([
    "Resumen",
    "Movimientos",
    "Analisis"
])

with tab_resumen:
    mostrar_resumen()

with tab_movimientos:
    mostrar_transacciones()

with tab_analisis:
    mostrar_analisis()