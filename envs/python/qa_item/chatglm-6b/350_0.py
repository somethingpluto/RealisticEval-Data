
def byte_array_to_hex_string(byte_array: bytes) -> str:
    """
    Converts a byte array into its corresponding hexadecimal string representation.

    Args:
        byte_array (bytes): An array of bytes to be converted into a hexadecimal string.

    Returns:
        str: A string representing the hexadecimal values of the bytes in the input array.If the input array is empty, returns an empty string.
    """
    if not byte_array:
        return ""
    
    hex_values = []
    for b in byte_array:
        hex_values.append(str(b).encode("hex"))
    
    return "".join(hex_values)

import unittest


class TestAnswer(unittest.TestCase):

    def test_empty_byte_array(self):
        input_data = bytes()  # Empty byte array
        self.assertEqual("", byte_array_to_hex_string(input_data), "Empty array should return empty string")

    def test_single_byte(self):
        input_data = bytes([0x0F])  # 15 in decimal
        result = byte_array_to_hex_string(input_data)
        self.assertTrue(result in ["0F", "0f"])

    def test_multiple_bytes(self):
        input_data = bytes([0x01, 0x0A, 0xFF])
        result = byte_array_to_hex_string(input_data)
        self.assertTrue(result in ["010aff", "010AFF"])

    def test_zero_bytes(self):
        input_data = bytes([0x00, 0x00, 0x00])
        self.assertEqual("000000", byte_array_to_hex_string(input_data), "Zero bytes should be converted to '000000'")

    def test_negative_bytes(self):
        input_data = bytes([0x80, 0xFF])  # 128 and 255 in signed byte representation
        result = byte_array_to_hex_string(input_data)
        self.assertTrue(result in ["80FF", "80ff"])
if __name__ == '__main__':
    unittest.main()