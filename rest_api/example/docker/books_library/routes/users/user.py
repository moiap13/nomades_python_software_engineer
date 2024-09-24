class User:
  def __init__(self, 
    id: str = "", 
    firstname:str = "", 
    lastname:str = "", 
    username:str = "", 
    password:str = "", 
    salt:str = "",
    *args, **kwargs
  ) -> None:
    self.id = id
    self.firstname = firstname
    self.lastname = lastname
    self.username = username
    self.password = password
    self.salt = salt

  def __repr__(self) -> str:
    return f"User({self.username}, {self.id})"

  def __str__(self) -> str:
    return self.__repr__