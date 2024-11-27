import json
from typing import List
from app.models.book import Book

BOOKS_FILE = "books.json"

def load_books() -> List[Book]:
    """Carga los libros desde el archivo JSON."""
    try:
        with open(BOOKS_FILE, "r", encoding="utf-8") as file:
            books_data = json.load(file)
            return [Book(**book) for book in books_data]
    except FileNotFoundError:
        return []

def save_books(books: List[Book]) -> None:
    """Guarda la lista de libros en el archivo JSON."""
    with open(BOOKS_FILE, "w", encoding="utf-8") as file:
        json.dump([book.dict() for book in books], file, ensure_ascii=False, indent=4)
