def mod_exp(base, exponent, modulus):
    """
    Perform modular exponentiation: (base^exponent) % modulus efficiently.

    Parameters:
    base (int): The base value.
    exponent (int): The exponent value (should be non-negative).
    modulus (int): The modulus value (should be positive).

    Returns:
    int: The result of (base^exponent) % modulus.

    Raises:
    ValueError: If modulus is less than or equal to zero.
    """

    if modulus <= 0:
        raise ValueError("Modulus must be a positive integer.")

    result = 1
    base = base % modulus  # Ensure base is within the modulus

    while exponent > 0:
        # If exponent is odd, multiply the base with the result
        if exponent % 2 == 1:
            result = (result * base) % modulus

        # Right shift the exponent by 1 (equivalent to exponent //= 2)
        exponent //= 2
        # Square the base
        base = (base * base) % modulus

    return result