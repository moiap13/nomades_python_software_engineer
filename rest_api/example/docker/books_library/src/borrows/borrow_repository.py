import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from firebase_admin.firestore import DocumentSnapshot, DocumentReference
from firebase_admin import firestore

from config.firestore_db import db

from .borrow import Borrow
from .borrow_mapper import BorrowMapper

class BorrowRepository:
  def __init__(self) -> None:
    self.collection = db.collection(u"borrows")
  
  def get_borrows_per_user(self, user_id: str) -> list[Borrow]:
    user_doc_ref: DocumentReference = db.collection(u"users").document(user_id)
    borrows: list[DocumentSnapshot] = self.collection.where("user", "==", user_doc_ref).order_by("end", direction=firestore.Query.DESCENDING).get()
    return [BorrowMapper.to_borrow(borrow) for borrow in borrows]

  def borrow(self, borrow_request: Borrow) -> Borrow:
    _, doc_ref = self.collection.add(BorrowMapper.to_firestore_dict(db, borrow_request))
    borrow_request.id = doc_ref.id
    return borrow_request
