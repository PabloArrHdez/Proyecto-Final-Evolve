#  Predicción de Ventas de Videojuegos

Este proyecto es un producto mínimo viable (MVP) desarrollado como parte de un TFM de Data Science. Consiste en un modelo predictivo que estima la categoría de ventas de un videojuego en el momento de su lanzamiento, usando características clave del mismo. El modelo está integrado en una aplicación interactiva mediante **Streamlit**.

---

##  ¿Qué hace esta aplicación?

Permite al usuario:
- Introducir información sobre un videojuego (género, consola, precio, etc.)
- Obtener una predicción automática de ventas clasificadas en:
  - `Muy Alta`: +2 millones de copias vendidas.
  - `Alta`: entre 1 y 2 millones de copias vendida.
  - `Normal`: menos de 1 millón de copias vendidas

---

##  Modelo utilizado

Se ha entrenado un modelo de **Random Forest Classifier** con un pipeline de preprocesamiento (escalado de variables numéricas + codificación One-Hot).  
El modelo alcanza una precisión del **70%** con tres clases desbalanceadas.

---

##  Variables independientes utilizadas

- Plataforma (`Platform`)
- Año de lanzamiento (`Year`)
- Género (`Genre`)
- Precio del juego (`Price`)
- Estado de la consola (`Estado_Consola`)
- Clasificación PEGI (`PEGI_categoria`)
- Modo de juego (`Modo Juego`)
- Duración estimada (`Duracion_juego_cat`)
- Nota de usuarios (`User Score`)
- N.º de valoraciones (`User Ratings Count`)
- Precio consola (`Price_Platform`)
- Año consola (`Year_Consola`)
- Años desde el lanzamiento de la consola
- Situación económica global del año

Las variables ocultas (`Publisher`, `Precio_relativo`, `Nombre_Base`) son gestionadas automáticamente por el sistema.

---

##  Resultados del modelo

```text
Random Forest Classification Report:
  Accuracy: 70%
  - Muy Alta: Precision 0.70, Recall 0.38
  - Alta: Precision 0.57, Recall 0.48
  - Normal: Precision 0.75, Recall 0.88
```

---

##  Autor

**Pablo Arrastia Hernández**  
Trabajo Final para el Master en Data Science & IA | Evolve 2025