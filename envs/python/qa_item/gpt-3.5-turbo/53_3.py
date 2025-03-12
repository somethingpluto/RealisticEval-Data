import sys
import ctypes

def size_in_bytes(obj) -> int:
    """
    computes and returns the size of an object in bytes in memory

    Args:
        obj (any): question object

    Returns: the size of this object in bytes in memory

    """
    size = sys.getsizeof(obj)
    if isinstance(obj, str):
        size += sys.getsizeof(obj.encode('utf-8'))
    elif isinstance(obj, tuple):
        size += sum(size_in_bytes(item) for item in obj)
    elif isinstance(obj, list):
        size += sum(size_in_bytes(item) for item in obj)
    elif isinstance(obj, dict):
        size += sum(size_in_bytes(key) + size_in_bytes(value) for key, value in obj.items())
    return size
import unittest
import sys

class TestSizeInBytes(unittest.TestCase):

    def test_size_of_integer(self):
        # Test the size of an integer
        integer_value = 42
        expected_size = sys.getsizeof(integer_value)
        result_size = size_in_bytes(integer_value)
        self.assertEqual(result_size, expected_size)

    def test_size_of_string(self):
        # Test the size of a string
        string_value = "Hello, world!"
        expected_size = sys.getsizeof(string_value)
        result_size = size_in_bytes(string_value)
        self.assertEqual(result_size, expected_size)

    def test_size_of_list(self):
        # Test the size of a list
        list_value = [1, 2, 3, 4, 5]
        expected_size = sys.getsizeof(list_value)
        result_size = size_in_bytes(list_value)
        self.assertEqual(result_size, expected_size)

    def test_size_of_dictionary(self):
        # Test the size of a dictionary
        dict_value = {'key1': 'value1', 'key2': 'value2'}
        expected_size = sys.getsizeof(dict_value)
        result_size = size_in_bytes(dict_value)
        self.assertEqual(result_size, expected_size)

    def test_size_of_custom_object(self):
        # Test the size of a custom object
        class CustomObject:
            def __init__(self):
                self.attr1 = 'a'
                self.attr2 = 123
        custom_obj = CustomObject()
        expected_size = sys.getsizeof(custom_obj)  # Note: Does not include size of attributes unless explicitly calculated
        result_size = size_in_bytes(custom_obj)
        self.assertEqual(result_size, expected_size)
if __name__ == '__main__':
    unittest.main()