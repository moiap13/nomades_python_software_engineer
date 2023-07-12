def estPair(nombre): # O(1)
    # if nombre%2:
    #     return "Le nombre est impair"
    
    # return "Le nombre est pair"
    return "Le nombre est impair" if nombre%2 else "Le nombre est pair"

def factorielle(n):
    resultat = 1
    for i in range(1,n+1):
      resultat *= i
    return resultat  

def fibonacci(n):
    return None

def somme(n): # O(n) -> O(1)
    # total = 0
    # for i in range (1, n+1):
    #     total +=i
    # return total
    return (n*(n+1))//2

def auCarre(n): # O(1)
    return n*n 

def est_premier(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 1/2) + 1):
        if n % i == 0:
            return False
    
    return True
