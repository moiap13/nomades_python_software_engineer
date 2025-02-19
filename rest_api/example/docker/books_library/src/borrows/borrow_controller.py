import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from flask_smorest import Blueprint
from flask import g

from src._helpers.decorators import authenticated
from src.books.book import Book
from src.users.user import User

from .dto.response.borrow_response import BorrowResponse
from .dto.request.borrow_request import BorrowRequest
from .borrow_service import BorrowService
from .borrow import Borrow

borrows_bp = Blueprint("borrows", "borrows", url_prefix="/borrows", description="Routes to borrow a book")

borrows_service = BorrowService()


@borrows_bp.route("/my")
@authenticated
@borrows_bp.response(status_code=200, schema=BorrowResponse(many=True))
def get_my_borrows():
    return borrows_service.get_borrows_per_user(g.user_id)

@borrows_bp.route("/borrow", methods=["POST"])
@authenticated
@borrows_bp.arguments(BorrowRequest)
@borrows_bp.response(status_code=200, schema=BorrowResponse)
def add_borrow(borrow_request: dict):
    print(borrow_request)
    borrow = Borrow(
        id="",
        user=User(
            id=g.user_id
        ),
        book=Book(
            id=borrow_request["book_id"]
        ),
        start=borrow_request["start"],
        end=borrow_request["end"]
    )
    return borrows_service.borrow(borrow)