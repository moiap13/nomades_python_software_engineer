from flask_smorest import Blueprint


from .login_service import LoginService
from .dto.request import LoginUser
from .dto.response import LoginToken

login = Blueprint("login", "login", url_prefix="/login", description="Login operations")

login_service = LoginService()

@login.route("/", methods=["POST"])
@login.arguments(LoginUser)
@login.response(status_code=200, schema=LoginToken)
@login.response(status_code=401)
def post(login_data: dict[str, str]):
  try:
    return {"token": login_service.login(login_data["username"], login_data["password"])}
  except ValueError as e:
    return {"message": str(e)}, 401