import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Estimador")
st.title('🎮 Modelo predictivo categórico de ventas de Videojuegos. 👾')

tab1, tab2 = st.tabs(["Resumen", "Contacto"])

with tab1:
    st.subheader("Resumen del proyecto")
    st.write("texto sobre el resumen de tu proyecto")
    
with tab2:
    st.subheader("Contacto")
    st.write("Autor: Pablo Arrastia Hernández")
    st.write("Email: pabloarrhdez@gmail.com")
    st.write("Cuenta GitHub: https://github.com/PabloArrHdez")
