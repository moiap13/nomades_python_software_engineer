import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from firebase_admin.firestore import DocumentSnapshot, DocumentReference

from src.books.book import Book
from src.users.user import User
from src.books.book_mapper import BookMapper
from src.users.user_mapper import UserMapper

from .borrow import Borrow

class BorrowMapper:
  @staticmethod
  def to_borrow(borrow_data: dict | DocumentReference | DocumentSnapshot) -> Borrow:
    borrow_dict: dict[str, dict | float] = {}
    if isinstance(borrow_data, DocumentReference):
      borrow_id = borrow_data.id
      borrow_data: dict[str, float | DocumentReference] = borrow_data.get().to_dict()
      borrow_data["id"] = borrow_id

      book_data: dict[str, str | list[str]] = borrow_data["book"].get().to_dict()
      book_data["id"] = borrow_data["book"].id

      user_data: dict[str, str | list[str]] = borrow_data["user"].get().to_dict()
      user_data["id"] = borrow_data["user"].id

      borrow_data["book"] = book_data
      borrow_data["user"] = user_data
    elif isinstance(borrow_data, DocumentSnapshot):
      borrow_id = borrow_data.id
      borrow_data: dict[str, float | DocumentReference] = borrow_data.to_dict()
      borrow_data["id"] = borrow_id
      
      book_data: dict[str, str | list[str]] = borrow_data["book"].get().to_dict()
      book_data["id"] = borrow_data["book"].id

      user_data: dict[str, str | list[str]] = borrow_data["user"].get().to_dict()
      user_data["id"] = borrow_data["user"].id

      borrow_data["book"] = book_data
      borrow_data["user"] = user_data
    
    assert type(borrow_data) == dict

    borrow_dict.update(borrow_data)

    return Borrow(
      id=borrow_dict.get("id", ""),
      user=UserMapper.to_user(borrow_dict["user"]),
      book=BookMapper.to_book(borrow_dict["book"]),
      start=borrow_dict.get("start", None),
      end=borrow_dict.get("end", None)
    )

  def to_firestore_dict(db, borrow: Borrow) -> dict:
    return {
      "user": db.collection(u"users").document(borrow.user.id),
      "book": db.collection(u"books").document(borrow.book.id),
      "start": borrow.start,
      "end": borrow.end
    }