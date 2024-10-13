class Tester(unittest.TestCase):
    """Test cases for the return_string function."""

    def test_non_empty_string(self):
        """Test Case 1: Copy a non-empty string."""
        original = "Hello, World!"
        copy = return_string(original)
        self.assertEqual(copy, original)

    def test_empty_string(self):
        """Test Case 2: Copy an empty string."""
        original = ""
        copy = return_string(original)
        self.assertEqual(copy, original)

    def test_special_characters(self):
        """Test Case 3: Copy a string with special characters."""
        original = "C++ is fun! @#$%^&*()"
        copy = return_string(original)
        self.assertEqual(copy, original)

    def test_single_character_string(self):
        """Test Case 4: Copy a single character string."""
        original = "A"
        copy = return_string(original)
        self.assertEqual(copy, original)

    def test_null_pointer(self):
        """Test Case 5: Passing a None (should raise an exception)."""
        with self.assertRaises(InvalidArgumentError):
            return_string(None)
