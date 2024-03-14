from flask_smorest import Blueprint

from utils.my_jwt import issue_token

from .login_service import LoginService

from .dto.request.login_request import LoginRequest
from .dto.response.login_response import LoginResponse

login = Blueprint("login", "login", url_prefix="/", description="Login API")

login_service = LoginService()

@login.route("/login", methods=["POST"])
@login.arguments(LoginRequest)
@login.response(status_code=200, schema=LoginResponse)
@login.response(status_code=401)
def login_request(login_request: dict):
  try:
    email = login_request["email"]
    password = login_request["password"]
    user_id = login_service.login(email, password)
    return {"token": issue_token(user_id)}, 200
  except Exception as e:
    return {"message": str(e)}, 401

