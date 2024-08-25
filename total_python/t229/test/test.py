import unittest


class TestGetFileSize(unittest.TestCase):

    def test_auto_unit_selection(self):
        """ Test automatic unit selection based on file size """
        # Test that units are correctly auto-selected based on size
        self.assertEqual(get_file_size(500), ('500 B', 500))  # Bytes
        self.assertEqual(get_file_size(2000), ('1.95 KB', 1.953125))  # Kilobytes
        self.assertEqual(get_file_size(3 * 1024 ** 2), ('3.00 MB', 3.0))  # Megabytes
        self.assertEqual(get_file_size(5 * 1024 ** 3), ('5.00 GB', 5.0))  # Gigabytes

    def test_specific_unit(self):
        """ Test output when specific units are requested """
        # Test for each unit conversion
        self.assertEqual(get_file_size(1024, 'KB'), ('1.00 KB', 1.0))

    def test_invalid_unit(self):
        """ Test behavior when an invalid unit is provided """
        with self.assertRaises(ValueError):
            get_file_size(1024, 'xyz')  # Should raise ValueError for invalid unit

    def test_large_file_size(self):
        """ Test with very large file size """
        # Testing a large number, should format to gigabytes
        self.assertEqual(get_file_size(10 * 1024 ** 4), ('10240.00 GB', 10240.0))

    def test_zero_bytes(self):
        """ Test with zero bytes """
        # Edge case for zero bytes
        self.assertEqual(get_file_size(0), ('0 B', 0))
