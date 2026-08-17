import os
import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = os.getenv("TMDB_BASE_URL", "https://api.themoviedb.org/3")

async def get_popular_movies():
    """
    Consulta la API de TMDB de forma asincrónica y devuelve una lista limpia de películas.
    """
    url = f"{BASE_URL}/movie/popular"
    params = {
        "api_key": API_KEY,
        "language": "es-ES"
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            # Procesamos la respuesta aquí mismo para entregar datos limpios
            movies = [
                {
                    "title": m.get("title"),
                    "year": m.get("release_date", "").split("-")[0] if m.get("release_date") else "S/D"
                }
                for m in data.get("results", [])
            ]
            return movies
        except Exception as e:
            print(f"Error accediendo a TMDB: {e}")
            return []