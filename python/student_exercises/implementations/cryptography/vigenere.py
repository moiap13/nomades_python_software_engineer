def vigenere_encrypt(text: str, key: str) -> str:
    """
    Encrypts text using the Vigenère cipher.

    Infos:
      Vigenère cipher: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
      chr: https://docs.python.org/3/library/functions.html#chr
      ord: https://docs.python.org/3/library/functions.html#ord
    
    Examples:
      vigenere_encrypt("hello world", "key") -> "RIJVS UYVJN"
      vigenere_encrypt("attack at dawn", "lemon") -> "LXFOPV EF RNHR"
      vigenere_encrypt("123 hello!", "abc") -> "123 HFNLP!"

    Constraints:
      key must only contain alphabetic characters (a-z, A-Z).
      text may contain any characters.

    Assumptions:
      - text is a string.
      - key is a string containing only alphabetic characters.
      - The function is case-insensitive, converting both text and key to uppercase.

    Args:
      text (str): The plaintext to encrypt.
      key (str): The encryption key.

    Returns:
      str: The encrypted text.
    """
    return None


def vigenere_decrypt(ciphertext: str, key: str) -> str:
    """
    Decrypts text encrypted using the Vigenère cipher.

    Infos:
      Vigenère cipher: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
      chr: https://docs.python.org/3/library/functions.html#chr
      ord: https://docs.python.org/3/library/functions.html#ord
    
    Examples:
      vigenere_decrypt("RIJVS UYVJN", "key") -> "HELLO WORLD"
      vigenere_decrypt("LXFOPV EF RNHR", "lemon") -> "ATTACK AT DAWN"
      vigenere_decrypt("123 HFNLP!", "abc") -> "123 HELLO!"

    Constraints:
      key must only contain alphabetic characters (a-z, A-Z).
      ciphertext may contain any characters.

    Assumptions:
      - ciphertext is a string.
      - key is a string containing only alphabetic characters.
      - The function is case-insensitive, converting both ciphertext and key to uppercase.

    Args:
      ciphertext (str): The encrypted text to decrypt.
      key (str): The decryption key.

    Returns:
      str: The decrypted plaintext.
    """
    return None


# Example usage
if __name__ == "__main__":
    plaintext = "hello world"
    key = "key"
    encrypted = vigenere_encrypt(plaintext, key)
    decrypted = vigenere_decrypt(encrypted, key)

    print("Plaintext:", plaintext)
    print("Key:", key)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)