from fastapi import APIRouter, HTTPException, Depends
from app.models.book import Book
from app.services.book_service import BookService
from typing import List
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

book_service = BookService()

@router.get("/books", response_model=List[Book])
async def get_books():
    logger.info("Fetching all books")
    return book_service.get_books()

@router.post("/books", response_model=Book)
async def create_book(book: Book):
    try:
        logger.info(f"Creating book: {book}")
        # El id no se envía, el repositorio lo generará automáticamente
        return book_service.create_book(book.title, book.author, book.year)
    except ValueError as e:
        logger.error(f"Error creating book: {e}")
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, updated_book: Book):
    try:
        logger.info(f"Updating book with ID {book_id}")
        updated_data = updated_book.dict(exclude_unset=True)
        return book_service.update_book(book_id, updated_data)
    except ValueError as e:
        logger.error(f"Error updating book: {e}")
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/books/{book_id}", response_model=Book)
async def delete_book(book_id: int):
    try:
        logger.info(f"Deleting book with ID {book_id}")
        return book_service.delete_book(book_id)
    except ValueError as e:
        logger.error(f"Error deleting book: {e}")
        raise HTTPException(status_code=404, detail=str(e))
