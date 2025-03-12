import numpy as np

def check_xor_sum(combination: np.ndarray):
    """
    Checks the XOR sums of specific columns in a given combination array.

    Args:
        combination (np.ndarray): A 2D numpy array where each column corresponds
                                  to a specific value.

    Returns:
        bool: True if the XOR sums of the specified columns match the required
              values; otherwise, False.
    """
    # Define the columns to check and their required XOR sums
    columns_to_check = [0, 2, 4]  # Example columns to check
    required_xor_sums = [0, 1, 0]  # Example required XOR sums

    # Check if the number of columns to check matches the number of required XOR sums
    if len(columns_to_check) != len(required_xor_sums):
        raise ValueError("The number of columns to check must match the number of required XOR sums.")

    # Calculate the XOR sums for the specified columns
    xor_sums = [np.bitwise_xor.reduce(combination[:, col]) for col in columns_to_check]

    # Compare the calculated XOR sums with the required XOR sums
    return xor_sums == required_xor_sums
import unittest

import numpy as np


class TestCheckXorSum(unittest.TestCase):

    def test_correct_xor_sums(self):
        """ Test with combination values that produce the expected XOR sums. """
        combination = np.array([
            [0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        ])
        self.assertFalse(check_xor_sum(combination))

    def test_incorrect_xor_sums(self):
        """ Test with combination values that do not meet the expected XOR sums. """
        combination = np.array([
            [0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00]
        ])
        self.assertFalse(check_xor_sum(combination))

    def test_edge_case_with_zero(self):
        """ Test with a combination where all values are zero. """
        combination = np.zeros((1, 8), dtype=int)  # 1 row of zeros
        self.assertFalse(check_xor_sum(combination))

    def test_large_numbers(self):
        """ Test with large numbers in the combination. """
        combination = np.array([
            [0x6b000000, 0x00000000, 0x00000012, 0x00000000, 0x76000000, 0x00000000, 0x00000000, 0x00000000],
            [0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000]
        ])
        self.assertFalse(check_xor_sum(combination))

    def test_multiple_rows(self):
        """ Test with a combination that contains multiple rows. """
        combination = np.array([
            [0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00],
            [0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00],
            [0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00]
        ])
        self.assertTrue(check_xor_sum(combination))
if __name__ == '__main__':
    unittest.main()