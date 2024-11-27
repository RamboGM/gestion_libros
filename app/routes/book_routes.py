from fastapi import APIRouter, HTTPException
from app.models.book import Book
from app.database import load_books, save_books
from typing import List

router = APIRouter()

@router.get("/books", response_model=list[Book])
async def get_books():
    books = load_books()
    return books

@router.post("/books", response_model=List[Book])
async def create_books(books: List[Book]):
    existing_books = load_books()
    existing_books.extend(books)
    save_books(existing_books)
    return books

@router.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, updated_book: Book):
    books = load_books()
    for book in books:
        if book.id == book_id:
            book.title = updated_book.title
            book.author = updated_book.author
            book.genre = updated_book.genre
            save_books(books)
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@router.delete("/books/{book_id}", response_model=Book)
async def delete_book(book_id: int):
    books = load_books()
    for book in books:
        if book.id == book_id:
            books.remove(book)
            save_books(books)
            return book
    raise HTTPException(status_code=404, detail="Book not found")
