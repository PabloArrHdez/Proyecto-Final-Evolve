import streamlit as st
### IMAGEN DE FONDO ####
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://images.pexels.com/photos/15763947/pexels-photo-15763947/free-photo-of-tecnologia-divertido-videojuegos-juego-de-azar.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    h1, h2, h3, h4, h5, h6, p, div, span {{
        color: white !important;
    }}
        section[data-testid="stSidebar"] > div {{
        background-color: rgba(0, 0, 0, 0.5);
    }}
    
    /* Estilo para los tabs */
    div[data-testid="stTabs"] > div {{
        background-color: rgba(0, 0, 0, 0.4);
        border-radius: 12px;
        padding: 20px;
        margin-top: 20px;
        border: 1px solid white;
        box-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
    }}
        /* Créditos de la imagen */
    .credit {{
        position: fixed;
        bottom: 10px;
        right: 10px;
        font-size: 13px;
        background-color: rgba(0, 0, 0, 0.6);
        padding: 6px 10px;
        border-radius: 8px;
        color: white;
        border: 1px solid white;
        box-shadow: 0 0 6px rgba(255, 255, 255, 0.4);
        z-index: 100;
    }}
        .credit a {{
        color: white;
        text-decoration: underline;
    }}
    </style>

    <div class="credit">
        Foto de <a href="https://www.pexels.com/es-es/@hellojoshwithers/" target="_blank">Josh Withers</a> en <a href="https://www.pexels.com/es-es/" target="_blank">Pexels</a>
    </div>
    """,
    unsafe_allow_html=True)


# Título con color personalizado (usando HTML)
st.markdown("<h1 style='color: #000000;'>Descripción de los Datos</h1>", unsafe_allow_html=True)

# Texto descriptivo con estilo CSS (color, tamaño, fuente, etc.)
st.markdown("""
<div style='color: #000000; font-size: 16px;'>
Este conjunto de datos, previo a una posterior limpieza, unión y transformación de los mismos, simula las características que influyen en las ventas globales de un videojuego en el año que sale al mercado.

<ul>
<li><b>Platform</b>: Videoconsola disponible para jugar.</li>
<li><b>Year</b>: Año de lanzamiento del videojuego.</li>
<li><b>Genre</b>: Género del videojuego.</li>
<li><b>Publisher</b>: Empresa que desarrolla el juego.</li>
<li><b>User_Score</b>: Puntuación del cliente (0-10) en la página web 'Metacritic.com'.</li>
<li><b>User Ratings Count</b>: Número de veces que han puntuado.</li>
<li><b>Estado_Consola</b>: Situación en el mercado actual de la videoconsola.</li>
<li><b>Price</b>: Precio del videojuego, en Euros (€), de salida al mercado.</li>
<li><b>Price_Platform</b>: Precio de salida, en Euros (€), de la videoconsola al mercado.</li>
<li><b>Year_Consola</b>: Año en el que salió la videoconsola.</li>
<li><b>Modo Juego</b>: Opción del videojuego de jugar varios jugadores o es individual.</li>
<li><b>Años_desde_lanzamiento_consola</b>: Tiempo desde que salió al mercado la consola hasta que salió el juego.</li>
<li><b>Precio_relativo</b>: Precio del juego en relación con el precio de la consola.</li>
<li><b>PEGI_Categoria</b>: Clasificación de edad recomendada por contenido.</li>
<li><b>Duración_juego_cat</b>: Tiempo de duración principal según el género.</li>
<li><b>Tipo_Saga</b>: Indica si pertenece a una saga.</li>
<li><b>Situacion_Economica</b>: Situación económica global en el año de lanzamiento.</li>
</ul>
</div>
""", unsafe_allow_html=True)
