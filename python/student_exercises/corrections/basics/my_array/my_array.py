def sum(tableau: list[int]) -> int:
    """
    Function that returns the sum of the elements of the array
    :param tableau: the array to sum
    :return: the sum of the elements of the array
    """
    total = 0
    for curr_elem in tableau:
        total += curr_elem
    return total


def average(tableau: list[int]) -> float:
    """
    Function that returns the average of the elements of the array
    :param tableau: the array to average
    :return: the average of the elements of the array
    """
    total = 0
    for curr_elem in tableau:
        total += curr_elem
    return total / len(tableau)
    # return sum(tableau) / len(tableau)


def min(tableau: list[int]) -> int:
    """
    [10,3,5,2]
    Function that returns the minimum of the elements of the array
    :param tableau: the array to find the minimum of
    :return: the minimum of the elements of the array
    """
    # curr_min = 10e10 # math.inf
    # curr_min = tableau[0]
    # for curr_elem in tableau:
    #     if curr_elem < curr_min:
    #         curr_min = curr_elem
    # return curr_min
    # curr_min = tableau[0]
    # for i in range(1, len(tableau)):
    #     if tableau[i] < curr_min:
    #         curr_min = tableau[i]
    # return curr_min
    curr_min = tableau[0]
    for curr_elem in tableau[1:]:
        if curr_elem < curr_min:
            curr_min = curr_elem
    return curr_min
        



def max(tableau: list[int]) -> int:
    """
    Function that returns the maximum of the elements of the array
    :param tableau: the array to find the maximum of
    :return: the maximum of the elements of the array
    """    
    curr_min = tableau[0]
    for curr_elem in tableau[1:]:
        if curr_elem > curr_min:
            curr_min = curr_elem
    return curr_min
        


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
    :return: the mode of the elements of the array
    """
    # counter = 0
    # mode = [0]
    # new_tab = sorted(tableau)

    # for curr_elem in (new_tab):
    #     curr_freq = new_tab.count[curr_elem]
    #     if curr_freq > counter:
    #         counter = curr_freq
    #         mode = curr_elem
    # return mode 
    occurences = {}
    for item in tableau:
      if item not in occurences:
        occurences[item] = 0
      occurences[item] += 1
    
    max_occurences: int = max(list(occurences.values()))
    mode = []
    for k, v in occurences.items():
      if v == max_occurences:
        mode.append(k)
    
    return min(mode)
        
def variance(tableau: list[int]) -> float: # O(n) | O(n^2)
    """
    Function that returns the variance of the elements of the array
    :param tableau: the array to find the variance of
    :return: the variance of the elements of the array
    """
    # avg = average(tableau)
    # v = 0                                     
    # for curr_elem in tableau:                 
    #    v += (curr_elem-avg)**2 
    # return v/len(tableau)
    from functools import reduce
    avg = average(tableau)
    return reduce(lambda a, b: a + (b-avg)**2, tableau, 0)/len(tableau)

def standard_deviation(tableau: list[int]) -> float:
    """
    Function that returns the standard deviation of the elements of the array
    The standard deviation is the square root of the variance.
    :param tableau: the array to find the standard deviation of
    :return: the standard deviation of the elements of the array
    """
    return variance(tableau)**(1/2)

def exist(tableau: list[int], valeur: int) -> bool:
    """
    Function that returns True if the value exists in the array
    :param tableau: the array to check if the value exists in
    :param valeur: the value to check if it exists in the array
    :return: True if the value exists in the array, False otherwise
    """
    for i in tableau:
        if valeur == i:
            return True
    return False
    # return valeur in tableau


def position(tableau: list[int], valeur: int) -> int:
    """
    Function that returns the position of the first value in the array
    If the value does not exist in the array, it returns -1
    :param tableau: the array to find the position of
    :param valeur: the value to find the position of
    :return: the position of the value in the array
    """
    for i in range(len(tableau)):
        curr_elem = tableau[i]
        if curr_elem == valeur:
            return i
    return -1


def similars(arr1: list[int], arr2: list[int]) -> bool:
    """
    Function that returns True if the two arrays are similar
    :param arr1: the first array
    :param arr2: the second array
    :return: True if the two arrays are similar, False otherwise
    """
    if len(arr1) != len(arr2): return False

    for i in range(len(arr1)):
      if arr1[i] != arr2[i]:
        return False
    return True


def is_list(tableau) -> bool:
    """
    Function that returns True if the array is a table
    :param tableau: the array to check if it is a table
    :return: True if the array is a table, False otherwise
    """
    return type(tableau) is list


def is_list_of_numbers(tableau) -> bool:
    """
    Function that returns True if the array is a table of numbers
    :param tableau: the array to check if it is a table of numbers
    :return: True if the array is a table of numbers, False otherwise
    """
    if not is_list(tableau): return False
    if len(tableau) == 0: return False

    for i in tableau:
      if type(i) != int:
        return False
    return True

def sort_ascending(arr: list[int]) -> list[int]: # O(n^2) | O(n*log(n))
    """
    Function that returns the sorted array in ascending order 
    :param arr: the array to sort
    :return: the sorted array in ascending order
    """
    for i in range(len(arr)):             # O(n)
      for j in range(i+1, len(arr)):      # O(n*n)
        if arr[i] >= arr[j]:
          arr[j], arr[i] = arr[i], arr[j]
    return arr


def sort_descending(arr: list[int]) -> list[int]:
    """
    Function that returns the sorted array in descending order 
    :param arr: the array to sort
    :return: the sorted array in descending order
    """
    for i in range(len(arr)):             # O(n)
      for j in range(i+1, len(arr)):      # O(n*n)
        if arr[i] <= arr[j]:
          arr[j], arr[i] = arr[i], arr[j]
    return arr

def median(tableau: list[int]) -> int:
    """
    Function that returns the median of the elements of the array
    :param tableau: the array to find the median of
    :return: the median of the elements of the array
    """
    tableau = sort_ascending(tableau)
    return tableau[len(tableau)//2] if len(tableau)%2==1 else (tableau[len(tableau)//2]+tableau[len(tableau)//2-1])/2
