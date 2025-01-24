def caesar_cipher(text: str, shift: int) -> str:
  """
  Encodes text using the Caesar cipher.

  Infos:
    caesar cipher: https://en.wikipedia.org/wiki/Caesar_cipher
    chr: https://docs.python.org/3/library/functions.html#chr
    ord: https://docs.python.org/3/library/functions.html#ord
  
  Examples:
    caesar_cipher("hello world", 3) -> "khoor zruog"
    caesar_cipher("hello world", 0) -> "hello world"
    caesar_cipher("hello world", 26) -> "hello world"

  Constraints:
    0 <= shift <= 26

  Assumptions:
    text is a string made of only lowercase letters ascci characters
    shift is an integer

  Args:
    text (str): The text to be encoded.
    shift (int): The number of characters to shift the text.

  Returns:
    str: The encoded text.
  """ 
  CHARSET_LEN = 26 # we assume here we only use ascii lowercase letters
  encoded = ""
  return encoded


print(caesar_cipher("hello worldz", 3))
print(caesar_cipher(caesar_cipher("hello world", 3), -3))
