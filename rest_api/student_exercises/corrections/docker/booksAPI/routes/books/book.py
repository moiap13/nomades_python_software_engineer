class Book():
  def __init__(self, isbn="", title="", summary="", authors=[]):
    self.isbn = isbn
    self.title = title
    self.summary = summary
    self.authors = authors

  def to_dict(self):
    print(self.authors)
    d = {
      "title": self.title,
      "summary": self.summary
    }

    if len(self.authors) > 0:
      d["authors"] = self.authors

    print(d)
    return d
  

  @staticmethod
  def from_dto(data):
    return Book(data["isbn"], data["title"], data["summary"], data.get("authors", []))
  
  def update(self, new_book):
    if new_book.title:
      self.title = new_book.title
    if new_book.summary:
      self.summary = new_book.summary
    return self
