from firebase_admin.firestore import DocumentSnapshot, DocumentReference

from .borrowing import Borrowing

def toEntity(borrowing: dict | DocumentReference | DocumentSnapshot) -> Borrowing:
    b = Borrowing()
    if isinstance(borrowing, DocumentReference):
        borrowing = borrowing.get().to_dict()
    elif isinstance(borrowing, DocumentSnapshot):
        borrowing = borrowing.to_dict()
    b.end = borrowing.get('end', '')
    b.start = borrowing.get('start', '')
    b.book_isbn = borrowing.get('book_isbn', '')
    return b

def toResponse(borrowing: Borrowing) -> dict:
    return {
        "book_isbn": borrowing.book_isbn,
        "start": borrowing.start,
        "end": borrowing.end
    }