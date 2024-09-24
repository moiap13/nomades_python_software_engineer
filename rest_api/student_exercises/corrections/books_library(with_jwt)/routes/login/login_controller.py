from flask_smorest import Blueprint

from .dto.request.login_request import LoginRequest
from .login_service import LoginService

login = Blueprint("login", "login", url_prefix="/login", description="Login routes")
login_service = LoginService()

@login.route("/", methods=["POST"])
@login.arguments(LoginRequest)
@login.response(status_code=200)
@login.response(status_code=401)
def login_user(login_request: dict):
  try:
    return {"token" : login_service.login(login_request)}
  except ValueError as e:
    return {"message": str(e)}, 401
