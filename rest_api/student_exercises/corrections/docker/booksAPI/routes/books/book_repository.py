import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from config.database import db

from firebase_admin.firestore import DocumentSnapshot

from .book import Book
from .book_mapper import toEntity

class BookRepository():
  def __init__(self):
    self.collection = db.collection(u"books")
  
  def get_all(self) -> list[Book]:
    books = self.collection.get()
    books_ret = []
    for book in books:
      bd = book.to_dict()
      assert "title" in bd and "summary" in bd
      books_ret.append(Book(book.id, bd["title"], bd["summary"]))
    return books_ret
  
  def insert_book(self, book: Book) -> None:
    self.collection.document(book.isbn).set(book.to_dict())

  def get_one(self, isbn: str) -> Book:
    firestore_book: DocumentSnapshot = self.collection.document(isbn).get()
    if not firestore_book.exists:
      raise Exception(f"Book with isbn {isbn} not found")
    
    return toEntity(firestore_book)
  
  def update_one(self, isbn: str, book: Book) -> None:
    self.collection.document(isbn).update(book.to_dict())

  def delete_one(self, isbn: str) -> None:
    self.collection.document(isbn).delete()
