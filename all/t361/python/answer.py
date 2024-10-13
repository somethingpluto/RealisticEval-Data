class InvalidArgumentError(Exception):
    """Custom exception for invalid arguments."""
    pass


def function_to_integrate(x: float) -> float:
    """Computes the value of the function to integrate."""
    return x * x


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
    # Check if n is a positive even integer
    if n <= 0 or n % 2 != 0:
        raise InvalidArgumentError("n must be a positive even integer.")

    # Calculate the width of each subinterval
    h = (b - a) / n
    sum_value = 0.0

    # Calculate the weighted sum of the function values
    for idx in range(n + 1):  # range(n + 1) to include n
        x = a + idx * h  # Calculate the x value at the current index
        fx = function_to_integrate(x)  # Evaluate the function at x

        # Apply the Simpson's Rule weighting
        if idx == 0 or idx == n:  # First and last terms (f(a) and f(b))
            sum_value += fx
        elif idx % 2 == 1:  # Odd index terms (4 * f(a + b))
            sum_value += 4.0 * fx
        else:  # Even index terms (2 * f(a + b))
            sum_value += 2.0 * fx

    # Final calculation to obtain the integral value
    return (h / 3.0) * sum_value  # Simpson's Rule formula
