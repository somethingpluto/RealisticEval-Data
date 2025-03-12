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

    def int_to_bitstring(num: int, length: int) -> List[int]:
        return [(num >> i) & 1 for i in range(length)]

    def bitstring_to_int(bits: List[int]) -> int:
        return sum(bit << i for i, bit in enumerate(bits))

    bits_1 = int_to_bitstring(idx_1, max(idx_1.bit_length(), idx_2.bit_length()))
    bits_2 = int_to_bitstring(idx_2, max(idx_1.bit_length(), idx_2.bit_length()))

    output_bits = [b1 ^ b2 for b1, b2 in zip(bits_1, bits_2)]

    return bitstring_to_int(output_bits)
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