import os, sys
ROOT_DIR: str = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(ROOT_DIR)

import requests
from dotenv import dotenv_values

from .book import Book
from .book_repository import BookRepository

GOOGLE_BOOKS_API_KEY: str = dotenv_values(os.path.join(ROOT_DIR, ".env"))["GOOGLE_BOOKS_API_KEY"]

class BookService:
  def __init__(self) -> None:
    self.repository = BookRepository()
  
  def create_book(self, book: Book) -> Book:
    if book.isbn:
      response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=isbn:{book.isbn}&key={GOOGLE_BOOKS_API_KEY}")
      if response.status_code == 200:
        google_book_data = response.json()
        if "items" in google_book_data and google_book_data.get("totalItems", 0) > 0:
          google_book_data = google_book_data["items"][0]
          if "volumeInfo" in google_book_data:
            book.title = google_book_data["volumeInfo"]["title"] if "title" in google_book_data["volumeInfo"] else book.title
            book.authors = google_book_data["volumeInfo"]["authors"] if "authors" in google_book_data["volumeInfo"] else book.authors

    return self.repository.create_book(book)
  
  def get_all(self) -> list[Book]:
    return self.repository.get_all()

  def get_book_by_isbn(self, isbn: str) -> Book:
    return self.repository.get_book_by_isbn(isbn)
