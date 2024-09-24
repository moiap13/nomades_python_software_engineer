"""
This is a hashed password that is generated using the SHA-256 algorithm.
You task is to find the password that was used to generate this hash.
For that you need to know some information about the password:
- It is an alphabetical string
- It is a lower case string
- It is a 5 letter string

The password to be found is hashed using the SHA-256 algorithm.
The SHA-256 algorithm is a hashing algorithm that takes a string as input and generates a 256 bit (32 byte) hash as output.
The hash is a hexadecimal string that is 64 characters long.
You can use the hashlib library to generate the hash of a string.
example:
    ```python
    password = hashlib.sha256("MyCurrentPassword".encode()).hexdigest()
    ```

Knowing that information, 
you can write a program that will generate all possible combinations of 5 letter strings. and try to break the password.
"""
import hashlib
import string
import time
from tqdm import tqdm 
import random

def brute_force_password(charset: str, length: int, target_hash: str) -> tuple[str | None, float]:
    MAX_ITER = len(charset) ** length
    start_time = time.time()

    # TODO: Implement the brute force algorithm

    # for a in charset:
    #     for b in charset:
    #         for c in charset:
    #             for d in charset:
    #                 for e in charset:
    #                     p = a+b+c+d+e
    #                     h_p: str = hashlib.sha256(p.encode()).hexdigest()
    #                     if h_p == target_hash:
    #                         # you found the password hourra
    #                         return p, time.time() - start_time

    lc = list(charset)
    random.shuffle(lc)
    charset = ''.join(lc)

    for x in tqdm(range(MAX_ITER)):
        p = ''
        for col in range(length-1, -1, -1): # col -> 4, 3, 2, 1, 0
            p += charset[(x // len(charset)**col) % len(charset)]
        
        h_p: str = hashlib.sha256(p.encode()).hexdigest()
        if h_p == target_hash:
            # you found the password hourra
            return p, time.time() - start_time 
            
    return None, time.time() - start_time

# Example usage:
charset: str = string.ascii_lowercase  # Define your character set
length: int = 5  # Define the length of the password
target_hash: str = "d0bc381952d0827f36467818a9560eb5eb6fda8a64a422aa21fcda3f2263e8b4"
target_hash: str = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"

password, time_taken = brute_force_password(charset, length, target_hash)

if password:
    print("Password:", password)
else:
    print("Password not found.")
    
print("Time taken:", time_taken)

"""
Questions Part
1. What is the time complexity of the brute force algorithm?
  len(charset)**length -> 26**5 -> 11'881'376


2. What would be the time complexity if the password was 6 characters long instead of 5?
  26**6 = 308'915'776

3. What would be the value of MAX_ITER if the password contains uppercase letters, lowercase letters, digits and special characters?
  95**5 = 7'737'809'375

4. Imagine you have a computer that clock a 4GHZ (4 billion cycles per second). 
  Complete the table below with the time taken to break the password for different lengths of passwords.
  ```
  | population/length | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
  |-------------------|---|---|---|---|---|----|----|----|----|----|
  | lower_case (26)   | | | | | | | | | | |
  | upper_case (26)   | | | | | | | | | | |
  | digits (10)       | | | | | | | | | | |
  | special (32)      | | | | | | | | | | |
  | alpha_lower_upper (52) | | | | | | | | | | |
  | alphanumeric (62) | | | | | | | | | | |
  | all_characters (95) | | | | | | | | | | |
  ```
"""
