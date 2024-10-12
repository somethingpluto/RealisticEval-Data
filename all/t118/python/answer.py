def hsl_to_rgb(h: int, s: int, l: int) -> dict:
    """
    Converts HSL color values to RGB.

    Args:
        h (int): Hue (0-360 degrees).
        s (int): Saturation (0-100%).
        l (int): Lightness (0-100%).

    Returns:
        dict: A dictionary containing the RGB values.
    """
    # Convert saturation and lightness to the range of [0, 1]
    s /= 100
    l /= 100
    c = (1 - abs(2 * l - 1)) * s  # Chroma
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = l - c / 2

    r, g, b = 0, 0, 0

    if 0 <= h < 60:
        r, g, b = c, x, 0
    elif 60 <= h < 120:
        r, g, b = x, c, 0
    elif 120 <= h < 180:
        r, g, b = 0, c, x
    elif 180 <= h < 240:
        r, g, b = 0, x, c
    elif 240 <= h < 300:
        r, g, b = x, 0, c
    elif 300 <= h < 360:
        r, g, b = c, 0, x

    # Convert the RGB components to 0 - 255 range
    r = round((r + m) * 255)
    g = round((g + m) * 255)
    b = round((b + m) * 255)

    return {'r': r, 'g': g, 'b': b}
