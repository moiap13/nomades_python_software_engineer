class User:
  def __init__(
    self, 
    id: str = "", 
    firstname: str = "", 
    lastname: str = "", 
    username: str = "",
    email: str = "",
    salt: str = "",
    password: str = ""
  ) -> None:
    self.id = id
    self.firstname = firstname
    self.lastname = lastname
    self.username = username
    self.email = email
    self.salt = salt
    self.password = password

  def __str__(self) -> str:
    return f"User(id={self.id}, username={self.username}, email={self.email})"
  
  def __repr__(self) -> str:
    return self.__str__()
