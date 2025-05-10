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


df_filtrado = df[
    (df["Estado_Consola"].isin(estado_consola)) &
    (df["Genre"].isin(genero)) &
    (df["PEGI_categoria"].isin(pegi_cateogria)) &
    (df["Duracion_juego_cat"].isin(duracion_juego)) &
    (df["Price"].between(price_range[0], price_range[1]))
]
st.write (f"Se econtró {df_filtrado.shape[0]} videojuegos")
st.dataframe(df_filtrado)