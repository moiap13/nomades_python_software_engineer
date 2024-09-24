from flask.views import MethodView
from flask_smorest import Blueprint

from .book import Book

from .dto.request.create_book import CreateBookRequest
from .dto.request.update_book import UpdateBookRequest
from .dto.response.book_response import BookId, BookISBN, BookResponse, BookResponseList

from .book_service import BookService
from .book_mapper import BookMapper

books = Blueprint("books", "books", url_prefix="/books", description="Books routes")

book_service = BookService()
book_mapper = BookMapper()

@books.route("/")
class BookController(MethodView):
    @books.doc(description="Retrieve a list of all the books of the system")
    @books.response(status_code=200, schema=BookResponseList(many=True), description="Return the list of all the books")
    def get(self):
        # Get all books
        return book_service.get_all()
    
    @books.arguments(CreateBookRequest)
    @books.response(status_code=200, schema=BookResponse)
    @books.response(status_code=422)
    @books.doc(description="Create a book in the system")
    def post(self, book: dict):
        try:
            return book_service.create_book(book_mapper.to_book(book))
        except ValueError as e:
            return {"message": str(e)}, 422
        
@books.route("/<book_id>")
class BookRetrieveController(MethodView):
    @books.doc(description="Get a book by firebase ID")
    @books.response(status_code=200, schema=BookResponse, description="Return specific book by ID")
    @books.response(status_code=404)
    def get(self, book_id: str):
        # Get book by ID
        try:
          return book_mapper.to_dict(book_service.get_one(book_id))
        except ValueError as e:
          return {"message": str(e)}, 404

    @books.doc(description="Update a book by ID")
    @books.arguments(UpdateBookRequest)
    @books.response(status_code=200, schema=BookResponse)
    @books.response(status_code=404)
    def put(self, book: dict, book_id: str):
        # Update book by ID
        try:
          return book_mapper.to_dict(book_service.update_book(book_mapper.to_book(book), book_id))
        except ValueError as e:
          return {"message": str(e)}, 404

    @books.doc(description="Delete a book by ID")
    @books.response(status_code=204)
    def delete(self, book_id: str):
        # Delete book by ID
        return book_service.delete_one(book_id)

@books.route("/isbn/<isbn>")
class BookRetrieveController(MethodView):
    @books.doc(description="Get a book by ISBN")
    @books.response(status_code=200, schema=BookResponse, description="Return specific book by ISBN")
    def get(self, isbn):
        # Get book by ID
        return book_mapper.to_dict(book_service.get_book_by_isbn(isbn))