def sum_calibration_values(calibration_document):
    """
    Sums up calibration values extracted from the document.
    Each calibration value is formed by combining the first and last digits of numbers found in each line
    into a two-digit number.

    Args:
        calibration_document (iterable): An iterable of strings, each representing a line of text.

    Returns:
        int: The total sum of all calibration values.
    """
    total_sum = 0

    for line in calibration_document:
        # Filter out non-digit characters
        digits = [char for char in line if char.isdigit()]

        # Extract the first and last digits
        if digits:
            first_digit = int(digits[0])
            last_digit = int(digits[-1])

            # Combine to form a two-digit number
            calibration_value = first_digit * 10 + last_digit

            # Add to the total sum
            total_sum += calibration_value

    return total_sum