class TodoNotFound(Exception):
  def __init__(self, message):
    super().__init__(message)

class TodoEmpty(Exception):
  def __init__(self, message):
    super().__init__(message) 