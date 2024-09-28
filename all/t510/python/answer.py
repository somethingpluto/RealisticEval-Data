def find_powers(num):
    """
    Find the powers of 2 and 3 that multiply to produce the given number.

    Parameters:
    num (int): A positive integer greater than zero.

    Returns:
    tuple: A tuple (n, m) where n is the power of 2 and m is the power of 3.
           Returns None if the number is zero or if the number has prime factors other than 2 and 3.
    """

    # Input validation
    if num <= 0:
        raise ValueError("Input must be a positive integer greater than zero.")

    n, m = 0, 0  # Initialize counters for powers of 2 and 3

    # Count the power of 2 in the factorization
    while num % 2 == 0:
        n += 1
        num //= 2

    # Count the power of 3 in the factorization
    while num % 3 == 0:
        m += 1
        num //= 3

    # If num is reduced to 1, only 2's and 3's were factors
    if num == 1:
        return n, m
    else:
        return None  # Return None if there are other prime factors