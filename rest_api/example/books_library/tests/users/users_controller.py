import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from flask_smorest import Api
from routes.users.user_controller import users

class TestUserController(unittest.TestCase):
    def setUp(self):
        # Setup the Flask test client
        self.app = Flask(__name__)

        class APIConfig:
          API_TITLE = "Books Library Testing"
          API_VERSION = "v0"  
          OPENAPI_VERSION = "3.0.2"

        self.app.config.from_object(APIConfig)

        self.api = Api(self.app)
        self.api.register_blueprint(users)
        self.client = self.app.test_client()
    
    @patch('routes.users.user_service.UserService')
    @patch('routes.users.user_mapper.UserMapper')
    def test_get_all_users(self, MockUserMapper, MockUserService):
        # Mock UserService and UserMapper within user_controller.py
        mock_service_instance = MockUserService.return_value
        mock_mapper_instance = MockUserMapper.return_value

        # Mock get_all return value
        mock_user = MagicMock()
        mock_service_instance.get_all.return_value = [mock_user]
        mock_mapper_instance.to_dict.return_value = {
            "id": "1",
            "firstname": "John",
            "lastname": "Doe",
            "username": "johndoe",
            "password": "hashedpassword",
            "salt": "randomsalt"
        }

        # Debugging: Print to verify mock setup
        print("Mock get_all return value:", mock_service_instance.get_all())
        print("Mock to_dict return value:", mock_mapper_instance.to_dict(mock_user))

        # Perform GET request to /users/
        response = self.client.get("/users/")
        data = response.get_json()

        # Debugging: Print response data
        print("Response JSON:", data)

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertIn("users", data)
        self.assertEqual(len(data["users"]), 1)
        self.assertEqual(data["users"][0]["username"], "johndoe")

    @patch('routes.users.user_service.UserService')
    @patch('routes.users.user_mapper.UserMapper')
    def test_create_user_success(self, MockUserMapper, MockUserService):
        # Create mock service and mapper
        mock_service = MockUserService.return_value
        mock_mapper = MockUserMapper.return_value

        # Setup the mock return values
        mock_user = MagicMock()
        mock_mapper.to_user.return_value = mock_user
        mock_service.create_user.return_value = mock_user
        mock_mapper.to_dict.return_value = {
            "id": "1",
            "firstname": "John",
            "lastname": "Doe",
            "username": "johndoe",
            "password": "hashedpassword",
            "salt": "randomsalt"
        }

        # Define the input data
        input_data = {
            "firstname": "John",
            "lastname": "Doe",
            "username": "johndoe",
            "password": "password123",
            "email": "test@gmail.com"
        }

        # Call the endpoint
        response = self.client.post("/users/", json=input_data)
        data = response.get_json()

        print(data)

        # Assertions
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data["username"], "johndoe")
        self.assertEqual(data["firstname"], "John")

    @patch('routes.users.user_service.UserService')
    @patch('users.user_mapper.UserMapper')
    def test_create_user_conflict(self, MockUserMapper, MockUserService):
        # Create mock service and mapper
        mock_service = MockUserService.return_value
        mock_mapper = MockUserMapper.return_value

        # Setup the mock to raise ValueError
        mock_mapper.to_user.return_value = MagicMock()
        mock_service.create_user.side_effect = ValueError("user with username johndoe already exists")

        # Define the input data
        input_data = {
            "firstname": "John",
            "lastname": "Doe",
            "username": "johndoe",
            "password": "password123",
            "email": "test@gmail.com"
        }

        # Call the endpoint
        response = self.client.post("/users/", json=input_data)
        data = response.get_json()

        # Assertions
        self.assertEqual(response.status_code, 422)
        self.assertIn("message", data)
        self.assertEqual(data["message"], "user with username johndoe already exists")

if __name__ == '__main__':
    unittest.main()
