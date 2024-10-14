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