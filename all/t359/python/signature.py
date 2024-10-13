def trapezoidal_rule(func, a: float, b: float, n: int) -> float:
    """
    Calculate the integral approximation of a given function on a given interval [a,b] using the trapezoidal rule of numerical integration.

    :param func: The function to integrate, represented as a callable that takes a float and returns a float.
    :param a: The lower bound of the integration interval.
    :param b: The upper bound of the integration interval.
    :param n: The number of subintervals to use in the approximation (more intervals yield higher accuracy).
    :return: The approximate value of the integral over the interval [a, b].
    """