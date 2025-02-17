import uuid

from flask.views import MethodView
from flask_smorest import Blueprint
from flask_smorest.error_handler import ErrorSchema

from .dto.request.create_user import CreateUserRequest
from .dto.response.user_response import UserResponse, UserIdentifier
from .dto.response.user_response_list import UserResponseList
from .user import User
from .user_mapper import UserMapper
from .user_service import UserService
from .user_exceptions import UserNotFound

users_bp: Blueprint = Blueprint("users", "users", url_prefix="/users", description="Users routes")
user_service = UserService()

@users_bp.route("/")
class UserGlobalController(MethodView):
  @users_bp.doc(description="Retrieve a list of all the users in the system")
  @users_bp.response(status_code=200, schema=UserResponseList, description="A list containing all the users of the system")
  def get(self):
    users = [
      User(
        id=str(uuid.uuid4()),
        firstname="John",
        lastname="Doe",
        username="johndoe",
        email="johndoe@test.com",
        password="password"
      ), User(
        id=str(uuid.uuid4()),
        firstname="Jane",
        lastname="Doe",
        username="janedoe",
        email="janedoe@test.com",
        password="password"
      )
    ]

    return {"users": users}

  @users_bp.doc(description="Add a user in the system")
  @users_bp.arguments(schema=CreateUserRequest)
  # @users_bp.response(status_code=201, schema=UserResponse, description="Return the inserted user")
  # @users_bp.response(status_code=422, schema=ErrorSchema, description="")
  def post(self, create_user_data: dict[str, str]):
    try:
      return UserMapper.to_dict(user_service.create_user(UserMapper.to_user(create_user_data)))
    except ValueError as e:
      return {"message": str(e)}, 422

@users_bp.route("/<id>")
class UsersSpecificController(MethodView):
  def get(self):
    pass

  def put(self):
    pass

  def delete(self):
    pass

@users_bp.route("/username/<username>")
def get_user_by_username(username: str): 
  try:
    return UserMapper.to_dict(user_service.get_user_by_username(username))
  except UserNotFound as e:
    return {"message": str(e)}, 404
  except ValueError as e:
    return {"message": "Contact administrator"}, 500
