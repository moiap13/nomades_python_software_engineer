def sum(tableau: list[int]) -> int:
    """
    Function that returns the sum of the elements of the array
    :param tableau: the array to sum
    :return: the sum of the elements of the array
    """
    total = 0
    for element in tableau:
      total += element
    return total



def average(tableau: list[int]) -> float:
    """
    Function that returns the average of the elements of the array
    :param tableau: the array to average
    :return: the average of the elements of the array
    """
    # total = 0
    # for element in tableau:
    #   total += element
    # return total/len(tableau)
    return sum(tableau) / len(tableau) 


def min(tableau: list[int]) -> int:
    """
    Function that returns the minimum of the elements of the array
    :param tableau: the array to find the minimum of
    :return: the minimum of the elements of the array
    """
    current_min = tableau[0]
    for elem in tableau[1:]:
        if current_min > elem:
            current_min=elem 
    return current_min

def max(tableau: list[int]) -> int:
    """
    Function that returns the maximum of the elements of the array
    :param tableau: the array to find the maximum of
    :return: the maximum of the elements of the array
    """
    current_max = tableau[0]
    for elem in tableau[1:]:
        if current_max < elem:
            current_max = elem 
    return current_max


def min_max(tableau: list[int]) -> tuple[int, int]:
    """
    Function that returns the minimum and maximum of the elements of the array
    :param tableau: the array to find the minimum and maximum of
    :return: the minimum and maximum of the elements of the array
    """
    # current_min = tableau[0]
    # current_max = tableau[0]
    # for elem in tableau[1:]:
    #     if current_min > elem:
    #         current_min = elem 
    #     elif current_max < elem:
    #         current_max =elem 
    # return current_min, current_max
    return (min(tableau), max(tableau))

def mode(tableau: list[int]) -> int:
    """
    Function that returns the mode of the elements of the array
    The mode is the value that appears most often in a set of data values.
    If there is a tie, the mode is the smallest value.
    :param tableau: the array to find the mode of
    :return: the mode of the elements of the array
    """
    return None

def variance(tableau: list[int]) -> float: # O(n)
    """
    Function that returns the variance of the elements of the array
    :param tableau: the array to find the variance of
    :return: the variance of the elements of the array
    """
    if tableau != []:
        # squared_diffs = [(x - mean) ** 2 for x in tableau]
        # variance_value = sum(squared_diffs) / len(tableau)
        mean = average(tableau)     # O(n)
        total = 0                   # O(1)
        for elem in tableau:        # O(n)
            total += (elem-mean)**2   # O(1)
        return total / len(tableau) # O(1)


def standard_deviation(tableau: list[int]) -> float:
    """
    Function that returns the standard deviation of the elements of the array
    The standard deviation is the square root of the variance.
    
    :param tableau: the array to find the standard deviation of
    
    :return: the standard deviation of the elements of the array
    """
    # import math
    # return math.sqrt(variance)
    return variance(tableau) ** (1/2)


def exist(tableau: list[int], valeur: int) -> bool:
    """
    Function that returns True if the value exists in the array
    :param tableau: the array to check if the value exists in
    :param valeur: the value to check if it exists in the array
    :return: True if the value exists in the array, False otherwise
    """
    return valeur in tableau


def position(tableau: list[int], valeur: int) -> int:
    """
    Function that returns the position of the first value in the array
    If the value does not exist in the array, it returns -1
    :param tableau: the array to find the position of
    :param valeur: the value to find the position of
    :return: the position of the value in the array
    """
    # for index in range(0,len(tableau)):
    #     if valeur == tableau[index]:
    #         return index
    # return -1 

    for index, value in enumerate(tableau):
        if valeur == value:
            return index
    return -1

def similars(arr1: list[int], arr2: list[int]) -> bool:
    """
    Function that returns True if the two arrays are similar
    :param arr1: the first array
    :param arr2: the second array
    :return: True if the two arrays are similar, False otherwise
    """
    #return arr1 == arr2
    if len(arr1) != len(arr2):
        return False
    
    assert len(arr1) == len(arr2), "Arrays must have the same size"

    for index in range(len(arr1)):
        if arr1[index] != arr2[index]:
            return False
    return True
            
            

def is_list(tableau) -> bool:
    """
    Function that returns True if the array is a table
    :param tableau: the array to check if it is a table
    :return: True if the array is a table, False otherwise
    """
    return type(tableau) == list


def is_list_of_numbers(tableau) -> bool:
    """
    Function that returns True if the array is a table of numbers
    :param tableau: the array to check if it is a table of numbers
    :return: True if the array is a table of numbers, False otherwise
    """
    if type(tableau) != list or len(tableau) == 0:
        return False

    for value in tableau:
        if type(value) != int:
            return False
    return True

def sort_ascending(arr: list[int]) -> list[int]:
    """
    Function that returns the sorted array in ascending order 
    :param arr: the array to sort
    :return: the sorted array in ascending order
    """
    list_sort=[]
    for _ in range(0,len(arr)):
        mini=arr[0]
        for z in arr[1:]:
            if z < mini:
                mini=z
        arr.remove(mini)
        list_sort.append(mini)

    return list_sort


def sort_descending(arr: list[int]) -> list[int]:
    """
    Function that returns the sorted array in descending order 
    :param arr: the array to sort
    :return: the sorted array in descending order
    """
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def median(tableau: list[int]) -> int:
    """
    Function that returns the median of the elements of the array
    :param tableau: the array to find the median of
    :return: the median of the elements of the array
    """

    tableau = sort_ascending(tableau)
    mid = len(tableau) // 2
    return tableau[mid] if len(tableau) % 2 == 1 else (tableau[mid] + tableau[mid-1]) / 2

    if len(tableau) % 2 == 0:
        return (tableau[int(len(tableau) / 2)] + tableau[len(tableau) // 2 -1]) / 2
    else:
        return tableau[len(tableau) // 2]