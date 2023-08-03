def compteMots(phrase):
    count = 0
    phrase = phrase.strip()
    for char in phrase:
        if char == " ":
            count += 1
    return count + 1


def inverser(mot):
    reverse = ""
    for i in range(len(mot) - 1, -1, -1):
        reverse += mot[i]
    return reverse


def estPalindrome(mot):
    return inverser(mot) == mot


def compteCaracteres(mot):
    count = 0
    for char in mot:
        count += 1
    return count


def compterLesLettres(mot):
    count = 0
    for char in mot:
        # if char is not empty and not a digit
        if char != " " and not char.isdigit():
            count += 1
    return count


def compteVoyelles(mot):
    voyelles = ["a", "e", "i", "o", "u", "y"]
    count = 0
    for char in mot:
        if char.lower() in voyelles:
            count += 1
    return count


def compteConsonnes(mot):
    voyelles = ["a", "e", "i", "o", "u", "y"]
    count = 0
    for char in mot:
        if char.lower() not in voyelles and char != " ":
            count += 1
    return count


def concatenation(mot1, mot2):
    return mot1 + mot2
