from firebase_admin.firestore import DocumentReference, DocumentSnapshot

from .user import User

class UserMapper:
  @staticmethod
  def to_user(user: dict[str, str] | DocumentReference | DocumentSnapshot) -> User:
    user_dict: dict[str, str] = {}
    if isinstance(user, DocumentReference):
      user_dict.update({"id": user.id})
      user = user.get().to_dict()
    elif isinstance(user, DocumentSnapshot):
      user_dict.update({"id": user.id})
      user = user.to_dict()

    assert type(user) == dict

    user_dict.update(user)

    return User(
      id=user_dict.get("id", ""),
      firstname=user_dict.get("firstname", ""),
      lastname=user_dict.get("lastname", ""),
      username=user_dict.get("username", ""),
      email=user_dict.get("email", ""),
      salt=user_dict.get("salt", ""),
      password=user_dict.get("password", "")
    )

  @staticmethod
  def to_dict(user: User) -> dict[str, str]:
    return {
      'id': user.id,
      'firstname': user.firstname,
      'lastname': user.lastname,
      'username': user.username,
      'email': user.email,
      'salt': user.salt,
      'password': user.password
    }

  @staticmethod
  def to_firestore_dict(user: User) -> dict[str, str]:
    return {
      'firstname': user.firstname,
      'lastname': user.lastname,
      'username': user.username,
      'email': user.email,
      'salt': user.salt,
      'password': user.password
    }