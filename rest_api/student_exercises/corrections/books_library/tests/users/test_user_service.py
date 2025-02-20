import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import unittest
import hashlib
from unittest.mock import patch

from src.users.user_service import UserService
from src.users.user import User
from src.users.user_exceptions import UserNotFound

from src._helpers.random_password_generator import generate_password

class TestUserService(unittest.TestCase):
  @patch('src.users.user_repository.UserRepository')
  def setUp(self, MockRepository):
    self.mock_repository = MockRepository()
    self.user_service = UserService()
    self.user_service.repository = self.mock_repository
  
  def test_create_user_win(self):
    #Arrange
    # random.seed(1)
    PASSWORD: str = "1234567890"
    add_user_request = User(id="", username="u1", email="test@test.com", firstname="test", lastname="test", password=PASSWORD)
    SALT: str = generate_password(True, True, False, False, 10)
    H_PASSWORD: str = hashlib.sha256((PASSWORD+SALT).encode()).hexdigest()

    self.mock_repository.get_user_by_email.side_effect = UserNotFound
    self.mock_repository.get_user_by_username.side_effect = UserNotFound

    mocked_user: User = User(id="1", username="u1", email="test@test.com", firstname="test", lastname="test", password=H_PASSWORD, salt=SALT)
    self.mock_repository.create_user.return_value = mocked_user

    #Act
    created_user: User = self.user_service.create_user(add_user_request)

    #Assert
    self.assertEqual(created_user.id, "1")
    self.assertEqual(created_user.username, "u1")
    self.assertEqual(created_user.email, "test@test.com")
    self.assertEqual(created_user.firstname, "test")
    self.assertEqual(created_user.lastname, "test")
    self.assertEqual(created_user.password, H_PASSWORD)
    self.assertEqual(created_user.salt, SALT)

    self.mock_repository.get_user_by_email.assert_called_once_with("test@test.com")
    self.mock_repository.get_user_by_username.assert_called_once_with("u1")
    self.mock_repository.create_user.assert_called_once_with(add_user_request)
  
  def test_create_user_fail_email_exists(self):
    #Arrange
    add_user_request = User(id="", username="u1", email="test@test.com", firstname="test", lastname="test", password="PASSWORD")
    self.mock_repository.get_user_by_email.return_value = User(id="")

    #Act & Assert
    with self.assertRaises(ValueError) as context:
      self.user_service.create_user(add_user_request)
      self.assertEqual(str(context.exception), "User with email=test@test.com already exists in database")
    


  def test_get_all_users(self):
    #Arrange
    mocked_users: list[User] = [User(id="1", username="u1", email="1@1.com"), User(id="2", username="u2", email="2@2.com")]
    self.mock_repository.get_all.return_value = mocked_users

    #Act
    users: list[User] = self.user_service.get_all()

    #Assert
    self.assertEqual(users, mocked_users)
    assert len(users) == 2
    for u in users:
      assert isinstance(u, User), "u should be of type User"
    
    self.mock_repository.get_all.assert_called_once()
  
  #TODO: Add tests for user_service.get_user_by_id 
  #TODO: Add tests for user_service.get_user_by_username 

if __name__ == '__main__':
  unittest.main()