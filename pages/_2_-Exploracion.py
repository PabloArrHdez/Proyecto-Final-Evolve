import streamlit as st
import pandas as pd

st.title ("Explorador de videojuegos desde 1980 hasta 2020")

df = pd.read_csv('Data/video_games_sales_completo.csv')

st.dataframe(df)
st.sidebar.header("Filtrar")