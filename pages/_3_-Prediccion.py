import streamlit as st
import pandas as pd
import joblib

# Cargar modelo
modelo = joblib.load('Modelo/modelo_videojuegos.pkl')

# Título de la app
st.title('Predicción de Ventas de Videojuegos')
st.markdown('Introduce los detalles del videojuego para estimar su categoría de ventas.')

# Inputs visibles para el usuario
plataformas_activas = [
    'PlayStation 4', 'Xbox One', 'PC'
]
plataforma_secundaria = ['Nintendo 3DS', 'PlayStation Vita']
plataforma_obsoleta = ['Nintendo Wii', 'Nintendo Entertainment System', 'Game Boy', 'Nintendo DS', 'Xbox 360', 'PlayStation 3', 'PlayStation 2', 'Super Nintendo Entertainment System', 'Game Boy Advance', 'Nintendo 64', 'PlayStation', 'Xbox', 'Atari 2600', 'PlayStation Portable', 'GameCube', 'Nintendo Wii U', 'Sega Genesis', 'Dream Cast', 'Sega Saturn']
estado_consola = st.selectbox('Antigüedad Consola', ['Obsoleta', 'Consola Secundaria', 'Consola Activa'])
if estado_consola == 'Consola Activa':
    platform = st.selectbox('Plataforma', plataformas_activas)
elif estado_consola == 'Consola Secundaria':
    platform = st.selectbox('Plataforma', plataforma_secundaria)
else:
    platform = st.selectbox('Plataforma', plataforma_obsoleta)
genre = st.selectbox('Género', ['Sports', 'Platform', 'Racing', 'Role-Playing', 'Puzzle', 'Misc', 'Shooter', 'Simulation', 'Action', 'Fighting', 'Adventure', 'Strategy'])      # Ajusta también
price = st.number_input('Precio del videojuego (€)', min_value=29.99, max_value=69.99, value=29.99)
price_platform = st.number_input('Precio de la consola (€)', min_value=113.5, max_value=599.0, value=113.5)
modo_juego = st.selectbox('Modo de juego', ['Multijugador', 'Individual'])
pegi = st.selectbox('Clasificación PEGI', ['Infantil', 'Adulto', 'Adolescente'])
duracion_cat = st.selectbox('Duración estimada', ['Corto', 'Medio', 'Largo'])
year = st.number_input('Año del videojuego', min_value=1980, max_value=2020, value=1980)
nota_usuario = st.number_input('Nota del usuario', min_value=0, max_value=10, value=0)
n_votaciones = st.number_input('Nº votaciones', min_value=0, max_value=24855, value=5)
year_consola = st.number_input('Año de la consola', min_value=1977, max_value=2013, value=1977)
saga = st.selectbox('Saga', ['No saga', 'Saga'])
economia = st.selectbox('Situación economica', ['Crecimiento', 'Recesion'])
publisher = st.selectbox('Compañia', ['Nintendo', 'Microsoft Game Studios', 'Take-Two Interactive',
 'Sony Computer Entertainment', 'Activision', 'Ubisoft', 'Bethesda Softworks',
 'Electronic Arts', 'Sega'])



# Botón para predecir
if st.button('Predecir Ventas'):
    # Crear dataframe con los valores ingresados
    input_data = pd.DataFrame ({
        'Platform': [platform],
        'Genre': [genre],
        'Price': [price],
        'Modo Juego': [modo_juego],
        'PEGI_categoria': [pegi],
        'Duracion_juego_cat': [duracion_cat],
        'Year': [year],
        'Publisher': [publisher],  # valor típico o uno frecuente
        'User Score': [nota_usuario],
        'User Ratings Count': [n_votaciones],
        'Estado_Consola': [estado_consola],
        'Price_Platform': [price_platform],
        'Year_Consola': [year_consola],
        'Tipo_Saga': [saga],
        'Situacion_Economica': [economia],
        'Nombre_Base': ['JuegoGenérico'],
        'Precio_relativo': [price / price_platform],
        'Años_desde_lanzamiento_consola': [year - year_consola]
    })

prediccion = modelo.predict(input_data)[0]
st.success(f'Predicción estimada: **{prediccion}**')

if prediccion == 'Muy Alta':
    st.info('🔹 Estimación: entre 1.22 y 82.74 millones de unidades vendidas.')
elif prediccion == 'Alta':
    st.info('🔹 Estimación: entre 250 mil y 1.21 millones de unidades vendidas')
elif prediccion == 'Normal':
    st.info('🔹 Estimación: entre mil y 240 mil de unidades vendidas.')
