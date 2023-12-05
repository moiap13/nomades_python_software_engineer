def sum(tableau: list[int]) -> int:
    """
    Function that returns the sum of the elements of the array
    :param tableau: the array to sum
    :return: the sum of the elements of the array
    """
    total = 0
    for curr_i in tableau:
        total += curr_i
    return total


def average(tableau: list[int]) -> float:
    """
    Function that returns the average of the elements of the array
    :param tableau: the array to average
    :return: the average of the elements of the array
    """
    # total = 0
    # for curr_i in tableau:
    #     total += curr_i
    #     avg = total / len(tableau)
    # return avg
    return sum(tableau) / len(tableau)


def min(tableau: list[int]) -> int:
    import math
    """
    Function that returns the minimum of the elements of the array
    :param tableau: the array to find the minimum of
    :return: the minimum of the elements of the array
    """
    if len(tableau) == 0:
        return -math.inf
        
    minimum = tableau[0]
    # for i in range(1, len(tableau)):
    #     if minimum > tableau[i]:
    #         minimum = tableau[i]
    for curr_i in tableau[1:]:
        if minimum > curr_i:
            minimum = curr_i
    return minimum

def max(tableau: list[int]) -> int:
    import math
    """
    Function that returns the maximum of the elements of the array
    :param tableau: the array to find the maximum of
    :return: the maximum of the elements of the array
    """
    if len(tableau) == 0:
        return math.inf
        
    maximum = tableau[0]
    # for i in range(1, len(tableau)):
    #     if minimum > tableau[i]:
    #         minimum = tableau[i]
    for curr_i in tableau[1:]:
        if maximum < curr_i:
            maximum = curr_i
    return maximum


def min_max(tableau: list[int]) -> list[int, int]:
    """
    Function that returns the minimum and maximum of the elements of the array
    :param tableau: the array to find the minimum and maximum of
    :return: the minimum and maximum of the elements of the array
    """
    return [min(tableau), max(tableau)]


def mode(tableau: list[int]) -> int:
    """
    Function that returns the mode of the elements of the array
    The mode is the value that appears most often in a set of data values.
    If there is a tie, the mode is the smallest value.
    :param tableau: the array to find the mode of
    :return: the mode of the elements of the array1
    """
    return None

def variance(tableau: list[int]) -> float:
    """
    Function that returns the variance of the elements of the array
    :param tableau: the array to find the variance of
    :return: the variance of the elements of the array
    """
    var = 0
    avg = average(tableau)
    for i in range(len(tableau)):
        var += (tableau[i] - avg)**2/len(tableau)
    return var


def standard_deviation(tableau: list[int]) -> float:
    import math
    """
    Function that returns the standard deviation of the elements of the array
    The standard deviation is the square root of the variance.
    :param tableau: the array to find the standard deviation of
    :return: the standard deviation of the elements of the array
    """
    return math.sqrt(variance(tableau))


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
    for i, v in enumerate(tableau):
        if v == valeur:
            return i
    return -1


def similars(arr1: list[int], arr2: list[int]) -> bool:
    """
    Function that returns True if the two arrays are similar
    :param arr1: the first array
    :param arr2: the second array
    :return: True if the two arrays are similar, False otherwise
    """
    if len(arr1) != len(arr2):
        return False

    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True


def is_list(tableau: any) -> bool:
    """
    Function that returns True if the array is a table
    :param tableau: the array to check if it is a table
    :return: True if the array is a table, False otherwise
    """
    return type(tableau) == list


def is_list_of_numbers(tableau:list[any]) -> bool:
    """
    Function that returns True if the array is a table of numbers
    :param tableau: the array to check if it is a table of numbers
    :return: True if the array is a table of numbers, False otherwise
    """
    if not is_list(tableau) or len(tableau) == 0:
        return False
    
    for curr_element in tableau:
        if not isinstance(curr_element, int):
            return False
    return True

def sort_ascending(arr: list[int]) -> list[int]:
    """
    Function that returns the sorted array in ascending order 
    :param arr: the array to sort
    :return: the sorted array in ascending order
    """
    asc = arr.copy()
    for i in range(len(arr)):
        local_min = min(arr[i:])
        pos = position(asc, local_min)
        asc[i], arr[i] = arr[pos], asc[i]
    return asc


def sort_descending(arr: list[int]) -> list[int]:
    """
    Function that returns the sorted array in descending order 
    :param arr: the array to sort
    :return: the sorted array in descending order
    """
    return sort_ascending(arr)[::-1]

def median(tableau: list[int]) -> int:
    """
    Function that returns the median of the elements of the array
    :param tableau: the array to find the median of
    :return: the median of the elements of the array
    """
    med = sort_ascending(tableau)
    if len(med) % 2 == 1:
        return med[len(med)//2]
    
    mid_point = len(med)//2-1
    return average(med[mid_point:mid_point+2])
