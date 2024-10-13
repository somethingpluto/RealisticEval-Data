import math

def abbreviate_number(number: float) -> str:
    """
    Abbreviates a number to a string with a suffix based on its magnitude.

    :param number: The number to abbreviate.
    :return: The abbreviated string representation of the number.
    """
    # If the number is less than 1000, return it as is.
    if number < 1000:
        return str(number)

    # Determine the tier of the number based on its magnitude.
    tier = math.floor(math.log10(number) / 3)

    # Define suffixes for each tier.
    suffixes = ["", "k", "M", "B", "T"]

    # Calculate the base number by dividing by the corresponding power of ten.
    base_number = number / (10 ** (tier * 3))

    # Round the base number to one decimal place.
    rounded_number = round(base_number, 1)

    # Return the number with its corresponding suffix.
    return f"{rounded_number}{suffixes[tier]}"