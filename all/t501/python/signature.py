def convert_to_short_format(input_str) -> str:
    """
    Converts a string concatenated with underscores to a short format.
    For example:
        input: f1_p1_g1_b1_c1
        output: fpgbc
    Args:
        input_str (str): The input string with segments separated by underscores.

    Returns:
        str: A short format string derived from the first characters of each segment.
    """
