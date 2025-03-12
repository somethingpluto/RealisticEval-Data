from typing import List

def compute_output_index(idx_1: int, idx_2: int) -> int:
    idx_1_bits = [int(x) for x in bin(idx_1)[2:]][::-1]
    idx_2_bits = [int(x) for x in bin(idx_2)[2:]][::-1]
    
    max_len = max(len(idx_1_bits), len(idx_2_bits))
    idx_1_bits += [0] * (max_len - len(idx_1_bits))
    idx_2_bits += [0] * (max_len - len(idx_2_bits))
    
    result_bits = [bit1 ^ bit2 for bit1, bit2 in zip(idx_1_bits, idx_2_bits)]
    
    result = sum([bit * 2**i for i, bit in enumerate(result_bits)])
    
    return result
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