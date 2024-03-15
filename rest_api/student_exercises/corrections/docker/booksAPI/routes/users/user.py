class User():
  def __init__(self, id="", name="", email="", password=""):
    self.id = id
    self.name = name
    self.email = email
    self.password = password

  def to_dict(self):
    return {
      "name": self.name,
      "email": self.email,
      "password": self.password
    }
