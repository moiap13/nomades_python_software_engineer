import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import unittest

from src.books.book import Book

class TestUser(unittest.TestCase):
  def test_user_create_empty(self):
    b = Book()
    self.assertEqual(b.id, "")
    self.assertEqual(b.title, "")
    self.assertEqual(b.authors, [])
    self.assertEqual(b.isbn, "")
  
if __name__ == "__main__":
  unittest.main()
