from flask.views import MethodView
from flask_smorest import Blueprint

from utils.exceptions import UserNotComplete, UserNotFound

from .dto.request import UserCreate, UpdateUser
from .dto.response import UserResponse, UserDataResponse
from .user_service import UserService
from .user import User

users = Blueprint("users", "users", url_prefix="/users", description="Users operations")

user_service = UserService()

# @users.route("/")
# def get_all():
#   pass

# @users.route("/", methods=["POST"])
# def post_all():
#   pass


@users.route("/")
class UserController(MethodView):
  @users.doc(description="Returns all the users of the system")
  @users.response(status_code=200, schema=UserResponse(many=True), description="list of username and id")
  def get(self):
    # return [u.to_dict() for u in user_service.get_all()]
    return user_service.get_all()

  
  @users.doc(description="Add a user in the system")
  @users.arguments(UserCreate)
  @users.response(status_code=201, schema=UserDataResponse, description="The inserted user")
  @users.response(status_code=422)
  @users.response(status_code=400)
  def post(self, user_data: dict[str, str]):
    try:
      return user_service.add_user(User.from_dict(user_data)).to_dict()
    except ValueError as e:
      return {"message": str(e)}, 422
    except UserNotComplete as e:
      return {"message": str(e)}, 400
    
# TODO: Add routes for working with a specific user
# TODO: Add methos get, put, delete on route /users/<id>
@users.route("/<id>")
class UserController(MethodView):
  @users.arguments(UpdateUser)
  def put(self, user_update_data: dict[str, str], id: str): # /!\ Be carreful, user_update_data is the body sent in the request (JSON) and id is the url parameter comming from the class decorator
    pass