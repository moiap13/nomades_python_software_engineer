import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

# Library imports
from flask import g
from flask.views import MethodView
from flask_smorest import Blueprint

# root imports
from utils.my_jwt import issue_token
from utils.decorators import authenticated
from routes.login.dto.response.login_response import LoginResponse

# current dir imports
from .user_service import UserService
from .user_mapper import toEntity

# DTO imports
from .dto.request.user_create import UserCreateRequest
from .dto.response.user_response import UserResponse

users = Blueprint("users", "users", url_prefix="/users", description="Users API")

user_service = UserService()

@users.route("/")
class BooksCollection(MethodView):
  @users.response(status_code=200, schema=UserResponse(many=True))
  @authenticated
  def get(self):
    print("g.user_id", g.user_id)
    return user_service.get_all()
    

  @users.arguments(UserCreateRequest)
  @users.response(status_code=201, schema=LoginResponse)
  @users.response(status_code=401)
  def post(self, user: dict):
    try:
      return {
        "token": issue_token(user_service.create_new_user(toEntity(user)).id)
      }, 201
    except Exception as e:
      return {"message": str(e)}, 401

