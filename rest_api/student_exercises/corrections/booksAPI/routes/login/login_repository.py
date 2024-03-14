import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from firebase_admin.firestore import DocumentReference

from config.database import db

class LoginRepository:
    def __init__(self):
      self.collection = db.collection(u"users")

    def login(self, email, password) -> str:
      user = self.collection.where(u"email", u"==", email).where(u"password", u"==", password).get()
      if len(user) == 0:
          raise Exception("User and email not corresponding")
      return user[0].id
        
        