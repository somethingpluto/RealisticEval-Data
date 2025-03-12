
import numpy as np

def check_xor_sum(combination: np.ndarray) -> bool:
    """
    Checks the XOR sums of specific columns in a given combination array.

    Args:
        combination (np.ndarray): A 2D numpy array where each column corresponds
                                  to a specific value.

    Returns:
        bool: True if the XOR sums of the specified columns match the required
              values; otherwise, False.
    """
    # Initialize empty dictionary to store the XOR sums for each column
    xor_sums = {}

    # Loop through each row of the combination array
    for i in range(combination.shape[0]):
        # Loop through each column of the current row
        for j in range(combination.shape[1]):
            # Check if the current column is specified
            if i == 0 and j in XOR_SUMS:
                # If it is, add the XOR sum for that column to the dictionary
                xor_sums[j] = combination[i][j]
            else:
                # If it's not, add the XOR sum for the corresponding column to the
                # dictionary
                xor_sums[j] = combination[i][j]

    # Check if the XOR sums for the specified columns match the required values
    required_values = [0, 1, 0, 1]
    for j in range(combination.shape[1]):
        for i in range(combination.shape[0]):
            if i == 0 and j in required_values:
                # If it matches, return True
                return True
    return False

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