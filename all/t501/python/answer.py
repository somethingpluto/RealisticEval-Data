def convert_to_short_format(input_str):
    """
    Converts a string concatenated with underscores to a short format.

    :param input_str: The input string with segments separated by underscores.
    :return: A short format string derived from the first characters of each segment.
    """
    # Split the input string by underscores
    segments = input_str.split('_')

    # Extract the first character from each segment and join them
    short_format = ''.join(segment[0] for segment in segments)

    return short_format
