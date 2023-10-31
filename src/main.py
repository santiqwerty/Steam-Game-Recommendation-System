from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

# Cargar los DataFrames desde archivos Parquet
data_files = {
    "developer": pd.read_parquet('data/processed/developer_data.parquet'),
    "userdata": pd.read_parquet('data/processed/userdata_data.parquet'),
    "best_developer_year": pd.read_parquet('data/processed/best_developer_year_data.parquet'),
    "developer_reviews_analysis": pd.read_parquet('data/processed/developer_reviews_analysis_data.parquet'),
    "UserForGenre": pd.read_parquet('data/processed/UserForGenre_data.parquet'),
    "recomendacion_juego": pd.read_parquet('data/processed/recomendaciones_juego.parquet'),
    #"recomendacion_usuario": pd.read_parquet('data/processed/recomendaciones_usuario.parquet')
}

@app.get("/developer/{desarrollador}")
async def developer(desarrollador: str):
    try:
        data = data_files["developer"].loc[desarrollador]
        # Convertir el DataFrame a un diccionario donde cada clave es el nombre de la columna
        # y cada valor es una lista de valores de esa columna.
        result = data.to_dict(orient='list')
        return result
    except KeyError:
        raise HTTPException(status_code=404, detail="No se encontraron datos para el argumento proporcionado.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/userdata/{User_id}")
async def userdata(User_id: str):
    try:
        data = data_files["userdata"].loc[User_id]
        return data.to_dict()
    except KeyError:
        raise HTTPException(status_code=404, detail="No se encontraron datos para el argumento proporcionado.")

@app.get("/best_developer_year/{año}")
async def best_developer_year(año: int):
    try:
        # Convertir año a flotante
        año_float = float(año)
        data = data_files["best_developer_year"].loc[año_float]
        return data.to_dict()
    except KeyError:
        raise HTTPException(status_code=404, detail="No se encontraron datos para el argumento proporcionado.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/developer_reviews_analysis/{desarrolladora}")
async def developer_reviews_analysis(desarrolladora: str):
    try:
        data = data_files["developer_reviews_analysis"].loc[desarrolladora]
        return data.to_dict()
    except KeyError:
        raise HTTPException(status_code=404, detail="No se encontraron datos para el argumento proporcionado.")

@app.get("/UserForGenre/{genero}")
async def UserForGenre(genero: str):
    try:
        data = data_files["UserForGenre"].loc[genero]
        return data.to_dict()
    except KeyError:
        raise HTTPException(status_code=404, detail="No se encontraron datos para el argumento proporcionado.")

# Renombrar la columna __index_level_0__ a id_producto
data_files["recomendacion_juego"] = data_files["recomendacion_juego"].rename(columns={"__index_level_0__": "id_producto"})

# Verificar el tipo de datos de la columna id_producto
if data_files["recomendacion_juego"]['id_producto'].dtypes != 'int64':
    # Si no es int, convertir la columna id_producto a int
    data_files["recomendacion_juego"]['id_producto'] = data_files["recomendacion_juego"]['id_producto'].astype('int64')

@app.get("/recomendacion_juego/{id_producto}")
async def recomendacion_juego(id_producto: int):  # Asegúrate de que id_producto es del tipo correcto (int o str)
    try:
        # Ahora puedes buscar directamente por id_producto
        data = data_files["recomendacion_juego"].set_index('id_producto').loc[id_producto]
        return data.to_dict()
    except KeyError:
        raise HTTPException(status_code=404, detail="No se encontraron datos para el argumento proporcionado.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/recomendacion_usuario/{id_usuario}")
async def recomendacion_usuario(id_usuario: str):
    try:
        data = data_files["recomendacion_usuario"].loc[id_usuario]
        return data.to_dict()
    except KeyError:
        raise HTTPException(status_code=404, detail="No se encontraron datos para el argumento proporcionado.")

if __name__ == "__main__":
    import uvicorn
    # Inicia el servidor FastAPI.
    uvicorn.run(app, host="0.0.0.0", port=8000)