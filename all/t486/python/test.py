import unittest


class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Create an instance of Calculator before each test."""
        self.calculator = Calculator()

    def test_add(self):
        """Test the addition method."""
        result = self.calculator.add(10, 5)
        self.assertEqual(result, 15)

    def test_subtract(self):
        """Test the subtraction method."""
        result = self.calculator.subtract(10, 5)
        self.assertEqual(result, 5)

    def test_multiply(self):
        """Test the multiplication method."""
        result = self.calculator.multiply(10, 5)
        self.assertEqual(result, 50)

    def test_divide(self):
        """Test the division method."""
        result = self.calculator.divide(10, 5)
        self.assertEqual(result, 2.0)

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calculator.divide(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero.")