from app.repositories.book_repository import BookRepository
from app.models.book import Book

class BookService:
    def __init__(self):
        self.repository = BookRepository()

    def create_book(self, title: str, author: str, year: int):
        book = Book(id=0, title=title, author=author, year=year)
        return self.repository.create(book)

    def get_books(self):
        return self.repository.get_all()

    def get_book(self, book_id: int):
        return self.repository.get_by_id(book_id)

    def update_book(self, book_id: int, data: dict):
        return self.repository.update(book_id, data)

    def delete_book(self, book_id: int):
        return self.repository.delete(book_id)
