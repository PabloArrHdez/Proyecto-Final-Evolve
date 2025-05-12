import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Estimador")

# CSS para fondo



st.title('🎮 Modelo predictivo categórico de ventas de Videojuegos. 👾')

tab1, tab2 = st.tabs(["Contacto", "Resumen"])

with tab1:
    st.subheader("Contacto")
    st.write("Autor: Pablo Arrastia Hernández")
    st.write("Email: pabloarrhdez@gmail.com")
    st.write("Cuenta GitHub: https://github.com/PabloArrHdez")


with tab2:
    st.subheader("Resumen del proyecto")
    st.markdown(
    """
    A continuación mostramos un modelo predictivo **Random Forest** donde, gracias a las características propias que influyen en la venta de un videojuego, puede predecir, con un 70% de acierto, en qué intervalo categórico de cantidad de unidades vendidas se encuentra el videojuego que se prediga.

    El resultado que muestra el modelo se divide en tres categorías de estimación de ventas:

    - **Normal**: ventas comprendidas entre 1.000 y 240.000 unidades.  
    - **Alta**: ventas comprendidas entre 250.000 y 1.210.000 unidades.  
    - **Muy Alta**: ventas comprendidas entre 1.220.000 y más de 80 millones.
    """
)
