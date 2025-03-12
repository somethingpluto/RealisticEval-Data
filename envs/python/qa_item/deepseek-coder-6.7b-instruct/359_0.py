def trapezoidal_rule(func, a: float, b: float, n: int) -> float:
    """
    Calculate the integral approximation of a given function on the interval [a, b] using the trapezoidal rule.

    Args:
        func (callable): The function to integrate, which takes a float and returns a float.
        a (float): The lower bound of the integration interval.
        b (float): The upper bound of the integration interval.
        n (int): The number of subintervals to use in the approximation (more intervals yield higher accuracy).

    Returns:
        float: The approximate value of the integral over the interval [a, b].
    """
    h = (b - a) / n  # Width of each subinterval
    integral = 0.5 * (func(a) + func(b))  # Initialize with the first and last terms

    for i in range(1, n):
        x_i = a + i * h
        integral += func(x_i)

    integral *= h  # Multiply by the width of each subinterval
    return integral
import unittest


class Tester(unittest.TestCase):
    def test_constant_function(self):
        """ Test Case 1: Integration of a constant function (f(x) = 1) over [0, 1] """
        self.assertAlmostEqual(trapezoidal_rule(lambda x: 1.0, 0.0, 1.0, 100), 1.0, delta=1e-6)

    def test_linear_function(self):
        """ Test Case 2: Integration of a linear function (f(x) = x) over [0, 1] """
        self.assertAlmostEqual(trapezoidal_rule(lambda x: x, 0.0, 1.0, 100), 0.5, delta=1e-6)

    def test_quadratic_function(self):
        """ Test Case 3: Integration of a quadratic function (f(x) = x^2) over [0, 1] """
        self.assertAlmostEqual(trapezoidal_rule(lambda x: x * x, 0.0, 1.0, 1000), 1.0 / 3.0, delta=1e-6)

    def test_sine_function(self):
        """ Test Case 4: Integration of the sine function (f(x) = sin(x)) over [0, π] """
        self.assertAlmostEqual(trapezoidal_rule(lambda x: math.sin(x), 0.0, math.pi, 1000), 2.0, delta=1e-6)

    def test_exponential_function(self):
        """ Test Case 5: Integration of an exponential function (f(x) = exp(x)) over [0, 1] """
        self.assertAlmostEqual(trapezoidal_rule(lambda x: math.exp(x), 0.0, 1.0, 1000), math.exp(1.0) - 1.0, delta=1e-6)

if __name__ == '__main__':
    unittest.main()