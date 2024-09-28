def convert_to_color_through_yellow(value):
    """
    Converts a normalized value (0 to 1) to an RGB color transitioning
    from red to yellow and then from yellow to green.

    :param value: A float value between 0 and 1.
    :return: A tuple containing the RGB values (red, green, blue).
    """

    # Scale the value to 0-255 range
    scaled_value = value * 255

    # Initialize RGB values
    red, green, blue = 0, 0, 0

    # Determine the stage of interpolation
    if scaled_value <= 127.5:
        # Stage 1: Red to Yellow
        red = 255
        green = int(scaled_value) + 127  # Green increases from 127 to 255
        blue = 0  # Blue remains 0
    else:
        # Stage 2: Yellow to Green
        red = int(255 - (scaled_value - 127.5) * 2)  # Red decreases from 255 to 0
        green = 255  # Green remains at 255
        blue = 0  # Blue remains 0

    return red, green, blue
