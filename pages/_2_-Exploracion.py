import streamlit as st
import pandas as pd

st.title ("Explorador de videojuegos desde 1980 hasta 2020")

df = pd.read_csv('Data/video_games_sales_completo.csv')

st.dataframe(df)
st.sidebar.header("Filtrar")
estado_consola = st.sidebar.multiselect("Estado Consola", df["Estado_Consola"].unique())
genero = st.sidebar.multiselect("Genero", df["Genre"].unique())
pegi_cateogria = st.sidebar.multiselect("PEGI", df["PEGI_categoria"].unique())
duracion_juego = st.sidebar.multiselect("Duración", df["Duracion_juego_cat"].unique())
precio_min, precio_max = df["Price"].min(), df["Price"].max()
price_range = st.sidebar.slider("Precio Videojuego", precio_min, precio_max, (precio_min, precio_max))