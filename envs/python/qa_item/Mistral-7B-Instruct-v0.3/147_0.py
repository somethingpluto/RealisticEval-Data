import codecs

def array_buffer_to_string(buffer: bytes) -> str:
    """
    Converts an ArrayBuffer to a string.
    Args:
        buffer (bytes): The bytes object to be converted.

    Returns:
        str: The string representation of the bytes object.
    """
    return codecs.decode(buffer, 'utf-8', 'ignore')
import unittest


class TestArrayBufferToString(unittest.TestCase):

    def test_empty_buffer(self):
        """Should return an empty string for an empty bytes object."""
        buffer1 = bytes()  # Equivalent to an empty ArrayBuffer
        result = array_buffer_to_string(buffer1)
        self.assertEqual(result, '')  # Expected: ""

    def test_single_character_a(self):
        """Should return 'A' for a buffer containing the character 'A'."""
        buffer2 = b'A'  # Directly using bytes to represent 'A'
        result = array_buffer_to_string(buffer2)
        self.assertEqual(result, 'A')  # Expected: "A"

    def test_string_hello(self):
        """Should return 'Hello' for a buffer containing the string 'Hello'."""
        buffer3 = b'Hello'  # Directly using bytes to represent 'Hello'
        result = array_buffer_to_string(buffer3)
        self.assertEqual(result, 'Hello')  # Expected: "Hello"

    def test_multiple_characters(self):
        """Should return the correct string for a buffer containing multiple characters."""
        buffer4 = b'Hello, World!'  # Directly using bytes to represent the string
        result = array_buffer_to_string(buffer4)
        self.assertEqual(result, 'Hello, World!')  # Expected: "Hello, World!"

    def test_input_buffer_not_modified(self):
        """Should not modify the input buffer."""
        input_string = "Test input"
        buffer8 = input_string.encode('utf-8')  # Encode the input string to bytes
        array_buffer_to_string(buffer8)  # Call the function
        result = buffer8.decode('utf-8')  # Decode the buffer to check its content
        self.assertEqual(result, input_string)  # Check if the buffer content remains unchanged
if __name__ == '__main__':
    unittest.main()