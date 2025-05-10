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

# Botón para predecir
if st.button('Predecir Ventas'):
    # Crear dataframe con los valores ingresados
    input_data = pd.DataFrame({
        'Platform': [platform],
        'Genre': [genre],
        'Price': [price],
        'Modo Juego': [modo_juego],
        'PEGI_Categoria': [pegi],
        'Duracion_ juego_cat': [duracion_cat],
        
        # Rellenar automáticamente el resto de variables
        'Year': [2024],
        'Publisher': ['Electronic Arts'],  # valor típico o uno frecuente
        'User_Score': [7.5],
        'User Ratings Count': [300],
        'Estado_Consola': ['Actual'],
        'Price_Platform': [299.99],
        'Year_Consola': [2017],
        'Años_desde_lanzamiento_consola': [2024 - 2017],
        'Precio_relativo': [price / 299.99],
        'Nombre_Base': ['BaseName'],
        'Tipo_Saga': ['No Saga'],
        'Situacion_Economica': ['Crecimiento']
    })

    # Predecir
    prediccion = modelo.predict(input_data)[0]
    st.success(f'Predicción estimada: **{prediccion}**')
