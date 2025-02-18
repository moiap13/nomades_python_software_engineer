from flask_smorest import Blueprint, abort

from .dto.request.login_request import LoginRequest
from .dto.response.login_response import LoginResponse
from .login_service import LoginService

login_bp = Blueprint("login", "login", description="Login routes")
login_service = LoginService()

@login_bp.route("/login", methods=["POST"])
@login_bp.arguments(LoginRequest)
@login_bp.response(status_code=401)
@login_bp.response(status_code=200, schema=LoginResponse)
def login_user(login_request: dict[str, str]):
  try:
    return {"token": login_service.login(login_request)}
  except Exception:
    abort(401)