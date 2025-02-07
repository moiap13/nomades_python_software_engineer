class User:
  def __init__(
    self, uid:str, pwd:str, salt:str, pp_filename:str,
    firstname:str, lastname:str, email:str, age:int
  ):
    self.uid = uid
    self.pwd = pwd
    self.salt = salt
    self.pp_filename = pp_filename
    self.firstname = firstname
    self.lastname = lastname
    self.email = email
    self.age = age
  
  def __str__(self) -> str:
    return f"User<{self.uid}>"

  def __repr__(self) -> str:
    return self.__str__()

  def to_dict(self, full=False) -> dict[str, str | int]:
    return {
      u"uid": self.uid,
      u"firstname": self.firstname,
      u"lastname": self.lastname,
      u"age": self.age,
      u"email": self.email,
      u"profile_picture_filename": self.pp_filename
    } | ({ u"pwd": self.pwd, u"salt": self.salt} if full else {})
  
  @staticmethod
  def from_dict(user_data: dict[str, str | int]) -> "User":
    return User(
      uid=user_data.get("uid", ""),
      pwd=user_data.get("pwd", ""),
      salt=user_data.get("salt", ""),
      pp_filename=user_data.get("profile_picture_filename", ""),
      firstname=user_data.get("firstname", ""),
      lastname=user_data.get("lastname", ""),
      email=user_data.get("email", ""),
      age=user_data.get("age", 0)
    )


      