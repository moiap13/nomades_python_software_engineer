from firebase_admin.firestore import DocumentReference, DocumentSnapshot

from .user import User

class UserMapper:
  def to_user(self, user: dict | DocumentSnapshot) -> User:
    user_dict = {}
    if isinstance(user, DocumentReference):
      user_dict.update({"id" : user.id})
      user = user.get().to_dict()      
    elif isinstance(user, DocumentSnapshot):
      user_dict.update({"id" : user.id})
      user = user.to_dict()

    user_dict.update(user)

    return User(
      user_dict.get("id", ""),
      user_dict.get("firstname", ""),
      user_dict.get("lastname", ""),
      user_dict.get("username", ""),
      user_dict.get("password", ""),
      user_dict.get("salt", "")
    )
  
  def to_dict(self, user: User) -> dict:
    return {
      u"id": user.id,
      u"firstname": user.firstname,
      u"lastname": user.lastname,
      u"username": user.username,
      u"password": user.password,
      u"salt": user.salt
    }

  def to_firestore_dict(self, user: User) -> dict:
    return {
      u"firstname": user.firstname,
      u"lastname": user.lastname,
      u"username": user.username,
      u"password": user.password,
      u"salt": user.salt
    }