from fastapi import FastAPI
from app.tmdb_client import get_popular_movies  # Importamos el nuevo nombre

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

# ... después de app = FastAPI() ...

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permitimos conexiones desde cualquier origen para desarrollo
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/movies/popular")
async def popular_movies():
    movies = await get_popular_movies()
    return {"results": movies}