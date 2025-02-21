import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import unittest

from src.users.user import User
from src.users.user_mapper import UserMapper

class TestUserMapper(unittest.TestCase):
  def test_dict_to_user_win(self):
    user_dict = {
      "id": "1",
      "username": "u1",
      "email": "test@test.com",
      "firstname": "test",
      "lastname": "test",
      "password": "password",
      "salt": "salt"
    }

    u = UserMapper.to_user(user_dict)

    self.assertEqual(u.id, "1")
    self.assertEqual(u.username, "u1")
    self.assertEqual(u.email, "test@test.com")
    self.assertEqual(u.firstname, "test")
    self.assertEqual(u.lastname, "test")
    self.assertEqual(u.password, "password")
    self.assertEqual(u.salt, "salt")

  def test_user_to_dict_win(self):
    u = User(
      id="1",
      username="u1",
      email="test@test.com",
      firstname="test",
      lastname="test",
      password="password",
      salt="salt"
    )

    u_dict = UserMapper.to_dict(u)

    self.assertEqual(u_dict["id"], "1")
    self.assertEqual(u_dict["username"], "u1")
    self.assertEqual(u_dict["email"], "test@test.com")
    self.assertEqual(u_dict["firstname"], "test")
    self.assertEqual(u_dict["lastname"], "test")
    self.assertEqual(u_dict["password"], "password")
    self.assertEqual(u_dict["salt"], "salt")

  def test_user_to_firestoredict_win(self):
    u = User(
      id="1",
      username="u1",
      email="test@test.com",
      firstname="test",
      lastname="test",
      password="password",
      salt="salt"
    )

    u_dict = UserMapper.to_firestore_dict(u)

    self.assertEqual(u_dict["username"], "u1")
    self.assertEqual(u_dict["email"], "test@test.com")
    self.assertEqual(u_dict["firstname"], "test")
    self.assertEqual(u_dict["lastname"], "test")
    self.assertEqual(u_dict["password"], "password")
    self.assertEqual(u_dict["salt"], "salt")
    self.assertFalse("id" in u_dict)

if __name__ == "__main__":
  unittest.main()