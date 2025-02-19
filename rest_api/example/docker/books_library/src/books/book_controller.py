import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from flask.views import MethodView
from flask import g
from flask_smorest import Blueprint, abort
from flask_smorest.error_handler import ErrorSchema

from .dto.request.book_create import CreateBook
from .dto.response.book_response import BookResponse
from .book_service import BookService
from .book_mapper import BookMapper
from .book import Book
from .book_exception import BookNotFound

from src._helpers.decorators import authenticated



books_bp = Blueprint("books", "books", url_prefix="/books", description="Books objects")

book_service = BookService()

@books_bp.route("/")
class BooksGlobalController(MethodView):

  @authenticated
  @books_bp.doc(description="Retrieve all the books in database")
  @books_bp.response(status_code=200, schema=BookResponse(many=True))
  def get(self):
    print(g.user_id)
    return book_service.get_all()


  @books_bp.doc(description="Insert a new book in database")
  @books_bp.arguments(CreateBook)
  @books_bp.response(status_code=201, schema=BookResponse)
  def post(self, book: dict):
    return book_service.create_book(BookMapper.to_book(book))

@books_bp.route("/isbn/<isbn>")
@books_bp.doc(description="Get a book by it's isbn value")
@books_bp.response(status_code=404, schema=ErrorSchema)
@books_bp.response(status_code=200, schema=BookResponse)
def get_book_by_isbn(isbn: str):
  try:
    return book_service.get_book_by_isbn(isbn)
  except BookNotFound as e:
    abort(404, {"message": str(e)})