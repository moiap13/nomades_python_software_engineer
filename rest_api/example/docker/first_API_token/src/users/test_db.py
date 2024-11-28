from user_service import UserService
from user import User

us = UserService()

u = User("", "Test3", "Test3", "test3", "123456", "")
print(us.add_user(u))
print(us.get_all())