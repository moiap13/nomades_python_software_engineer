class Book():
  def __init__(self, isbn="", title="", summary=""):
    self.isbn = isbn
    self.title = title
    self.summary = summary

  def to_dict(self):
    return {
      "isbn": self.isbn,
      "title": self.title,
      "summary": self.summary
    }

  @staticmethod
  def from_dto(data):
    return Book(data["isbn"], data["title"], data["summary"])
