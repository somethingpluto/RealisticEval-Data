from typing import Optional

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

    def to_bitstring(n: int, width: Optional[int] = None) -> str:
        return format(n, 'b').zfill(width) if width else format(n, 'b')

    def from_bitstring(s: str) -> int:
        return int(s, 2)

    idx_1_bitstring = to_bitstring(idx_1)
    idx_2_bitstring = to_bitstring(idx_2)

    max_len = max(len(idx_1_bitstring), len(idx_2_bitstring))
    idx_1_bitstring = idx_1_bitstring.zfill(max_len)
    idx_2_bitstring = idx_2_bitstring.zfill(max_len)

    xor_result = ''.join(str(int(bit_1) ^ int(bit_2)) for bit_1, bit_2 in zip(idx_1_bitstring, idx_2_bitstring))

    return from_bitstring(xor_result)
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