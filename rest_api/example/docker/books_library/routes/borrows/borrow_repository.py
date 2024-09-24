from config.firestore_db import db

class BorrowRepository:
  def __init__(self) -> None:
    self.collection = db.collection(u"borrowing")
  
  def get_borrowings_by_user_id(self, user_id: str) -> list[dict]: #TODO create a borrow obkect and change the return to return Borrow
    return [d.to_dict() for d in self.collection.where("user_id", "==", user_id).get()]