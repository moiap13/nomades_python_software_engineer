import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import unittest
from unittest.mock import patch, MagicMock

from routes.users.user_service import UserService
from routes.users.user import User

class TestUserService(unittest.TestCase):
  @patch('routes.users.user_repository.UserRepository')
  def setUp(self, MockRepository):
    # create a mock instance of UserRepository
    self.mock_repository = MockRepository()
    self.user_service = UserService()
    self.user_service.repository = self.mock_repository
  
  def test_get_all_users(self):
    # Arrange
    users: list[User] = [User(username="u1"), User(username="u2")]
    self.mock_repository.get_all.return_value = users

    # Act
    result = self.user_service.get_all()

    # Assert
    self.assertEqual(result, users)
    assert len(result) == 2
    for r in result:
      assert isinstance(r, User), "r should be of type User"

    self.mock_repository.get_all.assert_called_once()
  
  def test_create_user_success(self):
    # Arrange
    new_user = User(username='newuser', password='password123')
    self.mock_repository.get_user_by_username.return_value = []
    self.mock_repository.create_user.return_value = new_user

    # Act
    created_user: User = self.user_service.create_user(new_user)

    # Assert
    self.assertEqual(created_user.username, 'newuser')
    self.assertNotEqual(created_user.password, 'password123') # the returned password should be hashed
    self.assertIsNotNone(created_user.salt)
    import hashlib
    self.assertEqual(created_user.password, hashlib.sha256((created_user.salt + 'password123').encode()).hexdigest())
    self.mock_repository.get_user_by_username.assert_called_once_with("newuser")
    self.mock_repository.create_user.assert_called_once()

  # def test_create_user_failure(self):
  #   # Arrange
  #   existing_user = User(username='existinguser', password='password123')
  #   self.mock_repository.get_user_by_username.return_value = [existing_user]

  #   # Act & Assert
  #   with self.assertRaises(ValueError) as context:
  #       self.user_service.create_user(existing_user)

  #   self.assertEqual(str(context.exception), 'user with username existinguser already exists')
  #   self.mock_repository.get_user_by_username.assert_called_once_with('existinguser')
  #   self.mock_repository.create_user.assert_not_called()

if __name__ == "__main__":
  unittest.main()