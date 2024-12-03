from app.repositories.book_repository import BookRepository
from app.models.book import Book
import logging

logger = logging.getLogger(__name__)

class BookService:
    def __init__(self):
        self.repository = BookRepository()

    def create_book(self, title: str, author: str, year: int):
        book = Book(id=0, title=title, author=author, year=year)
        created_book = self.repository.create(book)
        logger.info(f"Book creation request: {created_book}")
        return created_book

    def get_books(self):
        logger.info("Service layer: fetching all books")
        return self.repository.get_all()

    def get_book(self, book_id: int):
        logger.info(f"Service layer: fetching book with ID {book_id}")
        return self.repository.get_by_id(book_id)

    def update_book(self, book_id: int, data: dict):
        logger.info(f"Service layer: updating book with ID {book_id}")
        book = self.repository.get_by_id(book_id)
        if not book:
            logger.error(f"Service layer: book with ID {book_id} does not exist")
            raise ValueError(f"Book with ID {book_id} does not exist")
        updated_book = self.repository.update(book_id, data)
        logger.info(f"Service layer: book with ID {book_id} updated")
        return updated_book

    def delete_book(self, book_id: int):
        logger.info(f"Service layer: deleting book with ID {book_id}")
        return self.repository.delete(book_id)
