def sum_calibration_values(calibration_document) -> int:
    """
    Sums up calibration values extracted from the document.
    Each calibration value is formed by combining the first and last digits of numbers found in each line
    into a two-digit number.

    Args:
        calibration_document (iterable): An iterable of strings, each representing a line of text.

    Returns:
        int: The total sum of all calibration values.
    """
