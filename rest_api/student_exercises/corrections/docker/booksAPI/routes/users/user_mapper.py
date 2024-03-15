from .user import User

def toEntity(user: dict) -> User:
  return User("", user["name"], user["email"], user["password"])
