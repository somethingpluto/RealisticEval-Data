def float_to_rgb(value: float) -> tuple:
    """
    Convert a floating-point number between 0 and 1 to a color from red to green in RGB format.

    :param value: A float between 0 and 1.
    :return: A tuple representing the RGB color.
    """
    if not (0.0 <= value <= 1.0):
        raise ValueError("Value must be between 0 and 1 inclusive.")

    # Calculate the red and green components
    red = int((1.0 - value) * 255)
    green = int(value * 255)

    # Blue component is always 0 for the red-to-green gradient
    blue = 0

    return (red, green, blue)