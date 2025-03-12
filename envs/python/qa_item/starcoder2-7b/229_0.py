def convert_file_size(size_bytes: int) -> str:
    if size_bytes < 1024:
        return f"{size_bytes}B"
    elif 1024 <= size_bytes < 1024**2:
        return f"{size_bytes / 1024}KB"
    elif 1024**2 <= size_bytes < 1024**3:
        return f"{size_bytes / 1024**2}MB"
    elif 1024**3 <= size_bytes < 1024**4:
        return f"{size_bytes / 1024**3}GB"
    elif 1024**4 <= size_bytes < 1024**5:
        return f"{size_bytes / 1024**4}TB"
    else:
        return f"{size_bytes / 1024**5}PB"
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