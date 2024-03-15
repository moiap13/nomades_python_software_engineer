from flask import Flask
from flask_smorest import Api

from routes.books.book_controller import books
from routes.users.user_controller import users
from routes.login.login_controller import login
from routes.borrowings.borrowing_controller import borrowings

server = Flask(__name__)
class APIConfig:
  API_TITLE = "Books API"
  API_VERSION = "v1"
  OPENAPI_VERSION = "3.0.2"
  OPENAPI_URL_PREFIX = "/"
  OPENAPI_SWAGGER_UI_PATH = "/docs"
  OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
  OPENAPI_REDOC_PATH = "/redoc"
  OPENAPI_REDOC_UI_URL = "https://cdn.jsdelivr.net/npm/redoc@latest/bundles/redoc.standalone.js"

server.config.from_object(APIConfig)

api = Api(server)

api.register_blueprint(books)
api.register_blueprint(users)
api.register_blueprint(login)
api.register_blueprint(borrowings)

if __name__ == "__main__":
  server.run(debug=True, port=5050, host="0.0.0.0")