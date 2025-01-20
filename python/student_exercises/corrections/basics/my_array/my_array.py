def sum(tableau: list[int]) -> int:
    """
    Function that returns the sum of the elements of the array
    :param tableau: the array to sum
    :return: the sum of the elements of the array
    """
    total: int = 0
    for number in tableau:
        total += number
    return total


def average(tableau: list[int]) -> float: # O(n)
    """ 
    Function that returns the average of the elements of the array
    :param tableau: the array to average
    :return: the average of the elements of the array
    """
    # avg: float = 0.0
    # total: int = 0
    # for i in range(len(tableau)):
    #     total += tableau[i]
    #     i+=1
    # avg = total / i
    # return avg

    return sum(tableau) / len(tableau)


def min(tableau: list[int]) -> int:
    """
    Function that returns the minimum of the elements of the array
    :param tableau: the array to find the minimum of
    :return: the minimum of the elements of the array
    """
    # min: int = 10e100
    # for n in tableau:
    #     if n < min:
    #         min = n
    # return min
    min: int = tableau[0]
    # for i in range(1, len(tableau)):
    #     if tableau[i] < min:
    #         min = tableau[i]
    for number in tableau[1:]:
      if number < min:
          min = number
    return min



def max(tableau: list[int]) -> int:
    """
    Function that returns the maximum of the elements of the array
    :param tableau: the array to find the maximum of
    :return: the maximum of the elements of the array
    """
    max: int = tableau[0]
    for i in range(1, len(tableau)):
        if tableau[i] > max:
            max = tableau[i]
    return max


def min_max(tableau: list[int]) -> tuple[int, int]: # O(n)
    """
    Function that returns the minimum and maximum of the elements of the array
    :param tableau: the array to find the minimum and maximum of
    :return: the minimum and maximum of the elements of the array
    """
    return (min(tableau), max(tableau)) # -> O(n)
    # min_ = max_ = tableau[0] 
    # for i in range(1, len(tableau)):
    #     curr_elem = tableau[i]
    #     if curr_elem < min_:
    #         min_ = curr_elem
    #     elif curr_elem > max_:
    #         max_ = curr_elem
    # return (min_, max_)


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
    x_bar: float = average(tableau) # O(n)
    total: float = 0.0              # O(1)
    for xi in tableau:              # O(n)
        total += (xi-x_bar)**2        # O(1)
    return total / len(tableau)     # O(1)


    # var_value: float = sum([(x- avg)**2 for x in tableau])
    # return var_value / len(tableau)

def standard_deviation(tableau: list[int]) -> float:
    """
    Function that returns the standard deviation of the elements of the array
    The standard deviation is the square root of the variance.
    :param tableau: the array to find the standard deviation of
    :return: the standard deviation of the elements of the array
    """
    # import math
    # return math.sqrt(variance(tableau))
    return variance(tableau)**(1/2)


def exist(tableau: list[int], valeur: int) -> bool:
    """
    Function that returns True if the value exists in the array
    :param tableau: the array to check if the value exists in
    :param valeur: the value to check if it exists in the array
    :return: True if the value exists in the array, False otherwise
    """
    # return valeur in tableau # O(n)
    for item in tableau:
        if item == valeur:
            return True
    return False
    


def position(tableau: list[int], valeur: int) -> int:
    """
    Function that returns the position of the first value in the array
    If the value does not exist in the array, it returns -1
    :param tableau: the array to find the position of
    :param valeur: the value to find the position of
    :return: the position of the value in the array
    """
    # for i in range(len(tableau)):
    #     if tableau[i] == valeur:
    #         return i
    # return -1
    for idx, val in enumerate(tableau):
        if val == valeur:
            return idx
    return -1
    # ind: int = [i for i, x in enumerate(tableau) if x == valeur]
    # if ind == []:
    #     ind = -1
    # else:
    #     ind = ind[0]
    # return ind



def similars(arr1: list[int], arr2: list[int]) -> bool:
    """
    Function that returns True if the two arrays are similar
    :param arr1: the first array
    :param arr2: the second array
    :return: True if the two arrays are similar, False otherwise
    """
    if len(arr1) != len(arr2):
        return False
    
    assert len(arr1) == len(arr2)
    index_arr = 0

    while(index_arr < len(arr1)):
        if arr1[index_arr] != arr2[index_arr]:
            return False
        index_arr += 1
    return True

    # index_arr1 = index_arr2 = 0
    # while(index_arr1 < len(arr1)):
    #     while(index_arr2 < len(arr2)):
    #         if arr1[index_arr1] != arr2[index_arr2]:
    #             return False
    #         index_arr1 += 1
    #         index_arr2 += 1
    # return True

    # return arr1 == arr2




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
    if not is_list(tableau) or len(tableau) == 0:
        return False
    
    for item in tableau:
        if type(item) != int:
            return False
    return True


def sort_ascending(arr: list[int]) -> list[int]:
    """
    Function that returns the sorted array in ascending order 
    python sort, O(n*log(n))
    :param arr: the array to sort
    :return: the sorted array in ascending order
    """
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                # tmp: int = arr[i]
                # arr[i] = arr[j]
                # arr[j] = tmp
                arr[i], arr[j] = (arr[j], arr[i])
    return arr


def sort_descending(arr: list[int]) -> list[int]:
    """
    Function that returns the sorted array in descending order 
    :param arr: the array to sort
    :return: the sorted array in descending order
    """
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]:
                arr[i], arr[j] = (arr[j], arr[i])
    return arr


def median(tableau: list[int]) -> float:
    """
    Function that returns the median of the elements of the array
    :param tableau: the array to find the median of
    :return: the median of the elements of the array
    """
    if len(tableau) == 0:
        return None
    
    new: list[int] = sort_ascending(tableau)
    # n: int = len(new)
    # if n%2==0:
    #     m: float = (new[n//2]+new[n//2+1])/2
    # else:
    #     m: float = float(new[n//2])
    # return m

    mid: int = len(new)//2
    return new[mid] if len(new)%2==1 else (new[mid]+new[mid-1])/2