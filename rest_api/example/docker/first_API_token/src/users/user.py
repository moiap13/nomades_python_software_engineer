import string
import random
import hashlib

class User():
  def __init__(self, 
               id: str = "",
               firstname: str = "",
               lastname: str = "",
               username: str = "",
               password: str = "",
               salt: str = ""
  ) -> None:
    self.id = id # firebase str id
    self.firstname = firstname
    self.lastname = lastname
    self.username = username
    self.password = password
    self.salt = salt 
  
  @staticmethod
  def from_dict(data: dict[str, str]) -> "User":
    return User(
      id=data.get("id", ""),
      firstname=data.get("firstname", ""),
      lastname=data.get("lastname", ""),
      username=data.get("username", ""),
      password=data.get("password", ""),
      salt=data.get("salt", "")
    )
  
  def __repr__(self) -> str:
    return f"<User {self.id}, {self.username}>"

  def __str__(self) -> str:
    return self.__repr__()
  
  def to_dict(self, with_id: bool = True) -> dict[str, str]:
    return {
      "firstname": self.firstname,
      "lastname": self.lastname,
      "username": self.username,
      "password": self.password,
      "salt": self.salt
    } | ({"id": self.id} if with_id else {})
  
  def generate_hash_pwd(self) -> None:
    if self.password == "":
      raise ValueError("password is missing, hashing impossible")
    
    self.salt = "".join(random.choices(string.ascii_letters, k=10))
    self.password = hashlib.sha256((self.password+self.salt).encode(encoding="utf-8")).hexdigest()
