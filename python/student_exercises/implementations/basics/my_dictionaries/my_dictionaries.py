def create_empty_dictionary() -> dict:
    """
    Create an empty dictionary.

    Returns:
        dict: An empty dictionary.

    Example:
        >>> create_empty_dictionary()
        {}
    """
    return {}


def add_key_value(dictionary: dict, key, value):
    """
    Add a key-value pair to the dictionary.

    Args:
        dictionary (dict): The dictionary to add the key-value pair to.
        key: The key to add.
        value: The value to add.

    Example:
        >>> dictionary = {}
        >>> add_key_value(dictionary, "key1", "value1")
        >>> dictionary
        {'key1': 'value1'}
        >>> add_key_value(dictionary, "key2", "value2")
        >>> dictionary
        {'key1': 'value1', 'key2': 'value2'}
    """
    dictionary[key] = value

def get_value(dictionary: dict, key):
    """
    Get the value associated with a key from the dictionary.

    Args:
        dictionary (dict): The dictionary to retrieve the value from.
        key: The key to retrieve the value for.

    Returns:
        The value associated with the key, or None if the key is not found.

    Example:
        >>> dictionary = {"key1": "value1", "key2": "value2"}
        >>> get_value(dictionary, "key1")
        'value1'
        >>> get_value(dictionary, "key3")
        None
    """
    return dictionary.get(key)


def check_key(dictionary: dict, key) -> bool:
    """
    Check if a key exists in the dictionary.

    Args:
        dictionary (dict): The dictionary to check.
        key: The key to check for.

    Returns:
        bool: True if the key exists in the dictionary, False otherwise.

    Example:
        >>> dictionary = {"key1": "value1", "key2": "value2"}
        >>> check_key(dictionary, "key1")
        True
        >>> check_key(dictionary, "key3")
        False
    """
    return key in dictionary


def remove_key_value(dictionary: dict, key):
    """
    Remove a key-value pair from the dictionary.

    Args:
        dictionary (dict): The dictionary to remove the key-value pair from.
        key: The key to remove.

    Example:
        >>> dictionary = {"key1": "value1", "key2": "value2"}
        >>> remove_key_value(dictionary, "key1")
        >>> dictionary
        {'key2': 'value2'}
    """
    dictionary.pop(key)


def count_key_value_pairs(dictionary: dict) -> int:
    """
    Count the number of key-value pairs in the dictionary.

    Args:
        dictionary (dict): The dictionary to count the key-value pairs.

    Returns:
        int: The number of key-value pairs in the dictionary.

    Example:
        >>> dictionary = {"key1": "value1", "key2": "value2"}
        >>> count_key_value_pairs(dictionary)
        2
        >>> dictionary = {}
        >>> count_key_value_pairs(dictionary)
        0
    """
    return len(dictionary)


def get_keys(dictionary: dict) -> list:
    """
    Get a list of keys from the dictionary.

    Args:
        dictionary (dict): The dictionary to retrieve the keys from.

    Returns:
        list: A list of keys from the dictionary.

    Example:
        >>> dictionary = {"key1": "value1", "key2": "value2"}
        >>> get_keys(dictionary)
        ['key1', 'key2']
        >>> dictionary = {}
        >>> get_keys(dictionary)
        []
    """
    return list(dictionary.keys())



def get_values(dictionary: dict) -> list:
    """
    Get a list of values from the dictionary.

    Args:
        dictionary (dict): The dictionary to retrieve the values from.

    Returns:
        list: A list of values from the dictionary.

    Example:
        >>> dictionary = {"key1": "value1", "key2": "value2"}
        >>> get_values(dictionary)
        ['value1', 'value2']
        >>> dictionary = {}
        >>> get_values(dictionary)
        []
    """
    return list(dictionary.values())


def get_items(dictionary: dict) -> list:
    """
    Get a list of key-value pairs from the dictionary.

    Args:
        dictionary (dict): The dictionary to retrieve the key-value pairs from.

    Returns:
        list: A list of key-value pairs from the dictionary.

    Example:
        >>> dictionary = {"key1": "value1", "key2": "value2"}
        >>> get_items(dictionary)
        [('key1', 'value1'), ('key2', 'value2')]
        >>> dictionary = {}
        >>> get_items(dictionary)
        []
    """
    return list(dictionary.items())


def update_values(dictionary: dict, key, value):
    """
    Update the value associated with a key in the dictionary.

    Args:
        dictionary (dict): The dictionary to update the value in.
        key: The key to update.
        value: The new value to assign.

    Example:
        >>> dictionary = {"key1": "value1", "key2": "value2"}
        >>> update_values(dictionary, "key1", "new_value1")
        >>> dictionary
        {'key1': 'new_value1', 'key2': 'value2'}
        >>> update_values(dictionary, "key3", "value3")  # No error should be raised
    """
    dictionary[key] = value


def merge_dictionaries(dictionary1: dict, dictionary2: dict) -> dict:
    """
    Merge two dictionaries into a new dictionary.

    Args:
        dictionary1 (dict): The first dictionary to merge.
        dictionary2 (dict): The second dictionary to merge.

    Returns:
        dict: A new dictionary containing the merged key-value pairs.

    Example:
        >>> dictionary1 = {"key1": "value1"}
        >>> dictionary2 = {"key2": "value2"}
        >>> merge_dictionaries(dictionary1, dictionary2)
        {'key1': 'value1', 'key2': 'value2'}
    """
    dictionary1.update(dictionary2)
    return dictionary1
    # return {**dictionary1, **dictionary2}


def clear_dictionary(dictionary: dict):
    """
    Clear all key-value pairs from the dictionary.

    Args:
        dictionary (dict): The dictionary to clear.

    Example:
        >>> dictionary = {"key1": "value1", "key2": "value2"}
        >>> clear_dictionary(dictionary)
        >>> dictionary
        {}
    """
    dictionary.clear()


def find_key_with_max_value(dictionary: dict):
    """
    Find the key with the maximum value in the dictionary.

    Args:
        dictionary (dict): The dictionary to search.

    Returns:
        The key with the maximum value, or None if the dictionary is empty.

    Example:
        >>> dictionary = {"key1": 10, "key2": 20, "key3": 5}
        >>> find_key_with_max_value(dictionary)
        'key2'
    """
    import math
    max_key, max_value = "", -math.inf

    for k, v in dictionary.items():
        if max_value < v:
            max_key = k
            max_value = v
    
    return max_key


def find_key_with_min_value(dictionary: dict):
    """
    Find the key with the minimum value in the dictionary.

    Args:
        dictionary (dict): The dictionary to search.

    Returns:
        The key with the minimum value, or None if the dictionary is empty.

    Example:
        >>> dictionary = {"key1": 10, "key2": 20, "key3": 5}
        >>> find_key_with_min_value(dictionary)
        'key3'
    """
    import math
    min_key, min_value = "", math.inf

    for k, v in dictionary.items():
        if min_value > v:
            min_key = k
            min_value = v
    
    return min_key


def check_same_key_value_pairs(dictionary1: dict, dictionary2: dict) -> bool:
    """
    Check if two dictionaries have the same key-value pairs.

    Args:
        dictionary1 (dict): The first dictionary to compare.
        dictionary2 (dict): The second dictionary to compare.

    Returns:
        bool: True if the dictionaries have the same key-value pairs, False otherwise.

    Example:
        >>> dictionary1 = {"key1": "value1", "key2": "value2"}
        >>> dictionary2 = {"key2": "value2", "key1": "value1"}
        >>> check_same_key_value_pairs(dictionary1, dictionary2)
        True
        >>> dictionary3 = {"key1": "value1", "key2": "value2"}
        >>> dictionary4 = {"key1": "value1", "key2": "value3"}
        >>> check_same_key_value_pairs(dictionary3, dictionary4)
        False
    """
    # for k, v in dictionary1.items():
    #     if k not in dictionary2:
    #         return False
        
    #     assert(k in dictionary2)

    #     if v != dictionary2[k]:
    #         return False
        
    # return True

    return len(dict(dictionary1.items() & dictionary2.items())) == len(dictionary1)
