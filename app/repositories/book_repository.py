from app.models.book import Book

class BookRepository:
    def __init__(self):
        self.books = []
        self.counter = 1

    def create(self, book: Book):
        book.id = self.counter
        self.books.append(book)
        self.counter += 1
        return book

    def get_all(self):
        return self.books

    def get_by_id(self, book_id: int):
        return next((book for book in self.books if book.id == book_id), None)

    def update(self, book_id: int, data: dict):
        book = self.get_by_id(book_id)
        if book:
            for key, value in data.items():
                setattr(book, key, value)
        return book

    def delete(self, book_id: int):
        book = self.get_by_id(book_id)
        if book:
            self.books.remove(book)
        return book
