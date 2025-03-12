from typing import Iterable

def sum_calibration_values(calibration_document: Iterable[str]) -> int:
    def get_digit(number: int, position: str) -> int:
        if position == 'first':
            return int(str(number)[0])
        elif position == 'last':
            return int(str(number)[-1])
    
    total_sum = 0
    for line in calibration_document:
        numbers = [int(num) for num in line.split() if num.isdigit()]
        for num in numbers:
            calibration_value = get_digit(num, 'first') * 10 + get_digit(num, 'last')
            total_sum += calibration_value
    
    return total_sum
import unittest

class TestSumCalibrationValues(unittest.TestCase):

    def test_basic_calculations(self):
        # Test with a simple input where lines contain at least two digits
        document = [
            "Reading 1234 calibration",
            "Measure 5678 complete",
            "End of data 91011"
        ]
        self.assertEqual(sum_calibration_values(document), 163)

    def test_no_digits(self):
        # Test lines with no digits
        document = [
            "No numbers here",
            "Still no numbers"
        ]
        self.assertEqual(sum_calibration_values(document), 0)

    def test_empty_lines(self):
        # Test with empty lines or lines with spaces
        document = [
            "",
            "   "
        ]
        self.assertEqual(sum_calibration_values(document), 0)

    def test_mixed_content(self):
        # Test with a mixture of valid and invalid lines
        document = [
            "Good line 1524 end",
            "Bad line",
            "Another good line 7681"
        ]
        self.assertEqual(sum_calibration_values(document), 85)
if __name__ == '__main__':
    unittest.main()