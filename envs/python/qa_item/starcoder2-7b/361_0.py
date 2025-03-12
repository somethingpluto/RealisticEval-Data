import numpy as np

def simpsons_rule(a: float, b: float, n: int) -> float:
    if n <= 0 or n % 2 != 0:
        raise ValueError("n must be positive and even")

    x = np.linspace(a, b, n+1)
    y = np.array([np.sin(xi) for xi in x])  # replace this with your function

    h = (b - a) / n
    integral = h / 3 * (y[0] + y[-1] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-1:2]))

    return integral
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