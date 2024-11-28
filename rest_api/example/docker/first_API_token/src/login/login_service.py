import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import hashlib

from src.users.user_repository import UserRepository
from src.users.user import User

from utils.exceptions import UserNotFound
from utils.my_jwt import create_token

class LoginService:
  def __init__(self):
    self.repository = UserRepository()

  def login(self, username: str, password: str) -> str:
    try:
      u: User = self.repository.get_user_by_username(username)
    except UserNotFound as e:
      raise ValueError("Wrong credentials")
    
    h_pwd: str = hashlib.sha256((password+u.salt).encode(encoding='utf-8')).hexdigest()
    if h_pwd != u.password:
      raise ValueError("Wrong credentials")

    return create_token(u.id)
