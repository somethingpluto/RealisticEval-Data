def count_numbers(s: str) -> int:
    return sum(1 for char in s if char.isdigit())
import unittest


class TestCountNumbers(unittest.TestCase):

    def test_multiple_numbers(self):
        result = count_numbers('There are 123 numbers in this string.')
        self.assertEqual(result, 3)  # '123' contains three numeric characters

    def test_no_numbers(self):
        result = count_numbers('No numbers here!')
        self.assertEqual(result, 0)  # No numeric characters in 'No numbers here!'

    def test_mixed_characters(self):
        result = count_numbers('Room 101 and Room 102')
        self.assertEqual(result, 6)  # '101' and '102' together contain six numeric characters

    def test_only_numbers(self):
        result = count_numbers('1234567890')
        self.assertEqual(result, 10)  # '1234567890' contains ten numeric characters

    def test_empty_string(self):
        result = count_numbers('')
        self.assertEqual(result, 0)  # An empty string contains no numeric characters

if __name__ == '__main__':
    unittest.main()