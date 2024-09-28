def convert_score_to_decimal(score_str):
    """
    Converts the string representation of a score to its decimal value.

    :param score_str: The score as a string, can be a decimal or a fraction (e.g., "2.5", "10/4")
    :return: The decimal value of the score as a float, or None if the input is invalid
    """
    try:
        # Check if the score is a fraction
        if '/' in score_str:
            numerator, denominator = score_str.split('/')
            decimal_value = float(numerator) / float(denominator)
        else:
            # Otherwise, treat it as a decimal
            decimal_value = float(score_str)

        return decimal_value

    except (ValueError, ZeroDivisionError) as e:
        print(f"Error converting '{score_str}' to decimal: {e}")
        return None
