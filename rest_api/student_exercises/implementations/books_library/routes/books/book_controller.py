from flask.views import MethodView
from flask_smorest import Blueprint

books = Blueprint("books", "books", url_prefix="/books", description="Books routes")
