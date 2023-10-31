# Steam Game Recommendation System

Este proyecto, realizado en el marco del primer proyecto individual de la etapa de labs, se enfoca en la creación de un sistema de recomendación de videojuegos para la plataforma multinacional Steam. Como MLOps Engineer, mi responsabilidad principal consistió en llevar el modelo de recomendación desde una etapa inicial de tratamiento y recolección de datos hasta su implementación y mantenimiento conforme llegaban nuevos datos.

## Estructura del Repositorio

La estructura del repositorio se organiza de la siguiente manera:

```
|-- data
    |-- raw: Datos crudos iniciales.
    |-- interim: Datos en tratamiento durante las etapas de ETL y EDA.
    |-- processed: Datos finales consumidos por la API.
|-- notebooks
    |-- 3 notebooks de ETL (Games, Reviews e Items) deben correrse antes del notbook ETL_Merge.ipynb
    |-- ETL_Merge.ipynb: Union de los datos, procesamiento final para la API
    |-- 3 notebooks de EDA (Games, Reviews e Items)
|-- src
    |-- main.py: Archivo principal de la API.
|-- .gitignore: Archivo para ignorar archivos y directorios no deseados.
|-- requirements.txt: Dependencias necesarias para ejecutar el proyecto.
|-- README.md: Descripción y guía del proyecto.
```

## Stack Tecnológico

- **Python**: Lenguaje principal para el desarrollo del proyecto.
- **Pandas**: Manipulación y análisis de datos.
- **FastAPI**: Framework para la creación de la API.
- **Scikit-learn**: Biblioteca para el entrenamiento del modelo de machine learning.
- **Render**: Plataforma para el despliegue de la API.
- **Parquet**: Formato de archivo para almacenamiento de datos en disco.

## Descripción de la API

La API creada con FastAPI se encarga de proporcionar recomendaciones de videojuegos basadas en distintos criterios. La API se encuentra alojada en Render y puede ser accedida a través del siguiente [link](https://your-api-link-on-render.com).

### Endpoints:

- **/developer/{desarrollador}**: Proporciona la cantidad de items y el porcentaje de contenido gratuito por año según la empresa desarrolladora.
- **/userdata/{User_id}**: Devuelve la cantidad de dinero gastado por el usuario, el porcentaje de recomendación y la cantidad de items.
- **/UserForGenre/{genero}**: Proporciona el usuario con más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.
- **/best_developer_year/{año}**: Devuelve el top 3 de desarrolladores con juegos más recomendados por usuarios para el año dado.
- **/developer_reviews_analysis/{desarrolladora}**: Según el desarrollador, devuelve un diccionario con el análisis de sentimientos de las reseñas de usuarios.
- **/recomendacion_juego/{id_de_producto}**: Proporciona una lista con 5 juegos recomendados similares al ingresado.
- **/recomendacion_usuario/{id_de_usuario}**: Proporciona una lista con 5 juegos recomendados para el usuario ingresado.

## Análisis Exploratorio de Datos (EDA)

Se realizó un análisis exploratorio para cada archivo (Games, Reviews e Items).

## Modelo de Aprendizaje Automático

El sistema de recomendación se basa en la similitud del coseno para proporcionar recomendaciones item-item y user-item. Los detalles del modelo y su entrenamiento se pueden encontrar en los notebooks correspondientes en la carpeta `notebooks`.

## Deployment

La API ha sido desplegada en Render para su consumo público. Puede acceder a la API a través del [link proporcionado](https://your-api-link-on-render.com).

## Disclaimer

Este proyecto tiene fines exclusivamente pedagógicos, simulando un entorno laboral para trabajar diversas temáticas ajustadas a la realidad. Los datos y resultados obtenidos en este proyecto no deben ser utilizados para la toma real de decisiones. 

## Enlaces de Interés

- [Video Demostrativo](https://your-video-link.com)
- [Documentación FastAPI](https://fastapi.tiangolo.com/)
- [Tutorial de Render](https://render.com/docs)

---

Para más detalles y consultas, no dude en contactar al autor del proyecto.