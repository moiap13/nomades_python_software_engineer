import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

# Library imports
from flask.views import MethodView
from flask_smorest import Blueprint

# root imports
from utils.decorators import authenticated

# current dir imports
from .borrowing_service import BorrowingService
from .borrowing_mapper import toResponse

# DTO imports
from .dto.request.borrow_request import BorrowRequest
from .dto.response.borrow_response import BorrowResponse

borrowings = Blueprint("borrowings", "borrowings", url_prefix="/borrowings", description="borrowings API")

borrow_service = BorrowingService()

@borrowings.route("/")
class BooksCollection(MethodView):
  @borrowings.response(status_code=200, schema=BorrowResponse(many=True))
  @authenticated
  def get(self):
    return [toResponse(b) for b in borrow_service.get_borrowed_books()]
    

  @borrowings.arguments(BorrowRequest)
  @borrowings.response(status_code=201, schema=BorrowResponse)
  @borrowings.response(status_code=422)
  @authenticated
  def post(self, borrow: dict):
    try:
      return toResponse(borrow_service.borrows(borrow["book_isbn"], borrow["nb_days"])), 201
    except Exception as e:
      return {"message": str(e)}, 422


@borrowings.route("/<string:book_isbn>", methods=["POST"])
@borrowings.response(status_code=200)
@authenticated
def returns(book_isbn: str):
  borrow_service.returns(book_isbn)
  return {}, 200