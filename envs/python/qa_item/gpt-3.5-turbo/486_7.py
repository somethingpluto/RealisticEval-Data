class Calculator:
    def add(self, a: float, b: float) -> float:
        """
        Returns the sum of a and b.
        """
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """
        Returns the difference of a and b.
        """
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """
        Returns the product of a and b.
        """
        return a * b

    def divide(self, a: float, b: float) -> float:
        """
        Returns the quotient of a and b.
        Raises ValueError if b is zero.
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b
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
        self.assertRaises(Exception)
if __name__ == '__main__':
    unittest.main()