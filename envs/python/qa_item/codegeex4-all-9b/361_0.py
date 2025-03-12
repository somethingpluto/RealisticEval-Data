def simpsons_rule(a: float, b: float, n: int) -> float:
    """
    Computes the approximate integral of a function using Simpson's Rule.

    Simpson's Rule is a method for numerical integration that approximates the integral of a function
    over an interval by fitting parabolas. This function divides the interval [a, b] into n subintervals
    and calculates the weighted sum of the function values at specific points.

    Args:
        a (float): The lower limit of integration.
        b (float): The upper limit of integration.
        n (int): The number of subintervals (must be even).

    Returns:
        float: The approximate value of the integral.

    Raises:
        ValueError: If n is not positive or if it is not even.
    """
    if n <= 0 or n % 2 != 0:
        raise ValueError("n must be a positive even integer")

    h = (b - a) / n
    integral = f(a) + f(b)

    for i in range(1, n, 2):
        integral += 4 * f(a + i * h)

    for i in range(2, n, 2):
        integral += 2 * f(a + i * h)

    return integral * h / 3

def f(x):
    # Define the function to integrate here
    return x**2  # Example function: f(x) = x^2

# Example usage:
# result = simpsons_rule(0, 1, 10)
# print(result)
import unittest


class Tester(unittest.TestCase):
    """Tests for Simpson's Rule implementation."""

    def test_basic_integral_0_to_1(self):
        """Test the integral of f(x) = x^2 from 0 to 1."""
        # The exact integral of f(x) = x^2 from 0 to 1 is 1/3
        result = simpsons_rule(0.0, 1.0, 10)
        self.assertAlmostEqual(result, 1.0 / 3.0, delta=0.01)

    def test_basic_integral_0_to_2(self):
        """Test the integral of f(x) = x^2 from 0 to 2."""
        # The exact integral of f(x) = x^2 from 0 to 2 is 8/3
        result = simpsons_rule(0.0, 2.0, 10)
        self.assertAlmostEqual(result, 8.0 / 3.0, delta=0.01)

    def test_negative_integral_minus1_to_0(self):
        """Test the integral of f(x) = x^2 from -1 to 0."""
        # The exact integral of f(x) = x^2 from -1 to 0 is 1/3
        result = simpsons_rule(-1.0, 0.0, 10)
        self.assertAlmostEqual(result, 1.0 / 3.0, delta=0.01)

    def test_large_interval_0_to_10(self):
        """Test the integral of f(x) = x^2 from 0 to 10."""
        # The exact integral from 0 to 10 of f(x) = x^2 is (10^3)/3 = 1000/3
        result = simpsons_rule(0.0, 10.0, 20)
        self.assertAlmostEqual(result, 1000.0 / 3.0, delta=0.01)

if __name__ == '__main__':
    unittest.main()