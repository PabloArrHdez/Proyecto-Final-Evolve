import streamlit as st
import pandas as pd
import joblib

# Cargar modelo
modelo = joblib.load('Modelo/modelo_videojuegos.pkl')

# Título de la app
st.title('Predicción de Ventas de Videojuegos')
st.markdown('Introduce los detalles del videojuego para estimar su categoría de ventas.')

# Inputs visibles para el usuario
platform = st.selectbox('Plataforma', ['PlayStation 4', 'Xbox One', 'PC', 'Nintendo Switch'])  # Ajusta tus valores reales
genre = st.selectbox('Género', ['Action', 'Sports', 'Role-Playing', 'Shooter', 'Racing'])      # Ajusta también
price = st.number_input('Precio del videojuego (€)', min_value=0.0, max_value=100.0, value=40.0)
modo_juego = st.selectbox('Modo de juego', ['Multijugador', 'Individual'])
pegi = st.selectbox('Clasificación PEGI', [3, 7, 12, 16, 18])
duracion_cat = st.selectbox('Duración estimada', ['Corta', 'Media', 'Larga'])


