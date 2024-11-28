from .user_repository import UserRepository
from .user import User

class UserService:
  def __init__(self):
    self.repository = UserRepository()

  def get_all(self) -> list[User]:
    return self.repository.get_all()
  
  def get_one(self, id: str) -> User:
    return self.repository.get_one(id)
  
  def add_user(self, user: User) -> User:
    if self.is_username_taken(user.username):
      raise ValueError(f"username '{user.username}' already exists in database")

    user.generate_hash_pwd()
    return self.repository.add_user(user)
  
  def update_user(self, user: User) -> User:
    if user.password != "":
      user.generate_hash_pwd()
    
    if user.username != "":
      if self.is_username_taken(user.username):
        raise ValueError(f"username '{user.username}' already exists in database")

    return self.repository.update_user(user)

  def delete_user(self, id):
    return self.repository.delete_user(id)
  
  def get_user_by_username(self, username: str) -> User:
    return self.repository.get_user_by_username(username)
  
  def is_username_taken(self, username: str) -> bool:
    return len(self.repository.get_users_by_username(username)) != 0
