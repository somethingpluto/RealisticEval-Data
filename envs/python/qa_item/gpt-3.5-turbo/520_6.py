from typing import List

def compute_output_index(idx_1: int, idx_2: int) -> int:
    """
    Computes the output index from two given indices in the MultiVector's representation
    of the G_n orthonormal basis.

    This function interprets the integers as little-endian bitstrings, takes their XOR,
    and interprets the result as an integer in little-endian.

    Args:
        idx_1 (int): Input index 1.
        idx_2 (int): Input index 2.

    Returns:
        int: The computed output index.
    """

    # Convert indices to binary strings and reverse them to interpret as little-endian
    bin_str_1 = bin(idx_1)[2:][::-1]
    bin_str_2 = bin(idx_2)[2:][::-1]
    
    # Pad the shorter binary string with zeros to match the length of the longer one
    max_len = max(len(bin_str_1), len(bin_str_2))
    bin_str_1 = bin_str_1.ljust(max_len, '0')
    bin_str_2 = bin_str_2.ljust(max_len, '0')
    
    # Perform XOR on the two binary strings
    xor_result = ''.join(str(int(digit_1) ^ int(digit_2)) for digit_1, digit_2 in zip(bin_str_1, bin_str_2))
    
    # Convert the XOR result back to an integer interpreting it as little-endian
    output_index = int(xor_result[::-1], 2)
    
    return output_index
import unittest


class TestComputeOutputIndex(unittest.TestCase):

    def test_standard_case(self):
        """Test with two standard positive integers."""
        idx_1 = 3  # binary: 11
        idx_2 = 5  # binary: 101
        expected = 6  # 3 XOR 5 = 6
        result = compute_output_index(idx_1, idx_2)
        self.assertEqual(result, expected)

    def test_identical_indices(self):
        """Test with identical indices (should return 0)."""
        idx_1 = 7  # binary: 111
        idx_2 = 7  # binary: 111
        expected = 0  # 7 XOR 7 = 0
        result = compute_output_index(idx_1, idx_2)
        self.assertEqual(result, expected)

    def test_zero_index(self):
        """Test with one index as zero."""
        idx_1 = 0  # binary: 0
        idx_2 = 5  # binary: 101
        expected = 5  # 0 XOR 5 = 5
        result = compute_output_index(idx_1, idx_2)
        self.assertEqual(result, expected)

    def test_large_numbers(self):
        """Test with large integer values."""
        idx_1 = 1024  # binary: 10000000000
        idx_2 = 2048  # binary: 100000000000
        expected = 3072  # 1024 XOR 2048 = 3072
        result = compute_output_index(idx_1, idx_2)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()