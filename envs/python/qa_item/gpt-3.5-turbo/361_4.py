import math

def simpsons_rule(a: float, b: float, n: int) -> float:
    if n <= 0 or n % 2 != 0:
        raise ValueError("n must be a positive even integer")

    h = (b - a) / n
    x = [a + i * h for i in range(n+1)]
    fx = [function(x_i) for x_i in x]

    integral = fx[0] + fx[n]
    for i in range(1, n):
        w = 2 if i % 2 == 0 else 4
        integral += w * fx[i]

    return h / 3 * integral

def function(x: float) -> float:
    # Define the function here, for example:
    return x**2

# Additional functions or code can be added here.
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