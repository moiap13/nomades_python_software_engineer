import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import unittest
from unittest.mock import patch

from src.users.user import User

class TestUserClass(unittest.TestCase):

  def test_create_user(self):
    u = User()
    self.assertEqual(u.id, "")
    self.assertEqual(u.username, "")
    self.assertEqual(u.firstname, "")
    self.assertEqual(u.lastname, "")
    self.assertEqual(u.password, "")
    self.assertEqual(u.salt, "")
  
  def test_create_user_with_values(self):
    u = User("1", "Test", "Test", "test", "test", "test")
    self.assertEqual(u.id, "1")
    self.assertEqual(u.username, "test")
    self.assertEqual(u.firstname, "Test")
    self.assertEqual(u.lastname, "Test")
    self.assertEqual(u.password, "test")
    self.assertEqual(u.salt, "test")
  
  def test_create_user_from_dict(self):
    user_dict = {}
    u = User.from_dict(user_dict)
    self.assertEqual(u.id, "")
    self.assertEqual(u.username, "")
    self.assertEqual(u.firstname, "")
    self.assertEqual(u.lastname, "")
    self.assertEqual(u.password, "")
    self.assertEqual(u.salt, "")
  
  def test_create_user_from_dict_with_values(self):
    user_dict = {
      "id": "1",
      "username": "test",
      "firstname": "Test",
      "lastname": "Test",
      "password": "test",
      "salt": "test"
    }
    u = User.from_dict(user_dict)

    self.assertEqual(u.id, "1")
    self.assertEqual(u.username, "test")
    self.assertEqual(u.firstname, "Test")
    self.assertEqual(u.lastname, "Test")
    self.assertEqual(u.password, "test")
    self.assertEqual(u.salt, "test")

  def test_to_dict(self):
    u = User()
    user_dict = u.to_dict()

    self.assertTrue("id" in user_dict)
    self.assertEqual(user_dict["id"], "")
    self.assertTrue("username" in user_dict)
    self.assertEqual(user_dict["username"], "")
    self.assertTrue("firstname" in user_dict)
    self.assertEqual(user_dict["firstname"], "")
    self.assertTrue("lastname" in user_dict)
    self.assertEqual(user_dict["lastname"], "")
    self.assertTrue("password" in user_dict)
    self.assertEqual(user_dict["password"], "")
    self.assertTrue("salt" in user_dict)
    self.assertEqual(user_dict["salt"], "")

  def test_to_dict_with_values(self):
    u = User("1", "Test", "Test", "test", "test", "test")
    user_dict = u.to_dict()

    self.assertTrue("id" in user_dict)
    self.assertEqual(user_dict["id"], "1")
    self.assertTrue("username" in user_dict)
    self.assertEqual(user_dict["username"], "test")
    self.assertTrue("firstname" in user_dict)
    self.assertEqual(user_dict["firstname"], "Test")
    self.assertTrue("lastname" in user_dict)
    self.assertEqual(user_dict["lastname"], "Test")
    self.assertTrue("password" in user_dict)
    self.assertEqual(user_dict["password"], "test")
    self.assertTrue("salt" in user_dict)
    self.assertEqual(user_dict["salt"], "test")
  
  def test_representation(self):
    u = User("1", "", "", "test", "", "")
    repr = u.__repr__()
    self.assertEqual(repr, "<User 1, test>")

  def test_str(self):
    u = User("1", "", "", "test", "", "")
    repr = str(u)
    self.assertEqual(repr, "<User 1, test>") 

  def test_hash_password_win(self):
    u = User(password="test")
    with patch('random.choices', lambda values, k: ["a"]*10):
      u.generate_hash_pwd()
      self.assertEqual(u.salt, "".join(["a"]*10))
      self.assertEqual(u.password, "c036f6a9ebb0308ec638492371227f00f134ea6ee43aea1337df38474253acaa")

  def test_hash_password_fail(self):
    u = User()
    with self.assertRaises(ValueError) as ctx:
      u.generate_hash_pwd()

if __name__ == "__main__":
  unittest.main()