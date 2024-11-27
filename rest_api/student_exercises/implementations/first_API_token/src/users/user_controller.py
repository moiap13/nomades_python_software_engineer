import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from flask import request

from flask.views import MethodView
from flask_smorest import Blueprint

from utils.exceptions import UserNotComplete, UserNotFound

from .dto.request import UserCreate, UpdateUser
from .dto.response import UserResponse, UserDataResponse
from .user_service import UserService
from .user import User

from utils.my_jwt import decode_token

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
class UserUniqueController(MethodView):
  @users.doc(description="Retrieve a single user given the id")
  @users.response(status_code=200, schema=UserDataResponse, description="The user with the given id")
  # @users.response(status_code=404)
  def get(self, id: str):
    try:
      return user_service.get_one(id)
    except UserNotFound as e:
      return {"message": str(e)}, 404
  
  @users.doc(description="Delete a specific user")
  @users.response(status_code=204)
  def delete(self, id: str):
    # TODO: protect the endpoint with token
    # The token will be placed in the headers of the reqeust, under the key 'Authorization'
    # The Authorization we accept is the Bearer Token Authorization
    # The Bearer Token authorization is a string in the form : 'Bearer <TOKEN>' 
    # TODO: Check that the 'Authorization' key is part of the headers of the request
    # TODO: check that the string for the key Authorization starts with Bearer
    # TODO: get the token (the token follows the Bearer keyword after a space)
    # TODO: use my_jwt.decode_token function to authenticate the user
    # PRO TIP: 
    # - The headers of the request are accessible to request.headers, where reqeust is the flask request object 
    # - The header variable is a dictionary, where the key is "Authorization"
    # - You can use start_with or split
    # TODO: If one steps fails ("Authorization" not in headers, token invalid, ...) returns a 401 with message "login first"

    return user_service.delete_user(id), 204

  @users.doc(description="update a specific user")
  @users.arguments(UpdateUser)
  @users.response(status_code=200, schema=UserDataResponse, description="The updated user")
  @users.response(status_code=422)
  def put(self, user_update_data: dict[str, str], id: str): # /!\ Be carreful, user_update_data is the body sent in the request (JSON) and id is the url parameter comming from the class decorator
    try:
      u = User.from_dict(user_update_data | {"id": id})
      return user_service.update_user(u).to_dict(), 200
    except ValueError as e:
      return {"message": str(e)}, 422