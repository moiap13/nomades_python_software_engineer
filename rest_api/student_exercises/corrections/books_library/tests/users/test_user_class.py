import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import unittest

from src.users.user import User

class TestUser(unittest.TestCase):
  def test_user_create_empty(self):
    user = User(id="")

    self.assertEqual(user.id, "")
    self.assertEqual(user.firstname, "")
    self.assertEqual(user.lastname, "")
    self.assertEqual(user.username, "")
    self.assertEqual(user.email, "")
    self.assertEqual(user.salt, "")
    self.assertEqual(user.password, "")
  
  def test_user_create_values(self):
    user = User(
      id="1",
      firstname="John",
      lastname="Doe",
      username="johndoe",
      email="johndoe@test.com",
      salt="salt",
      password="password"
    )

    self.assertEqual(user.id, "1")
    self.assertEqual(user.firstname, "John")
    self.assertEqual(user.lastname, "Doe")
    self.assertEqual(user.username, "johndoe")
    self.assertEqual(user.email, "johndoe@test.com")
    self.assertEqual(user.salt, "salt")
    self.assertEqual(user.password, "password")
  
  def test_user_repr(self):
    user = User(id="1", username="johndoe", email="johndoe@test.com")
    user_str = "User(id=1, username=johndoe, email=johndoe@test.com)"
    self.assertEqual(user.__repr__(), user_str)

if __name__ == "__main__":
  unittest.main()
