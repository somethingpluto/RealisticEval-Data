def convert_range_to_color_yellow_green_change(value: float) -> tuple:
    """
    Convert a value in the range [0, 1] to an RGB color that transitions
    from red to yellow and then from yellow to green.

    Parameters:
        value (float): A float value in the range [0, 1] representing the
                       interpolation position.

    Returns:
        tuple: A tuple containing the RGB color values (red, green, blue).
    """

    # Scale the input value from the range [0, 1] to [0, 255]
