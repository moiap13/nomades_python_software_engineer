def create_empty_set() -> set:
    """
    Create an empty set.

    Returns:
        set: An empty set.

    Example:
        >>> create_empty_set()
        set()
    """
    return set()


def create_set_from_list(lst: list) -> set:
    """
    Create a set from a list.

    Args:
        lst (list): The list to create the set from.

    Returns:
        set: A set containing the elements from the list.

    Example:
        >>> lst = [1, 2, 3, 4, 5]
        >>> create_set_from_list(lst)
        {1, 2, 3, 4, 5}

        >>> lst = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
        >>> create_set_from_list(lst)
        {1, 2, 3, 4, 5}
    """
    return set(lst)


def add_element(s: set, element):
    """
    Add an element to a set.

    Args:
        s (set): The set to add the element to.
        element: The element to add.

    Example:
        >>> s = set()
        >>> add_element(s, 1)
        >>> s
        {1}
    """
    s.add(element)


def remove_element(s: set, element):
    """
    Remove an element from a set.

    Args:
        s (set): The set to remove the element from.
        element: The element to remove.

    Example:
        >>> s = {1, 2, 3}
        >>> remove_element(s, 2)
        >>> s
        {1, 3}
    """
    s.remove(element)


def check_element(s: set, element) -> bool:
    """
    Check if an element is present in a set.

    Args:
        s (set): The set to check.
        element: The element to check.

    Returns:
        bool: True if the element is present, False otherwise.

    Example:
        >>> s = {1, 2, 3}
        >>> check_element(s, 1)
        True
        >>> check_element(s, 4)
        False
    """
    return element in s


def count_elements(s: set) -> int:
    """
    Count the number of elements in a set.

    Args:
        s (set): The set to count the elements in.

    Returns:
        int: The number of elements in the set.

    Example:
        >>> s = {1, 2, 3, 4, 5}
        >>> count_elements(s)
        5
    """
    return len(s)


def union_sets(s1: set, s2: set) -> set:
    """
    Perform the union of two sets.

    Args:
        s1 (set): The first set.
        s2 (set): The second set.

    Returns:
        set: A set containing all elements from both sets without duplicates.

    Example:
        >>> s1 = {1, 2, 3}
        >>> s2 = {3, 4, 5}
        >>> union_sets(s1, s2)
        {1, 2, 3, 4, 5}
    """
    return s1.union(s2)


def intersect_sets(s1: set, s2: set) -> set:
    """
    Perform the intersection of two sets.

    Args:
        s1 (set): The first set.
        s2 (set): The second set.

    Returns:
        set: A set containing elements present in both sets.

    Example:
        >>> s1 = {1, 2, 3}
        >>> s2 = {3, 4, 5}
        >>> intersect_sets(s1, s2)
        {3}
    """
    return s1.intersection(s2)


def difference_sets(s1: set, s2: set) -> set:
    """
    Find the difference between two sets.

    Args:
        s1 (set): The first set.
        s2 (set): The second set.

    Returns:
        set: A set containing elements from the first set that are not present in the second set.

    Example:
        >>> s1 = {1, 2, 3}
        >>> s2 = {3, 4, 5}
        >>> difference_sets(s1, s2)
        {1, 2}
    """
    return s1.difference(s2)


def check_subset(s1: set, s2: set) -> bool:
    """
    Check if one set is a subset of another set.

    Args:
        s1 (set): The first set.
        s2 (set): The second set.

    Returns:
        bool: True if s1 is a subset of s2, False otherwise.

    Example:
        >>> s1 = {1, 2, 3}
        >>> s2 = {1, 2, 3, 4, 5}
        >>> check_subset(s1, s2)
        True
        >>> check_subset(s2, s1)
        False
    """
    return s1.issubset(s2)


def check_disjoint(s1: set, s2: set) -> bool:
    """
    Check if two sets are disjoint (have no common elements).

    Args:
        s1 (set): The first set.
        s2 (set): The second set.

    Returns:
        bool: True if the sets are disjoint, False otherwise.

    Example:
        >>> s1 = {1, 2, 3}
        >>> s2 = {4, 5, 6}
        >>> check_disjoint(s1, s2)
        True
        >>> check_disjoint(s1, {3, 4})
        False
    """
    return s1.isdisjoint(s2)


def clear_set(s: set):
    """
    Clear all elements from a set.

    Args:
        s (set): The set to clear.

    Example:
        >>> s = {1, 2, 3}
        >>> clear_set(s)
        >>> s
        set()
    """
    s.clear()


def copy_set(s: set) -> set:
    """
    Create a shallow copy of a set.

    Args:
        s (set): The set to copy.

    Returns:
        set: A shallow copy of the set.

    Example:
        >>> s = {1, 2, 3}
        >>> s_copy = copy_set(s)
        >>> s_copy
        {1, 2, 3}
    """
    return s.copy()


def find_maximum(s: set):
    """
    Find the maximum element in a set.

    Args:
        s (set): The set to search.

    Returns:
        The maximum element in the set.

    Example:
        >>> s = {1, 2, 3, 4, 5}
        >>> find_maximum(s)
        5
    """
    return max(s)


def check_equal(s1: set, s2: set) -> bool:
    """
    Check if two sets are equal.

    Args:
        s1 (set): The first set.
        s2 (set): The second set.

    Returns:
        bool: True if the sets are equal, False otherwise.

    Example:
        >>> s1 = {1, 2, 3}
        >>> s2 = {3, 2, 1}
        >>> s3 = {1, 2, 4}
        >>> check_equal(s1, s2)
        True
        >>> check_equal(s1, s3)
        False
    """
    return s1 == s2
