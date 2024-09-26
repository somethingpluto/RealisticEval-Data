def convert_bits_to_bytes(bits_array):
    """
    Converts an array of bits (0s and 1s) into an array of bytes.

    Parameters:
    bits_array (List[int]): A list of bits (0s and 1s) to be converted.

    Returns:
    List[int]: A list of bytes (each byte is an integer) constructed from the input bits.
    """

    # Initialize an empty list to store the resulting bytes
    bytes_array = []
    new_byte = 0  # This will hold the current byte being formed
    bit_count = 0  # Counter to track the number of bits processed

    # Iterate over each bit in the input bits_array
    for bit in bits_array:
        # If the current bit is 1, set the corresponding bit in new_byte
        if bit:
            new_byte |= 1 << (bit_count % 8)  # Using bitwise OR to set the bit

        bit_count += 1  # Increment the bit counter

        # Check if we have processed 8 bits (a complete byte)
        if bit_count % 8 == 0:
            # Append the constructed byte to the bytes_array
            bytes_array.append(new_byte)
            new_byte = 0  # Reset new_byte for the next byte

    # Handle any remaining bits that don't form a complete byte
    if bit_count % 8 != 0:
        bytes_array.append(new_byte)

    return bytes_array
import unittest


class TestConvertBitsToBytes(unittest.TestCase):
    def test_empty_input(self):
        """Test with an empty bit array."""
        self.assertEqual(convert_bits_to_bytes([]), [])

    def test_complete_byte(self):
        """Test with exactly one complete byte (8 bits)."""
        bits = [1, 0, 1, 0, 1, 1, 0, 1]  # Should produce byte 0b10101101 = 173
        self.assertEqual(convert_bits_to_bytes(bits), [173])

    def test_two_complete_bytes(self):
        """Test with two complete bytes (16 bits)."""
        bits = [1, 0, 1, 0, 1, 1, 0, 1,  # First byte: 0b10101101
                0, 1, 1, 0, 1, 0, 0, 1]  # Second byte: 0b01101001
        self.assertEqual(convert_bits_to_bytes(bits), [173, 105])

    def test_incomplete_byte(self):
        """Test with bits that do not complete a byte."""
        bits = [1, 0, 1, 0, 1, 1, 0]  # 7 bits, should produce one byte and an incomplete byte
        self.assertEqual(convert_bits_to_bytes(bits), [173])  # 0b10101101 = 173, remaining 0b0000000

    def test_mixed_bits(self):
        """Test with a mixed array of bits (not forming complete bytes)."""
        bits = [1, 1, 0, 0, 1, 1, 1, 0,  # First byte: 0b11001110 = 206
                0, 0, 1]  # Incomplete byte: 0b00000001 = 1
        self.assertEqual(convert_bits_to_bytes(bits), [206, 1])

if __name__ == '__main__':
    unittest.main()