import unittest
from my_dictionaries import (
    create_empty_dictionary,
    add_key_value,
    get_value,
    check_key,
    remove_key_value,
    count_key_value_pairs,
    get_keys,
    get_values,
    get_items,
    update_values,
    merge_dictionaries,
    clear_dictionary,
    find_key_with_max_value,
    find_key_with_min_value,
    check_same_key_value_pairs,
)

class TestDictionaryFunctions(unittest.TestCase):

    def test_create_empty_dictionary(self):
        dictionary = create_empty_dictionary()
        self.assertIsInstance(dictionary, dict)
        self.assertEqual(len(dictionary), 0)

    def test_add_key_value(self):
        dictionary = {}
        add_key_value(dictionary, "key1", "value1")
        self.assertEqual(dictionary["key1"], "value1")
        add_key_value(dictionary, "key2", "value2")
        self.assertEqual(dictionary["key2"], "value2")

    def test_get_value(self):
        dictionary = {"key1": "value1", "key2": "value2"}
        self.assertEqual(get_value(dictionary, "key1"), "value1")
        self.assertEqual(get_value(dictionary, "key3"), None)

    def test_check_key(self):
        dictionary = {"key1": "value1", "key2": "value2"}
        self.assertTrue(check_key(dictionary, "key1"))
        self.assertFalse(check_key(dictionary, "key3"))

    def test_remove_key_value(self):
        dictionary = {"key1": "value1", "key2": "value2"}
        remove_key_value(dictionary, "key1")
        self.assertNotIn("key1", dictionary)
        self.assertRaises(KeyError, remove_key_value, dictionary, "key3")

    def test_count_key_value_pairs(self):
        dictionary = {"key1": "value1", "key2": "value2"}
        self.assertEqual(count_key_value_pairs(dictionary), 2)
        dictionary = {}
        self.assertEqual(count_key_value_pairs(dictionary), 0)

    def test_get_keys(self):
        dictionary = {"key1": "value1", "key2": "value2"}
        self.assertEqual(get_keys(dictionary), ["key1", "key2"])
        dictionary = {}
        self.assertEqual(get_keys(dictionary), [])

    def test_get_values(self):
        dictionary = {"key1": "value1", "key2": "value2"}
        self.assertEqual(get_values(dictionary), ["value1", "value2"])
        dictionary = {}
        self.assertEqual(get_values(dictionary), [])

    def test_get_items(self):
        dictionary = {"key1": "value1", "key2": "value2"}
        self.assertEqual(get_items(dictionary), [("key1", "value1"), ("key2", "value2")])
        dictionary = {}
        self.assertEqual(get_items(dictionary), [])

    def test_update_values(self):
        dictionary = {"key1": "value1", "key2": "value2"}
        update_values(dictionary, "key1", "new_value1")
        self.assertEqual(dictionary["key1"], "new_value1")
        update_values(dictionary, "key3", "value3")  # No error should be raised

    def test_merge_dictionaries(self):
        dictionary1 = {"key1": "value1"}
        dictionary2 = {"key2": "value2"}
        merged_dict = merge_dictionaries(dictionary1, dictionary2)
        self.assertEqual(merged_dict, {"key1": "value1", "key2": "value2"})

    def test_clear_dictionary(self):
        dictionary = {"key1": "value1", "key2": "value2"}
        clear_dictionary(dictionary)
        self.assertEqual(len(dictionary), 0)

    def test_find_key_with_max_value(self):
        dictionary = {"key1": 10, "key2": 20, "key3": 5}
        self.assertEqual(find_key_with_max_value(dictionary), "key2")

    def test_find_key_with_min_value(self):
        dictionary = {"key1": 10, "key2": 20, "key3": 5}
        self.assertEqual(find_key_with_min_value(dictionary), "key3")

    def test_check_same_key_value_pairs(self):
        dictionary1 = {"key1": "value1", "key2": "value2"}
        dictionary2 = {"key2": "value2", "key1": "value1"}
        self.assertTrue(check_same_key_value_pairs(dictionary1, dictionary2))
        dictionary3 = {"key1": "value1", "key2": "value2"}
        dictionary4 = {"key1": "value1", "key2": "value3"}
        self.assertFalse(check_same_key_value_pairs(dictionary3, dictionary4))

if __name__ == '__main__':
    unittest.main()
