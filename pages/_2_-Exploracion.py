import streamlit as st
import pandas as pd

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://images.pexels.com/photos/4522998/pexels-photo-4522998.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    h1, h2, h3, h4, h5, h6, p, div, span {{
        color: black !important;
    }}
        section[data-testid="stSidebar"] > div {{
        background-color: rgba(255, 255, 255, 0.8);
    }}
        /* Créditos de la imagen */
    .credit {{
        position: fixed;
        bottom: 10px;
        right: 10px;
        font-size: 13px;
        background-color: rgba(245, 245, 245, 1.0);
        padding: 6px 10px;
        border-radius: 8px;
        color: white;
        border: 1px solid white;
        box-shadow: 0 0 6px rgba(255, 255, 255, 0.4);
        z-index: 100;
    }}
        .credit a {{
        color: black;
        text-decoration: underline;
    }}
    </style>

    <div class="credit">
        Foto de <a href="https://www.pexels.com/es-es/@polina-tankilevitch/" target="_blank">Polina Tankilevitch</a> en <a href="https://www.pexels.com/es-es/" target="_blank">Pexels</a>
    </div>
    """,
    unsafe_allow_html=True
)

st.title ("Explorador de videojuegos desde 1980 hasta 2020")

df = pd.read_csv('Data/video_games_sales_completo.csv')

st.dataframe(df)
st.sidebar.header("Filtrar")
estado_consola = st.sidebar.multiselect("Estado Consola", df["Estado_Consola"].unique())
genero = st.sidebar.multiselect("Genero", df["Genre"].unique())
pegi_categoria = st.sidebar.multiselect("PEGI", df["PEGI_categoria"].unique())
duracion_juego = st.sidebar.multiselect("Duración", df["Duracion_juego_cat"].unique())
precio_min, precio_max = df["Price"].min(), df["Price"].max()
price_range = st.sidebar.slider("Precio Videojuego", precio_min, precio_max, (precio_min, precio_max))


df_filtrado = df[
    (df["Estado_Consola"].isin(estado_consola)) &
    (df["Genre"].isin(genero)) &
    (df["PEGI_categoria"].isin(pegi_categoria)) &
    (df["Duracion_juego_cat"].isin(duracion_juego)) &
    (df["Price"].between(price_range[0], price_range[1]))
]

st.write (f"Se econtró {df_filtrado.shape[0]} videojuegos")
st.dataframe(df_filtrado)