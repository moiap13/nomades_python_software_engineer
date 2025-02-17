from flask import Flask
from flask_smorest import Api

from src.users.user_controller import users_bp

app = Flask(__name__)

class APIConfig:
  API_TITLE = "Books Library"
  API_VERSION = "v1"
  OPENAPI_VERSION = "3.0.2"
  OPENAPI_URL_PREFIX = "/"
  OPENAPI_SWAGGER_UI_PATH = "/docs"
  OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

app.config.from_object(APIConfig)

api = Api(app)
api.register_blueprint(users_bp)

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=8081)