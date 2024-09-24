import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import firebase_admin.firestore as fs
from google.api_core.exceptions import NotFound

from config.firestore_db import db

from .book import Book
from .book_mapper import BookMapper

class BookRepository:
    def __init__(self) -> None:
        self.collection = db.collection(u"books")
        self.mapper = BookMapper()

    def get_all(self) -> list[Book]:
        return [self.mapper.to_book(b) for b in self.collection.get()]

    def get_one(self, book_id: str) -> Book:
        book = self.collection.document(book_id).get()

        if not book.exists:
            raise ValueError(f"Book with id {book_id} doesn't exist")
        
        return self.mapper.to_book(book)

    def create_book(self, book: Book) -> Book:
        _, book_ref = self.collection.add(self.mapper.to_firestore_dict(book))
        book.id = book_ref.id

        return self.mapper.to_dict(book)


    def get_book_by_isbn(self, isbn: str) -> list[Book]:
        return [self.mapper.to_book(b) for b in self.collection.where(filter=fs.firestore.FieldFilter("isbn", "==", isbn)).get()]
    
    def delete_one(self, book_id: str) -> None:
        self.collection.document(book_id).delete()

    def update_book(self, book: Book, book_id: str) -> Book:
      try:
        self.collection.document(book_id).update(self.mapper.to_firestore_update_dict(book))
      except NotFound as e:
        raise ValueError(f"Book with id {book_id} doesn't exist")
      
      return self.get_one(book_id)