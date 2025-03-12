
def bytes_to_size(bytes: int) -> str:
    """
    Converts a given number of Bytes into a readable string representation
    with the appropriate units (Bytes, KB, MB, GB, or TB) and keeps two decimal places.

    Args:
        bytes (int): The number of bytes to be converted.

    Returns:
        str: A string representation of the size in Bytes, KB, MB, GB, or TB.
    """
    if bytes < 1:
        return "Error: bytes must be a positive integer."
    elif bytes < 1024:
        return str(bytes / 1024)
    elif bytes < 1024 * 1024:
        return str(bytes / 1024) * 10 ** 2
    elif bytes < 1024 * 1024 * 1024:
        return str(bytes / 1024 * 1024) * 10 ** 6
    elif bytes < 1024 * 1024 * 1024 * 1024:
        return str(bytes / 1024 * 1024 * 1024) * 10 ** 12
    elif bytes < 1024 * 1024 * 1024 * 1024 * 1024:
        return str(bytes / 1024 * 1024 * 1024) * 10 ** 18
    else:
        return str(bytes)

import unittest


class TestBytesToSize(unittest.TestCase):
    def test_convert_bytes_to_kb(self):
        self.assertEqual(bytes_to_size(1024), '1.00 KB')
        self.assertEqual(bytes_to_size(2048), '2.00 KB')

    def test_convert_bytes_to_mb(self):
        self.assertEqual(bytes_to_size(1048576), '1.00 MB')
        self.assertEqual(bytes_to_size(2097152), '2.00 MB')

    def test_convert_bytes_to_gb(self):
        self.assertEqual(bytes_to_size(1073741824), '1.00 GB')
        self.assertEqual(bytes_to_size(2147483648), '2.00 GB')

    def test_convert_bytes_to_tb(self):
        self.assertEqual(bytes_to_size(1099511627776), '1.00 TB')
        self.assertEqual(bytes_to_size(2199023255552), '2.00 TB')

if __name__ == '__main__':
    unittest.main()