import streamlit as st
import pandas as pd
import joblib

# Cargar modelo
modelo = joblib.load('Modelo/modelo_videojuegos.pkl')

# Título de la app
st.title('Predicción de Ventas de Videojuegos')
st.markdown('Introduce los detalles del videojuego para estimar su categoría de ventas.')

# Inputs visibles para el usuario
estado_consola = st.selectbox('Antigüedad Consola', ['Obsoleta', ' Consola Secundaria', ' Consola Activa'])
platform = st.selectbox('Plataforma', ['Nintendo Wii', 'Nintendo Entertainment System', 'Game Boy', 'Nintendo DS', 'Xbox 360', 'PlayStation 3', 'PlayStation 2', 'Super Nintendo Entertainment System', 'Game Boy Advance', 'Nintendo 3DS', 'PlayStation 4', 'Nintendo 64', 'PlayStation', 'Xbox', 'PC', 'Atari 2600', 'PlayStation Portable', 'Xbox One', 'GameCube', 'Nintendo Wii U', 'Sega Genesis', 'Dream Cast', 'PlayStation Vita', 'Sega Saturn'])  # Ajusta tus valores reales
genre = st.selectbox('Género', ['Sports', 'Platform', 'Racing', 'Role-Playing', 'Puzzle', 'Misc', 'Shooter', 'Simulation', 'Action', 'Fighting', 'Adventure', 'Strategy'])      # Ajusta también
price = st.number_input('Precio del videojuego (€)', min_value=29.99, max_value=69.99, value=29.99)
modo_juego = st.selectbox('Modo de juego', ['Multijugador', 'Individual'])
pegi = st.selectbox('Clasificación PEGI', ['Infantil', 'Adulto', 'Adolescente'])
duracion_cat = st.selectbox('Duración estimada', ['Corto', 'Medio', 'Largo'])
year = st.number_input('Año del videojuego', min_value=1980, max_value=2020, value=1980)
nota_usuario = st.number_input('Nota del usuario', min_value=0, max_value=10, value=0)
n_votaciones = st.number_input('Nº votaciones', min_value=0, max_value=500, value=5)


