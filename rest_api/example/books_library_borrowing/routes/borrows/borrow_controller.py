from flask_smorest import Blueprint

from .borrow_service import BorrowService

from routes.books.dto.response.book_response import BookResponse
from routes.books.book_mapper import BookMapper

from utils.decorators import authenticated

borrows = Blueprint("borrows", "borrows", url_prefix="/borrows", description="Borrows routes")
borrow_service = BorrowService()
book_mapper = BookMapper()

@borrows.route("/me")
@authenticated
@borrows.response(status_code=200, schema=BookResponse(many=True))
@borrows.response(status_code=401)
def my_borrows():
  return [book_mapper.to_dict(b) for b in borrow_service.get_my_borrows()]
  
