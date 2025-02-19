import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import hashlib

from _helpers.my_jwt import create_token

from src.users.user_repository import UserRepository
from src.users.user_exceptions import UserNotFound

class LoginService:
  def __init__(self) -> None:
    self.repository = UserRepository()
  
  def login(self, login_request: dict[str, str]) -> str:
    username_email: str = login_request.get("username_email", "")
    pwd: str = login_request.get("password", "")
    try:
      user = self.repository.get_user_by_email(username_email)
    except UserNotFound as e:
      user = self.repository.get_user_by_username(username_email)
    
    assert user != None

    h_pwd: str = hashlib.sha256((pwd+user.salt).encode()).hexdigest()

    if h_pwd != user.password:
      raise ValueError("Wrong Cendentials")

    return create_token(user.id)
    