def convert_file_size(size_bytes: int) -> str:
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
    i = int(floor(log(size_bytes, 1024)))
    size_bytes = size_bytes / pow(1024, i)
    return f"{size_bytes:.2f} {suffixes[i]} "
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