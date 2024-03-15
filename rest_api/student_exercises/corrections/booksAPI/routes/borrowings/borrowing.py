from datetime import datetime

class Borrowing():
  def __init__(self, book_isbn: str = "", start: datetime = None, end: datetime = None) -> None:
    self.book_isbn = book_isbn
    self.start = start if isinstance(start, datetime) else datetime.now()
    self.end = end if isinstance(end, datetime) else datetime.now()