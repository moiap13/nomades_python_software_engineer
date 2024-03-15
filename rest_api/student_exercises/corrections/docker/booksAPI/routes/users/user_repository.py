import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from firebase_admin.firestore import DocumentReference

from config.database import db

from .user import User

class UserRepository():
  def __init__(self):
    self.collection = db.collection(u"users")

  def get_all(self) -> list[User]:
    users: list[DocumentReference] = self.collection.get()
    users_ret = []
    for user in users: # each user is DocumentReference of firestore
      ud = user.to_dict() # to_dict that comes from firestore document snapshot
      assert "name" in ud and "email" in ud and "password" in ud
      users_ret.append(User(user.id, ud["name"], ud["email"], ud["password"]))
    return users_ret
  
  def insert_user(self, user: User) -> str:
    if len(self.collection.where(u"email", u"==", user.email).get()) > 0:
      raise Exception("User already exists")
    return self.collection.add(user.to_dict())[1].id # to_dict that comes from User class
