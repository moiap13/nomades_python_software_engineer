import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from flask.views import MethodView
from flask_smorest import Blueprint

from utils.decorators import authenticated

from .dto.response.book_response import BookResponse
from .dto.request.create_book import CreateBook
from .dto.request.update_book import UpdateBook

from .book_service import BookService
from .book_mapper import toResponse, toEntity

books = Blueprint("books", "books", url_prefix="/books", description="Books API")

book_service = BookService()

@books.route("/")
class BooksCollection(MethodView):
  @books.response(status_code=200, schema=BookResponse(many=True))
  @authenticated
  def get(self):
    return book_service.get_all() 

  @books.arguments(CreateBook)
  @books.response(status_code=201, schema=BookResponse)
  @authenticated
  def post(self, book):
    return book_service.create_new_book(book)
  
@books.route("/<isbn>") # /books/{isbn} | I suggest you to avoid using spaces in isbn
class BookItem(MethodView):
  # TODO implement book item endpoint and logic
  # Don't forget to work with DTO
  # all the interractions with the database should be done using the book_repository class
  # all the logic about book item should be done inside the book_service
  @books.response(status_code=200, schema=BookResponse)
  @books.response(status_code=404)
  @authenticated
  def get(self, isbn):
    try:
      return toResponse(book_service.get_one(isbn)), 200
    except Exception as e:
      return {"error": str(e)}, 404

  @books.arguments(UpdateBook)
  @books.response(status_code=200, schema=BookResponse)
  @books.response(status_code=404)
  @authenticated
  def put(self,updated_book ,isbn):
    try:
      return toResponse(book_service.update_one(isbn, toEntity(updated_book)))
    except Exception as e:
      return {"error": str(e)}, 404

  @books.response(status_code=204)
  @authenticated
  def delete(self, isbn):
    return book_service.delete_one(isbn)

