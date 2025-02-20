class Book:
  def __init__(self, id:str = "", title:str = "", isbn:str = "", authors:list[str] = []):
    self.id = id
    self.title = title
    self.isbn = isbn
    self.authors = authors

  def __str__(self) -> str:
    return f"Book({self.id}, {self.isbn}, {self.title})"