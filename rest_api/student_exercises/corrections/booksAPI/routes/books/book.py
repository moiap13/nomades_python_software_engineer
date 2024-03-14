class Book():
  def __init__(self, isbn="", title="", summary=""):
    self.isbn = isbn
    self.title = title
    self.summary = summary

  def to_dict(self):
    return {
      "title": self.title,
      "summary": self.summary
    }

  @staticmethod
  def from_dto(data):
    return Book(data["isbn"], data["title"], data["summary"])
  
  def update(self, new_book):
    if new_book.title:
      self.title = new_book.title
    if new_book.summary:
      self.summary = new_book.summary
    return self
