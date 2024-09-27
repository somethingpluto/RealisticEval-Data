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