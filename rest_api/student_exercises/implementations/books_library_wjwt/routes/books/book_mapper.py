from firebase_admin.firestore import DocumentReference, DocumentSnapshot

from .book import Book

class BookMapper:
    def to_book(self, book: dict | DocumentSnapshot | DocumentReference) -> Book:
        book_dict = {}
        if isinstance(book, DocumentReference):
            book_dict.update({"id" : book.id})
            book = book.get().to_dict()      
        elif isinstance(book, DocumentSnapshot):
            book_dict.update({"id" : book.id})
            book = book.to_dict()

        book_dict.update(book)

        return Book(
            book_dict.get("id", ""),
            book_dict.get("title", ""),
            book_dict.get("isbn", ""),
            book_dict.get("authors", "")            
        )

    def to_dict(self, book: Book) -> dict:
        return {
            u"id": book.id,
            u"title": book.title,
            u"isbn": book.isbn,
            u"authors": book.authors
        }

    def to_firestore_dict(self, book: Book) -> dict:
        return {
            u"title": book.title,
            u"isbn": book.isbn,
            u"authors": book.authors
        }
    
    def to_firestore_update_dict(self, book: Book) -> dict:
      ud = {}
      if book.title:
          ud.update({u"title": book.title})
      if book.isbn:
          ud.update({u"isbn": book.isbn})
      if book.authors:
          ud.update({u"authors": book.authors})

      return ud
