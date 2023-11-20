import random
import string

def generate_random_password(length=12):
    # Define the character sets to build the password
    if length < 8:
        raise ValueError
    
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    all_chars = lowercase_letters + uppercase_letters + digits + special_chars

    password =  random.sample(lowercase_letters, 1) +\
                random.sample(uppercase_letters, 1) +\
                random.sample(digits, 1) +\
                random.sample(special_chars, 1) +\
                random.sample(all_chars, length-4)
    
    random.shuffle(password)
    return "".join(password)

    # Georgios Code
    # p = [random.choice(lowercase_letters) + random.choice(uppercase_letters) + random.choice(digits) + random.choice(special_chars)]
    # p = list(p)
    # #random.shuffle(p)
    # password = "".join(p)
    
    # i = 4
    # while i < length:
    #     r0 = random.choice(lowercase_letters)
    #     r1 = random.choice(uppercase_letters)
    #     r2 = random.choice(digits)
    #     r3 = random.choice(special_chars)
    #     password += "".join(random.sample(r0 + r1 + r2 + r3, 1))
    #     i += 1

    # random.shuffle(list(password))
    # return password



    # Homan code
    # all_chars = [lowercase_letters, uppercase_letters, digits, special_chars]

    # p = ""
    # for _ in range(length):
    #     random_list = random.choice(all_chars)
    #     char = random.choice(random_list)
    #     p += char

    # return p


password = generate_random_password()
print("Random Password:", password)





# Elena code
# def generate_random_password(length=12):
#     # Define the character sets to build the password
#     if length < 8:
#         return("Number of symbols need to be at least 8")
    
#     lowercase_letters = string.ascii_lowercase
#     uppercase_letters = string.ascii_uppercase
#     digits = string.digits
#     special_chars = string.punctuation
#     #
#     result_string = str()
#     l_symbol_type = ["L", "U", "N", "S"]
#     l_pass_stat = [0, 0, 0, 0]
#     #
#     def statistics(symbol_type, pass_stat: list[int]) -> list[int]:
#         if symbol_type == "L":
#             l_pass_stat[0] += 1
#         elif symbol_type == "U":
#             l_pass_stat[1] += 1
#         elif symbol_type == "N":
#             l_pass_stat[2] += 1
#         elif symbol_type == "S":
#             l_pass_stat[3] += 1
#         return l_pass_stat
#     #
#     def generated_symbol(cur_symbol_type: str) -> str:
#         if cur_symbol_type == "L":
#             return random.choice(lowercase_letters)
#         elif cur_symbol_type == "U":
#             return random.choice(uppercase_letters)
#         elif cur_symbol_type == "N":
#             return random.choice(digits)
#         return random.choice(special_chars)
#     # main part
#     for i in range (0, length):  
#       cur_symbol_type = random.choice(l_symbol_type)
#       cur_symbol = generated_symbol(cur_symbol_type)
#       result_string = result_string + cur_symbol
#       statistics(cur_symbol_type, l_pass_stat)
#       l_symbol_type.remove(cur_symbol_type)
#       if len(l_symbol_type) == 0:
#           l_symbol_type = ["L", "U", "N", "S"]
#     print(l_pass_stat)
#     return result_string