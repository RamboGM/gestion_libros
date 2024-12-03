from fastapi import FastAPI
import logging
from app.routes.book_routes import router

logging.basicConfig(
    filename="app.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger("main")

app = FastAPI(title="Gestión de Libros", version="1.0.0")

@app.on_event("startup")
def startup_event():
    logger.info("Starting the API...")

@app.on_event("shutdown")
def shutdown_event():
    logger.info("Shutting down the API...")

app.include_router(router, prefix="/api")

@app.get("/")
def read_root():
    logger.info("Root endpoint called")
    return {"message": "Bienvenido a la API de Gestión de Libros de ramboGM"}


