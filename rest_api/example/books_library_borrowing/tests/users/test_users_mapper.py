import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import unittest
from unittest.mock import MagicMock
from firebase_admin.firestore import DocumentReference, DocumentSnapshot

from routes.users.user import User
from routes.users.user_mapper import UserMapper


class TestUserMapper(unittest.TestCase):

  def setUp(self):
    # Initialize UserMapper
    self.user_mapper = UserMapper()

    # Create a sample User object for testing
    self.user = User(
        id="1",
        firstname="John",
        lastname="Doe",
        username="johndoe",
        password="hashedpassword",
        salt="randomsalt"
    )

  def test_to_user_from_dict(self):
    # Test converting a dictionary to a User object
    user_dict = {
        "id": "1",
        "firstname": "John",
        "lastname": "Doe",
        "username": "johndoe",
        "password": "hashedpassword",
        "salt": "randomsalt"
    }
    
    user = self.user_mapper.to_user(user_dict)
    self.assertEqual(user.id, "1")
    self.assertEqual(user.firstname, "John")
    self.assertEqual(user.lastname, "Doe")
    self.assertEqual(user.username, "johndoe")
    self.assertEqual(user.password, "hashedpassword")
    self.assertEqual(user.salt, "randomsalt")

  def test_to_user_from_document_snapshot(self):
    # Mock a DocumentSnapshot
    doc_snapshot = MagicMock(spec=DocumentSnapshot)
    doc_snapshot.id = "1"
    doc_snapshot.to_dict.return_value = {
        "firstname": "John",
        "lastname": "Doe",
        "username": "johndoe",
        "password": "hashedpassword",
        "salt": "randomsalt"
    }

    user = self.user_mapper.to_user(doc_snapshot)
    self.assertEqual(user.id, "1")
    self.assertEqual(user.firstname, "John")
    self.assertEqual(user.lastname, "Doe")
    self.assertEqual(user.username, "johndoe")
    self.assertEqual(user.password, "hashedpassword")
    self.assertEqual(user.salt, "randomsalt")

  def test_to_user_from_document_reference(self):
    # Mock a DocumentReference and its `get()` method
    doc_reference = MagicMock(spec=DocumentReference)
    doc_reference.id = "1"
    mock_snapshot = MagicMock()
    mock_snapshot.to_dict.return_value = {
        "firstname": "John",
        "lastname": "Doe",
        "username": "johndoe",
        "password": "hashedpassword",
        "salt": "randomsalt"
    }
    doc_reference.get.return_value = mock_snapshot

    user = self.user_mapper.to_user(doc_reference)
    self.assertEqual(user.id, "1")
    self.assertEqual(user.firstname, "John")
    self.assertEqual(user.lastname, "Doe")
    self.assertEqual(user.username, "johndoe")
    self.assertEqual(user.password, "hashedpassword")
    self.assertEqual(user.salt, "randomsalt")

  def test_to_dict(self):
    # Test converting a User object to a dictionary
    user_dict = self.user_mapper.to_dict(self.user)
    self.assertEqual(user_dict["id"], "1")
    self.assertEqual(user_dict["firstname"], "John")
    self.assertEqual(user_dict["lastname"], "Doe")
    self.assertEqual(user_dict["username"], "johndoe")
    self.assertEqual(user_dict["password"], "hashedpassword")
    self.assertEqual(user_dict["salt"], "randomsalt")

  def test_to_firestore_dict(self):
    # Test converting a User object to a Firestore-compatible dictionary
    firestore_dict = self.user_mapper.to_firestore_dict(self.user)
    self.assertNotIn("id", firestore_dict)  # `id` should not be included
    self.assertEqual(firestore_dict["firstname"], "John")
    self.assertEqual(firestore_dict["lastname"], "Doe")
    self.assertEqual(firestore_dict["username"], "johndoe")
    self.assertEqual(firestore_dict["password"], "hashedpassword")
    self.assertEqual(firestore_dict["salt"], "randomsalt")


if __name__ == "__main__":
  unittest.main()
