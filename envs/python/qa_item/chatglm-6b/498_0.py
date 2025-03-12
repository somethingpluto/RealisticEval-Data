
import hashlib

def compute_md5(input_string: str) -> str:
    """
    Computes and returns the MD5 hash of the input string.

    Args:
        input_string (str): The string to be hashed

    Returns:
        str: he MD5 hash of the input string in hexadecimal format
    """
    # Convert the input string to a byte array
    input_bytes = bytearray(input_string.encode('utf-8'))

    # Compute the MD5 hash using the MD5 algorithm
    md5_hash = hashlib.md5(input_bytes).hexdigest()

    # Convert the MD5 hash to a hexadecimal string
    return "".join([f"{md5_hash[:2]}" for md5_hash in md5_hash.split(" ")])

import unittest


class TestComputeMD5(unittest.TestCase):

    def test_empty_string(self):
        """ Test the MD5 hash of an empty string. """
        self.assertEqual(compute_md5(''), 'd41d8cd98f00b204e9800998ecf8427e')

    def test_simple_string(self):
        """ Test the MD5 hash of a simple string. """
        self.assertEqual(compute_md5('Hello, World!'), '65a8e27d8879283831b664bd8b7f0ad4')

    def test_numeric_string(self):
        """ Test the MD5 hash of a numeric string. """
        self.assertEqual(compute_md5('123456'), 'e10adc3949ba59abbe56e057f20f883e')

    def test_special_characters(self):
        """ Test the MD5 hash of a string with special characters. """
        self.assertEqual(compute_md5('!@#$%^&*()'), '05b28d17a7b6e7024b6e5d8cc43a8bf7')

    def test_long_string(self):
        """ Test the MD5 hash of a long string. """
        long_string = 'a' * 1000  # A string of 1000 'a' characters
        expected_hash = 'cabe45dcc9ae5b66ba86600cca6b8ba8'  # MD5 of 'aaaa....' (1000 'a's)
        self.assertEqual(compute_md5(long_string), expected_hash)
if __name__ == '__main__':
    unittest.main()