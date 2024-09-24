import string

from .book import Book
from .book_mapper import BookMapper
from .book_repository import BookRepository

class BookService:
    def __init__(self) -> None:
        self.repository = BookRepository()
        self.mapper = BookMapper()

    def get_all(self) -> list[Book]:
        return self.repository.get_all()
    
    def get_one(self, book_id) -> Book:
        return self.repository.get_one(book_id)
    
    def get_book_by_isbn(self, isbn: str) -> Book:
        isbn_book_list = self.repository.get_book_by_isbn(isbn)

        if len(isbn_book_list) != 1:
            raise ValueError(f"Book with ISBN {isbn} doesn't exist or there are multiple books with the same ISBN")

        return isbn_book_list[0]
    
    def create_book(self, book: Book) -> Book:
        # TODO: check if book already exists (based on ISBN)

        # Insert book in db
        return self.repository.create_book(book)
    
    def delete_one(self, book_id: str) -> None:
        return self.repository.delete_one(book_id)
    
    def update_book(self, book: Book, book_id: str) -> Book:
        # Check if book exists
        # b = self.get_one(book_id)


        # Update book in db
        return self.repository.update_book(book, book_id)
