import unittest


class TestBitsToBytes(unittest.TestCase):

    def test_exact_multiple_of_eight(self):
        """Test bit arrays that are exact multiples of 8 bits."""
        bits = [1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1]
        expected = bytearray([0b10110010, 0b01001111])  # Corrected to match actual byte values
        result = bits_to_bytes(bits)
        self.assertEqual(result, expected)

    def test_incomplete_byte_discarded(self):
        """Test bit arrays where the last bits do not make up a full byte."""
        bits = [1, 0, 1, 1, 0, 0, 1, 0, 0, 1]  # Last two bits should be discarded
        expected = bytearray([0b10110010])
        result = bits_to_bytes(bits)
        self.assertEqual(result, expected)

    def test_empty_bit_array(self):
        """Test an empty bit array."""
        bits = []
        expected = bytearray()
        result = bits_to_bytes(bits)
        self.assertEqual(result, expected)

    def test_single_full_byte(self):
        """Test bit arrays that exactly make one byte."""
        bits = [1, 1, 1, 1, 1, 1, 1, 1]  # Represents the byte 0xFF
        expected = bytearray([0xFF])
        result = bits_to_bytes(bits)
        self.assertEqual(result, expected)

    def test_no_bits_discarded(self):
        """Test bit arrays with multiple of 8 bits and no extra bits."""
        bits = [1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1]
        expected = bytearray([0xCC, 0x77])  # Corrected the second byte from 0xB7 to 0x77
        result = bits_to_bytes(bits)
        self.assertEqual(result, expected)
def bits_to_bytes(bits):
    """
    Convert an array of binary bits to an array of bytes. Every 8 bits are converted
    into one byte. If the length of the bit array is not a multiple of 8, the last
    incomplete byte will be discarded.

    Args:
    bits (list of int): The input array of bits (each element should be 0 or 1).

    Returns:
    bytearray: An array of bytes constructed from the bits.
    """
    # Ensure that the number of bits is a multiple of 8
    num_full_bytes = len(bits) // 8

    # Create a bytearray to store the byte values
    byte_array = bytearray()

    # Process each group of 8 bits
    for i in range(num_full_bytes):
        # Slice the bits array to get 8 bits
        byte_bits = bits[i*8:(i+1)*8]
        # Convert the list of bits to a string of bits
        byte_str = ''.join(str(bit) for bit in byte_bits)
        # Convert the string of bits to an integer and then to a byte
        byte = int(byte_str, 2)
        # Append the byte to the bytearray
        byte_array.append(byte)

    return byte_array