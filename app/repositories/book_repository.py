from app.models.book import Book
import logging
from app.database import load_books, save_books, get_next_id

logger = logging.getLogger(__name__)

class BookRepository:
    def __init__(self):
        self.books = load_books()
        self.counter = get_next_id(self.books)  

    def create(self, book: Book):
        book.id = self.counter 
        self.books.append(book)
        self.counter += 1 
        save_books(self.books) 
        logger.info(f"Book created with ID {book.id}: {book}")
        return book

    def get_all(self):
        logger.info("Fetching all books")
        return self.books

    def get_by_id(self, book_id: int):
        book = next((book for book in self.books if book.id == book_id), None)
        if book:
            logger.info(f"Book found with ID {book_id}: {book}")
        else:
            logger.warning(f"Book with ID {book_id} not found")
        return book

    def update(self, book_id: int, data: dict):
        books = self.get_all()
        for book in books:
            if book.id == book_id:
                for key, value in data.items():
                    setattr(book, key, value)
                save_books(books)
                logger.info(f"Book updated with ID {book_id}: {book}")
                return book
        logger.error(f"Failed to update: Book with ID {book_id} not found")
        raise ValueError(f"Book with ID {book_id} not found")
    
    def delete(self, book_id: int):
        book = self.get_by_id(book_id)
        if book:
            self.books.remove(book)
            save_books(self.books)
            logger.info(f"Book deleted with ID {book_id}: {book}")
        else:
            logger.warning(f"Failed to delete: Book with ID {book_id} not found")
        return book
