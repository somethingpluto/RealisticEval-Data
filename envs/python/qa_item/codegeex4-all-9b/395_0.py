def sum_calibration_values(calibration_document) -> int:
    """
    Sums up calibration values extracted from the document.
    Each calibration value is formed by combining the first and last digits of numbers found in each line
    into a two-digit number.

    Args:
        calibration_document (iterable): An iterable of strings, each representing a line of text.

    Returns:
        int: The total sum of all calibration values.
    """
    total_sum = 0
    for line in calibration_document:
        numbers = [int(num) for num in line.split() if num.isdigit()]
        for number in numbers:
            if len(str(number)) > 1:
                first_digit = int(str(number)[0])
                last_digit = int(str(number)[-1])
                calibration_value = first_digit * 10 + last_digit
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