import unittest


class TestByteCountToDisplaySizeByteCountToDisplaySize(unittest.TestCase):

    def test_zero_bytes(self):
        """Test case for 0 bytes."""
        input_size = 0
        expected = "0 bytes"
        self.assertEqual(byte_count_to_display_size(input_size), expected)

    def test_bytes_less_than_kb(self):
        """Test case for bytes less than 1KB."""
        input_size = 500
        expected = "500 bytes"
        self.assertEqual(byte_count_to_display_size(input_size), expected)

    def test_exactly_one_kb(self):
        """Test case for exactly 1KB."""
        input_size = 1024
        result = byte_count_to_display_size(input_size)
        self.assertTrue(result == "1 KB" or result == "1.00 KB")

    def test_between_kb_and_mb(self):
        """Test case for a size between 1KB and 1MB."""
        input_size = 5000
        expected = "4.88 KB"
        self.assertEqual(byte_count_to_display_size(input_size), expected)

    def test_exactly_one_mb(self):
        """Test case for exactly 1MB."""
        input_size = 1048576  # 1024 * 1024
        result = byte_count_to_display_size(input_size)
        self.assertTrue(result == "1 MB" or result == "1.00 MB")
