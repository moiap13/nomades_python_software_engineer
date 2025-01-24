from vigenere import vigenere_encrypt, vigenere_decrypt

def main():
    """
    Terminal User Interface for Vigenère Cipher.
    """
    print("Welcome to the Vigenère Cipher Tool!")
    print("===================================")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")

    while True:
        try:
            choice = int(input("\nEnter your choice (1/2/3): "))
            if choice == 1:
                text = input("Enter the plaintext: ")
                key = input("Enter the encryption key: ")
                if not key.isalpha():
                    print("Error: The key must only contain alphabetic characters!")
                    continue
                encrypted = vigenere_encrypt(text, key)
                print(f"Encrypted text: {encrypted}")
            elif choice == 2:
                ciphertext = input("Enter the ciphertext: ")
                key = input("Enter the decryption key: ")
                if not key.isalpha():
                    print("Error: The key must only contain alphabetic characters!")
                    continue
                decrypted = vigenere_decrypt(ciphertext, key)
                print(f"Decrypted text: {decrypted}")
            elif choice == 3:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number (1/2/3).")


if __name__ == "__main__":
    main()