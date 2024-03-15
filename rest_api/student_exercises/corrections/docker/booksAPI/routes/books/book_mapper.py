from firebase_admin.firestore import DocumentSnapshot, DocumentReference

from .book import Book

def toEntity(book: dict | DocumentReference | DocumentSnapshot) -> Book:
    b = Book()
    if isinstance(book, DocumentReference):
        b.isbn = book.id
        book = book.get().to_dict()
    elif isinstance(book, DocumentSnapshot):
        b.isbn = book.id
        book = book.to_dict()
    b.title = book.get('title', '')
    b.summary = book.get('summary', '')
    return b

def toResponse(book: Book) -> dict:
    return {
        "isbn": book.isbn,
        "title": book.title,
        "summary": book.summary
    }