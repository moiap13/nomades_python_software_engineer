from flask.views import MethodView
from flask_smorest import Blueprint

from .dto.response.book_response import BookResponse
from .dto.request.create_book import CreateBook

from .book_service import BookService

books = Blueprint("books", "books", url_prefix="/books", description="Books API")

book_service = BookService()

@books.route("/")
class BooksCollection(MethodView):
  @books.response(status_code=200, schema=BookResponse(many=True))
  def get(self):
    return book_service.get_all() 

  @books.arguments(CreateBook)
  @books.response(status_code=201, schema=BookResponse)
  def post(self, book):
    return book_service.create_new_book(book)
  
@books.route("/<isbn>") # /books/{isbn} | I suggest you to avoid using spaces in isbn
class BookItem(MethodView):
  # TODO implement book item endpoint and logic
  # Don't forget to work with DTO
  # all the interractions with the database should be done using the book_repository class
  # all the logic about book item should be done inside the book_service
  def get():
    pass

  def put():
    pass

  def delete():
    pass


