import hashlib

from .login_repository import LoginRepository

class LoginService():
  def __init__(self):
    self.login_repository = LoginRepository()

  def login(self, email, password) -> str:
    password = hashlib.sha256(password.encode()).hexdigest()
    return self.login_repository.login(email, password)