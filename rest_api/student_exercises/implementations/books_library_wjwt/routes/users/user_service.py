import hashlib
import random
import string

from .user import User
from .user_repository import UserRepository
from .user_mapper import UserMapper

class UserService:
  def __init__(self) -> None:
    self.repository = UserRepository()
    self.mapper = UserMapper()

  def get_all(self) -> list[User]:
    return self.repository.get_all()
  
  def create_user(self, user: User) -> User:
    # TODO: check if user already exists (based on username)
    user_with_username: list[User] = self.repository.get_user_by_username(user.username)
    if len(user_with_username) > 0:
      raise ValueError(f"user with username {user.username} already exists")
    
    # TODO: salt and hash password
    salt: str = "".join(random.choices(string.ascii_letters + string.digits, k=10))
    h_pwd = hashlib.sha256((salt + user.password).encode()).hexdigest()

    user.salt = salt
    user.password = h_pwd

    # TODO: insert user in db
    return self.repository.create_user(user)
