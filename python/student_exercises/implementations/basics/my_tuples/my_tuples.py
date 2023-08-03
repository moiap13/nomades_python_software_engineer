def create_empty_tuple() -> tuple:
    """
    Create an empty tuple.

    Returns:
        tuple: An empty tuple.

    Example:
        >>> create_empty_tuple()
        ()
    """
    return ()


def create_tuple_from_list(lst: list) -> tuple:
    """
    Create a tuple from a list.

    Args:
        lst (list): The list to create a tuple from.

    Returns:
        tuple: A tuple created from the list.

    Example:
        >>> lst = [1, 2, 3, 4, 5]
        >>> create_tuple_from_list(lst)
        (1, 2, 3, 4, 5)
    """
    return tuple(lst)


def access_element(t: tuple, index: int):
    """
    Access an element in the tuple using its index.

    Args:
        t (tuple): The tuple to access the element from.
        index (int): The index of the element to access.

    Returns:
        The element at the specified index in the tuple.

    Example:
        >>> t = (1, 2, 3, 4, 5)
        >>> access_element(t, 2)
        3
    """
    return t[index]


def slice_tuple(t: tuple, start: int, end: int) -> tuple:
    """
    Slice a tuple to extract a sub-tuple based on start and end indices.

    Args:
        t (tuple): The tuple to slice.
        start (int): The index to start the slice (inclusive).
        end (int): The index to end the slice (exclusive).

    Returns:
        tuple: The sliced sub-tuple.

    Example:
        >>> t = (1, 2, 3, 4, 5)
        >>> slice_tuple(t, 1, 4)
        (2, 3, 4)
    """
    return t[start:end]


def check_element(t: tuple, element) -> bool:
    """
    Check if an element exists in the tuple.

    Args:
        t (tuple): The tuple to check.
        element: The element to check for.

    Returns:
        bool: True if the element exists in the tuple, False otherwise.

    Example:
        >>> t = (1, 2, 3, 4, 5)
        >>> check_element(t, 3)
        True
    """
    return element in t


def get_tuple_length(t: tuple) -> int:
    """
    Get the length of the tuple.

    Args:
        t (tuple): The tuple to get the length of.

    Returns:
        int: The length of the tuple.

    Example:
        >>> t = (1, 2, 3, 4, 5)
        >>> get_tuple_length(t)
        5
    """
    return len(t)


def concatenate_tuples(t1: tuple, t2: tuple) -> tuple:
    """
    Concatenate two tuples into a single tuple.

    Args:
        t1 (tuple): The first tuple.
        t2 (tuple): The second tuple.

    Returns:
        tuple: The concatenated tuple.

    Example:
        >>> t1 = (1, 2, 3)
        >>> t2 = (4, 5, 6)
        >>> concatenate_tuples(t1, t2)
        (1, 2, 3, 4, 5, 6)
    """
    return t1 + t2


def count_occurrences(t: tuple, element) -> int:
    """
    Count the number of occurrences of an element in the tuple.

    Args:
        t (tuple): The tuple to count the occurrences in.
        element: The element to count.

    Returns:
        int: The number of occurrences of the element in the tuple.

    Example:
        >>> t = (1, 2, 2, 3, 3, 3, 4, 5)
        >>> count_occurrences(t, 2)
        2
    """
    return t.count(element)


def find_index(t: tuple, element):
    """
    Find the index of the first occurrence of an element in the tuple.

    Args:
        t (tuple): The tuple to search.
        element: The element to find.

    Returns:
        int: The index of the first occurrence of the element in the tuple.

    Raises:
        ValueError: If the element is not found in the tuple.

    Example:
        >>> t = (1, 2, 3, 4, 5)
        >>> find_index(t, 3)
        2
    """
    return t.count(element)


def check_equal(t1: tuple, t2: tuple) -> bool:
    """
    Check if two tuples are equal.

    Args:
        t1 (tuple): The first tuple to compare.
        t2 (tuple): The second tuple to compare.

    Returns:
        bool: True if the tuples are equal, False otherwise.

    Example:
        >>> t1 = (1, 2, 3)
        >>> t2 = (1, 2, 3)
        >>> check_equal(t1, t2)
        True
    """
    return t1 == t2


def find_maximum(t: tuple):
    """
    Find the maximum element in the tuple.

    Args:
        t (tuple): The tuple to search.

    Returns:
        The maximum element in the tuple.

    Example:
        >>> t = (1, 2, 3, 4, 5)
        >>> find_maximum(t)
        5
    """
    return max(t)


def find_minimum(t: tuple):
    """
    Find the minimum element in the tuple.

    Args:
        t (tuple): The tuple to search.

    Returns:
        The minimum element in the tuple.

    Example:
        >>> t = (1, 2, 3, 4, 5)
        >>> find_minimum(t)
        1
    """
    return min(t)


def convert_tuple_to_list(t: tuple) -> list:
    """
    Convert a tuple to a list.

    Args:
        t (tuple): The tuple to convert.

    Returns:
        list: The converted list.

    Example:
        >>> t = (1, 2, 3, 4, 5)
        >>> convert_tuple_to_list(t)
        [1, 2, 3, 4, 5]
    """
    return list(t)


def convert_list_to_tuple(lst: list) -> tuple:
    """
    Convert a list to a tuple.

    Args:
        lst (list): The list to convert.

    Returns:
        tuple: The converted tuple.

    Example:
        >>> lst = [1, 2, 3, 4, 5]
        >>> convert_list_to_tuple(lst)
        (1, 2, 3, 4, 5)
    """
    return tuple(lst)


def sort_tuple(t: tuple) -> tuple:
    """
    Sort the elements of the tuple in ascending order.

    Args:
        t (tuple): The tuple to sort.

    Returns:
        tuple: The sorted tuple.

    Example:
        >>> t = (3, 2, 5, 1, 4)
        >>> sort_tuple(t)
        (1, 2, 3, 4, 5)
    """
    return tuple(sorted(t))
