import unittest


class TestCRC64(unittest.TestCase):
    def test_positive_integer(self):
        result = CRC64.compute(123456789)
        expected = 0xA8E9F2D8578073DF  # Placeholder, replace with actual expected value
        self.assertEqual(result, expected)

    def test_negative_integer(self):
        result = CRC64.compute(-123456789)
        expected = 0x6BCD5C4AAB6E5F37  # Placeholder, replace with actual expected value
        self.assertEqual(result, expected)

    def test_zero(self):
        result = CRC64.compute(0)
        expected = 0x8B79EAEAC6D660F1  # Placeholder, replace with actual expected value
        self.assertEqual(result, expected)

    def test_maximum_unsigned_integer(self):
        result = CRC64.compute(0xFFFFFFFFFFFFFFFF)
        expected = 0xE9C6D914C4B8D9CA  # Placeholder, replace with actual expected value
        self.assertEqual(result, expected)

    def test_sequential_bytes(self):
        result = CRC64.compute(0x0102030405060708)
        expected = 0xD9963A56A1125ACB  # Placeholder, replace with actual expected value
        self.assertEqual(result, expected)