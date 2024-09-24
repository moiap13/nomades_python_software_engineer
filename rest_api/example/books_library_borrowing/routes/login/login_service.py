import os
import sys
import hashlib

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from routes.users.user_service import UserService
from utils.my_jwt import create_token

class LoginService:
  def __init__(self) -> None:
    self.user_service = UserService()

  def login(self, login_request: dict) -> str:
    username = login_request["username"]
    password = login_request["password"]

    try:
      user = self.user_service.get_user_by_username(username)
    except ValueError as e:
      raise ValueError("Wrong Credentials")

    pwd_h = hashlib.sha256((user.salt + password).encode()).hexdigest()

    if pwd_h != user.password:
      raise ValueError("Wrong Credentials")
    
    return create_token(user.id)

