from fastapi import FastAPI
from app.routes.book_routes import router

app = FastAPI(title="Gestión de Libros", version="1.0.0")

app.include_router(router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "¡Bienvenido a la API de Gestión de Libros!"}


