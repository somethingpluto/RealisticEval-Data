import colorsys

def float2color(f, start_hue=0, end_hue=120, saturation=1.0, value=1.0):
    """
    Interpolate float to a color range using HSV.
    :param f: Input float in the range [0, 1]
    :param start_hue: Starting hue value (default 0 for red)
    :param end_hue: Ending hue value (default 120 for green)
    :param saturation: Saturation value of the color (default 1.0)
    :param value: Value of the color (default 1.0)
    """
    # Ensure the input is within the valid range [0, 1]
    f = max(0, min(1, f))

    # Calculate the hue within the specified range
    hue = (end_hue - start_hue) * f + start_hue

    # Convert the HSV color to RGB
    r, g, b = colorsys.hsv_to_rgb(hue/360, saturation, value)

    # Convert RGB to 8-bit integers and then to a hex string
    hex_color = "#{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255), int(b * 255))

    return hex_color
