def get_first_three_elements(lst: list) -> list:
    """
    Return the first three elements of the list
    :param lst: The list
    :return: The first three elements of the list
    exemple:
    >>> get_first_three_elements([1, 2, 3, 4, 5]) -> [1, 2, 3]
    >>> get_first_three_elements([]) -> []
    >>> get_first_three_elements([1]) -> [1]
    >>> get_first_three_elements([1, 2]) -> [1, 2]
    """
    return lst[:3]
        

def get_last_two_elements(lst: list) -> list:
    """
    Return the last two elements of the list
    :param lst: The list
    :return: The last two elements of the list
    exemple:
    >>> get_last_two_elements([1, 2, 3, 4, 5]) -> [4, 5]
    >>> get_last_two_elements([]) -> []
    >>> get_last_two_elements([1]) -> [1]
    >>> get_last_two_elements([1, 2]) -> [1, 2]
    """
    return lst[-2:]

def reverse_list(lst: list) -> list:
    """
    Return the list in reverse order
    :param lst: The list
    :return: The list in reverse order
    exemple:
    >>> reverse_list([1, 2, 3, 4, 5]) -> [5, 4, 3, 2, 1]
    >>> reverse_list([]) -> []
    >>> reverse_list([1]) -> [1]
    >>> reverse_list([1, 2]) -> [2, 1]
    """
    return lst[::-1]

def get_even_index_elements(lst: list) -> list:
    """
    Return the elements of the list at even indexes
    :param lst: The list
    :return: The elements of the list at even indexes
    exemple:
    >>> get_even_index_elements([1, 2, 3, 4, 5]) -> [1, 3, 5]
    >>> get_even_index_elements([]) -> []
    >>> get_even_index_elements([1]) -> [1]
    >>> get_even_index_elements([1, 2]) -> [1]
    """
    return lst[::2]

def get_odd_index_elements(lst: list) -> list:
    """
    Return the elements of the list at odd indexes
    :param lst: The list
    :return: The elements of the list at odd indexes
    exemple:
    >>> get_odd_index_elements([1, 2, 3, 4, 5]) -> [2, 4]
    >>> get_odd_index_elements([]) -> []
    >>> get_odd_index_elements([1]) -> []
    >>> get_odd_index_elements([1, 2]) -> [2]
    """
    return lst[1::2]

def remove_duplicates(lst: list) -> list:
    """
    Return the list without duplicates
    :param lst: The list
    :return: The list without duplicates
    exemple:
    >>> remove_duplicates([1, 2, 3, 4, 5]) -> [1, 2, 3, 4, 5]
    >>> remove_duplicates([]) -> []
    >>> remove_duplicates([1]) -> [1]
    >>> remove_duplicates([1, 1, 1]) -> [1]
    >>> remove_duplicates([1, 2, 3]) -> [1, 2, 3]
    """
    return list(set(lst))

def square_elements(lst: list) -> list:
    """
    Return the list with all elements squared
    :param lst: The list
    :return: The list with all elements squared
    exemple:
    >>> square_elements([1, 2, 3, 4, 5]) -> [1, 4, 9, 16, 25]
    >>> square_elements([]) -> []
    >>> square_elements([0]) -> [0]
    >>> square_elements([-1, 2, -3]) -> [1, 4, 9]
    """
    return [x**2 for x in lst]
    # return list(map(lambda x: x*x, lst))

def double_elements(lst: list) -> list:
    """
    Return the list with all elements doubled
    :param lst: The list
    :return: The list with all elements doubled
    exemple:
    >>> double_elements([1, 2, 3, 4, 5]) -> [2, 4, 6, 8, 10]
    >>> double_elements([]) -> []
    >>> double_elements([0]) -> [0]
    >>> double_elements([-1, 2, -3]) -> [-2, 4, -6]
    """
    return [i*2 for i in lst]
    #return list(map(lambda x: x+x, lst))

def sum_of_elements(lst: list) -> int:
    """
    Return the sum of all elements of the list
    :param lst: The list
    :return: The sum of all elements of the list
    exemple:
    >>> sum_of_elements([1, 2, 3, 4, 5]) -> 15
    >>> sum_of_elements([]) -> 0
    >>> sum_of_elements([1]) -> 1
    >>> sum_of_elements([1, -1]) -> 0
    """
    if lst == []:
      return 0
    elif len(lst) == 1:
        return lst[0]
    
    return lst.pop() + sum_of_elements(lst)

    # ret = 0
    # for i in lst:
    #     ret += i
    
    # return ret

def is_sorted(lst: list) -> bool:
    """
    Return True if the list is sorted, False otherwise
    :param lst: The list
    :return: True if the list is sorted, False otherwise
    exemple:
    >>> is_sorted([1, 2, 3, 4, 5]) -> True
    >>> is_sorted([5, 4, 3, 2, 1]) -> False
    >>> is_sorted([]) -> True
    >>> is_sorted([1]) -> True
    >>> is_sorted([1, 1, 1]) -> True
    >>> is_sorted([1, 2, 1]) -> False
    """
    # last_elem = 0 # O(n)
    # for i in lst:
    #     if i < last_elem:
    #         return False
    #     last_elem = i

    # return True

    return sorted(lst) == lst # O(nlog(n))

def count_occurrences(lst: list, element: int) -> int:
    """
    Return the number of occurrences of the element in the list
    :param lst: The list
    :param element: The element
    :return: The number of occurrences of the element in the list
    exemple:
    >>> count_occurrences([1, 2, 2, 3, 3, 3, 4, 5], 2) -> 2
    >>> count_occurrences([1, 2, 2, 3, 3, 3, 4, 5], 3) -> 3
    >>> count_occurrences([1, 2, 2, 3, 3, 3, 4, 5], 6) -> 0
    >>> count_occurrences([], 1) -> 0
    >>> count_occurrences([1, 1, 1], 1) -> 3
    """
    cnt = 0
    for item in lst:
        if item == element:
            cnt += 1
    
    return cnt
      
    

def find_maximum(lst: list) -> int: # O(n)
    """
    Return the maximum element of the list
    :param lst: The list
    :return: The maximum element of the list
    exemple:
    >>> find_maximum([1, 2, 3, 4, 5]) -> 5
    >>> find_maximum([]) -> None
    >>> find_maximum([1]) -> 1
    >>> find_maximum([-1, -2, -3]) -> -1
    """
    # lst.sort() => O(nlog(n))
    if lst == []:
      return None
    
    import math
    max_elem = -math.inf
    for item in lst:
        if item > max_elem:
            max_elem = item
    return max_elem

def find_minimum(lst: list) -> int:
    """
    Return the minimum element of the list
    :param lst: The list
    :return: The minimum element of the list
    exemple:
    >>> find_minimum([1, 2, 3, 4, 5]) -> 1
    >>> find_minimum([]) -> None
    >>> find_minimum([1]) -> 1
    >>> find_minimum([-1, -2, -3]) -> -3
    """
    if lst == []:
      return None
    
    import math
    max_elem = math.inf
    for item in lst:
        if item < max_elem:
            max_elem = item
    return max_elem

def combine_lists(lst1: list, lst2: list) -> list:
    """
    Return a list with the elements of lst1 and lst2 combined
    :param lst1: The first list
    :param lst2: The second list
    :return: A list with the elements of lst1 and lst2 combined
    exemple:
    >>> combine_lists([1, 2, 3], [4, 5, 6]) -> [1, 4, 2, 5, 3, 6]
    >>> combine_lists([], []) -> []
    >>> combine_lists([1], [2]) -> [1, 2]
    """
    ret = []
    for i in range(len(lst1)):
        ret.append(lst1[i])
        ret.append(lst2[i])
    
    return ret
        

def is_palindrome(lst: list) -> bool:
    """
    Return True if the list is a palindrome, False otherwise
    :param lst: The list
    :return: True if the list is a palindrome, False otherwise
    exemple:
    >>> is_palindrome([1, 2, 3, 2, 1]) -> True
    >>> is_palindrome([1, 2, 3, 4, 5]) -> False
    >>> is_palindrome([]) -> True
    >>> is_palindrome([1]) -> True
    >>> is_palindrome([2, 2, 1]) -> False
    """
    return reverse_list(lst) == lst
