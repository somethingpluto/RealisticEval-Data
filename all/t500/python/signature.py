def convert_score_to_decimal(score_str: str) -> float:
    """
    Converts the string representation of a score to its decimal value.
    For example:
        input: 10/4
        output: 2.5
    Args:
        score_str (str): The score as a string, can be a decimal or a fraction

    Returns:
        float: The decimal value of the score as a float, or None if the input is invalid
    """
