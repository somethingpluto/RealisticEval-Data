import math

def convert_file_size(size_bytes: int) -> str:
    """
    Converts a file size in bytes to a human-readable format.
    For example:
        input: 2120
        output: 2KB
    Args:
        size_bytes (int): The size in bytes to be converted.

    Returns:
        str: The converted size in a human-readable format (e.g., "2KB", "1MB").
    """
    if size_bytes == 0:
        return '0B'
    
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    
    return '%s%s' % (s, size_name[i])
# Unit test class
import unittest


class TestFileSizeConverter(unittest.TestCase):


    def test_zero_bytes(self):
        self.assertEqual(convert_file_size(0), "0B")

    def test_bytes_less_than_1KB(self):
        self.assertEqual(convert_file_size(512), "512B")

    def test_exactly_1KB(self):
        self.assertEqual(convert_file_size(1024), "1KB")

    def test_2KB(self):
        self.assertEqual(convert_file_size(2048), "2KB")

    def test_exactly_1MB(self):
        self.assertEqual(convert_file_size(1048576), "1MB")

    def test_5MB(self):
        self.assertEqual(convert_file_size(5242880), "5MB")

    def test_exactly_1GB(self):
        self.assertEqual(convert_file_size(1073741824), "1GB")
if __name__ == '__main__':
    unittest.main()