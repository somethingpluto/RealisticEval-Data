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
    getcontext().prec = digits + 5  # Extra digits to ensure accuracy in calculations

    # Initial values
    a = Decimal(1)  # a_0
    b = Decimal(1) / Decimal(2).sqrt()  # b_0
    t = Decimal(1) / Decimal(4)  # t_0
    p = Decimal(1)  # p_0

    # Iterate to improve precision
    for _ in range(100):  # Sufficiently large number of iterations
        a_next = (a + b) / 2
        b = (a * b).sqrt()
        t -= p * (a - a_next) ** 2
        a = a_next
        p *= 2

    pi = (a + b) ** 2 / (4 * t)
    return str(pi)[:digits + 2]  # Return π with the requested number of digits