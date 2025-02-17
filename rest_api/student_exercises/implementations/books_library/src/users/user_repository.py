import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from firebase_admin.firestore import DocumentSnapshot

from config.firestore_db import db

from .user import User
from .user_mapper import UserMapper
from .user_exceptions import UserNotFound

class UserRepository:
  def __init__(self) -> None:
    self.collection = db.collection(u"users")
  
  def create_user(self, user: User) -> User:
    _, user_ref = self.collection.add(UserMapper.to_firestore_dict(user))
    user.id = user_ref.id
    return user
  
  def get_user_by_username(self, username: str) -> User:
    """
    Returns the user with the username given in parameters
    """
    users: list[DocumentSnapshot] = self.collection.where("username", "==", username).get()

    if len(users) > 1:
      raise ValueError(f"Many users with username={username}")
    if len(users) == 0:
      raise UserNotFound(f"User with username={username} doesn't exist in database")
    
    return UserMapper.to_user(users[0])

  def get_user_by_email(self, email: str) -> User:
    """
    Returns the user with the email given in parameters
    """
    users: list[DocumentSnapshot] = self.collection.where("email", "==", email).get()

    if len(users) > 1:
      raise ValueError(f"Many users with email={email}")
    if len(users) == 0:
      raise UserNotFound(f"User with email={email} doesn't exist in database")
    
    return UserMapper.to_user(users[0])