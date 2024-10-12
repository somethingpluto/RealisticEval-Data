from decimal import Decimal, getcontext


def compute_pi(digits: int) -> str:
    """
    Computing PI (π) Using Gauss-Legendre Algorithm with High-precision Arithmetic Library.

    Args:
        digits (int): The number of decimal digits to compute π to.

    Returns:
        str: The value of π to the specified number of digits.
    """
    # Set the precision for Decimal calculations
    getcontext().prec = digits + 10  # Extra precision to ensure accuracy
    one = Decimal(1)
    two = Decimal(2)
    four = Decimal(4)

    # Initialize variables
    a = one
    b = one / two ** 0.5  # b0 = 1 / sqrt(2)
    t = one / four  # t0 = 1/4
    p = one
    prev_pi = Decimal(0)
    pi = None

    # Iterate until the desired precision is reached
    for _ in range(10):
        a_next = (a + b) / two
        b_next = (a * b) ** 0.5
        diff = a - a_next
        t_next = t - (p * diff ** 2)
        p_next = p * two
        a, b, t, p = a_next, b_next, t_next, p_next

        pi = (a + b) ** 2 / (t * four)

        # Check if the desired precision has been reached
        if pi == prev_pi:
            break

        prev_pi = pi

    # Return π to the specified number of digits
    return str(pi.quantize(Decimal(10) ** -digits))  # Format to required precision