import hashlib

from .user_repository import UserRepository
from .user import User

class UserService():
  def __init__(self):
    self.user_repository = UserRepository()

  def get_all(self) -> list[User]:
    return self.user_repository.get_all()
  
  def create_new_user(self, user: User) -> User:
    user.password = hashlib.sha256(user.password.encode()).hexdigest()
    user.id = self.user_repository.insert_user(user)
    return user
  