def tri_croissant(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
            


def tri_decroissant(arr):
  for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
        if arr[j] < arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr

def somme(tableau):
    sum = 0
    for i in tableau:
        sum += i
    return sum

def moyenne(tableau):
    return somme(tableau) / len(tableau)


def min(tableau):
    m = tableau[0]
    for x in tableau:
        if x < m:
            m = x
    
    return m
        

def max(tableau):
    m = tableau[0]
    for x in tableau:
        if x > m:
            m = x
    
    return m


def min_max(tableau):
    return None


def mediane(tableau):
    return None


def mode(tableau):
    return None


def ecart_type(tableau):
    return None


def existe(tableau, valeur):
    return None


def position(tableau, valeur):
    return None


def similaires(arr1, arr2):
    return None


def est_tableau(tableau):
    return None


def est_tableau_de_nombres(tableau):
    return None
