def scale_to_range(input_array, input_min, input_max, output_min, output_max):
    """
    Scales the values in an array from one range to another.

    Parameters:
    input_array (list of float): The array of input values to be scaled.
    input_min (float): The minimum value in the input range.
    input_max (float): The maximum value in the input range.
    output_min (float): The minimum value in the output range.
    output_max (float): The maximum value in the output range.

    Returns:
    list of float: A new array with values scaled to the output range.

    Raises:
    ValueError: If any value in input_array is outside the range [input_min, input_max].
    """