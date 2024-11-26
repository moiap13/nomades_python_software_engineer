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
    # TODO: check that the username is unique, if the username doesn't exists in db we add the user in db, else raise a Value error
    user.generate_hash_pwd()
    return self.repository.add_user(user)
  
  def update_user(self, user: User) -> User:
    if user.password != "":
      user.generate_hash_pwd()

    return self.repository.update_user(user)

  def get_user_by_username(self, username: str) -> User:
    return self.repository.get_user_by_username(username)
