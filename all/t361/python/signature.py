def simpsons_rule(a: float, b: float, n: int) -> float:
    """
    Computes the approximate integral of a function using Simpson's Rule.

    Simpson's Rule is a method for numerical integration that approximates the integral of a function
    over an interval by fitting parabolas. This function divides the interval [a, b] into n subintervals
    and calculates the weighted sum of the function values at specific points.

    :param a: The lower limit of integration.
    :param b: The upper limit of integration.
    :param n: The number of subintervals (must be even).
    :return: The approximate value of the integral.

    :raises InvalidArgumentError: If n is not positive or if it is not even.
    """