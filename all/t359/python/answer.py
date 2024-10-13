from typing import Callable

def trapezoidal_rule(func: Callable[[float], float], a: float, b: float, n: int) -> float:
    """
    Calculate the integral approximation of a given function on a given interval [a,b] using the trapezoidal rule.

    This function calculates the integral approximation of a given mathematical function over
    the interval [a, b] using the trapezoidal rule of numerical integration. The interval is divided
    into a specified number of subintervals, and the area under the curve is approximated by trapezoids.

    :param func: The function to integrate, represented as a callable that takes a float and returns a float.
    :param a: The lower bound of the integration interval.
    :param b: The upper bound of the integration interval.
    :param n: The number of subintervals to use in the approximation (more intervals yield higher accuracy).
    :return: The approximate value of the integral over the interval [a, b].
    """
    if n <= 0:
        raise ValueError("Number of subintervals must be greater than 0.")

    h = (b - a) / n  # Step size
    integral = 0.5 * (func(a) + func(b))  # Initial trapezoid (half end heights)

    for i in range(1, n):
        integral += func(a + i * h)

    integral *= h
    return integral