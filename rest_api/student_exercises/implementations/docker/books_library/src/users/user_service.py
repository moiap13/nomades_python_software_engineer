import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import hashlib

from _helpers.random_password_generator import generate_password

from .user import User
from .user_repository import UserRepository
from .user_exceptions import UserNotFound

class UserService:
  def __init__(self) -> None:
    self.repository = UserRepository()
  
  def create_user(self, user: User) -> User:
    try:
      self.repository.get_user_by_email(user.email)
    except UserNotFound:
      pass
    else:
      raise ValueError(f"User with email={user.email} already exists in database")

    try:
      self.repository.get_user_by_username(user.username)
    except UserNotFound:
      pass
    else:
      raise ValueError(f"User with username={user.username} already exists in database") 

    user.salt = generate_password(True, True, False, False, 10)
    user.password = hashlib.sha256((user.password+user.salt).encode()).hexdigest()

    return self.repository.create_user(user)
  
  def get_all(self) -> list[User]:
    return self.repository.get_all()
  
  def get_user_by_username(self, username: str):
    return self.repository.get_user_by_username(username)

  def get_user_by_id(self, user_id: str) -> User:
    return self.repository.get_user_by_id(user_id)