if not isinstance(port, int):
        raise TypeError("Port number must be an integer.")
    return 1 <= port <= 65535
import unittest


class TestIsValidPortNumber(unittest.TestCase):

    def test_valid_port_number_middle(self):
        """Returns true for a valid port number in the middle of the range."""
        self.assertTrue(is_valid_port_number(8080))

    def test_lowest_valid_port_number(self):
        """Returns true for the lowest valid port number."""
        self.assertTrue(is_valid_port_number(1))

    def test_highest_valid_port_number(self):
        """Returns true for the highest valid port number."""
        self.assertTrue(is_valid_port_number(65535))

    def test_below_valid_range(self):
        """Returns false for a port number below the valid range."""
        self.assertFalse(is_valid_port_number(0))

    def test_above_valid_range(self):
        """Returns false for a port number above the valid range."""
        self.assertFalse(is_valid_port_number(65536))

if __name__ == '__main__':
    unittest.main()