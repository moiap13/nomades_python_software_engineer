from firebase_admin.firestore import DocumentReference, DocumentSnapshot

from .book import Book

class BookMapper:
  @staticmethod
  def to_book(book_data: dict[str, str | list[str] | DocumentReference | DocumentSnapshot]) -> Book:
    book_dict: dict[str, str | list[str]] = {}
    if isinstance(book_data, DocumentReference):
      book_dict.update({"id": book_data.id})
      book_data = book_data.get().to_dict()
    elif isinstance(book_data, DocumentSnapshot):
      book_dict.update({"id": book_data.id})
      book_data = book_data.to_dict()

    assert type(book_data) == dict

    book_dict.update(book_data)

    return Book(
      id=book_dict.get("id", ""),
      title=book_dict.get("title", ""),
      isbn=book_dict.get("isbn", ""),
      authors=book_dict.get("authors", []),
    )
  
  @staticmethod
  def to_dict(book: Book, firestore: bool = False) -> dict[str, str | list[str]]:
    return {
      "isbn": book.isbn,
      "title": book.title,
      "authors": book.authors,
    } | ({"id": book.id} if not firestore else {})
