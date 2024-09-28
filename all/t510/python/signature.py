def find_powers(num: int) -> tuple:
    """
    Find the powers of 2 and 3 that multiply to produce the given number.

    Args:
        num (int): A positive integer greater than zero.

    Returns:
        tuple: A tuple (n, m) where n is the power of 2 and m is the power of 3.
           Returns None if the number is zero or if the number has prime factors other than 2 and 3.
    """
