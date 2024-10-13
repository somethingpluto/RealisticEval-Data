def rgb_to_hsl(rgb: dict) -> dict:
    """
    Converts RGB color values to HSL (Hue, Saturation, Lightness) color values.
    The input RGB values should be in the range of 0 to 255, and the output HSL values will have:
    - `h` (Hue) in the range of 0 to 360,
    - `s` (Saturation) in the range of 0 to 100 (percentage),
    - `l` (Lightness) in the range of 0 to 100 (percentage).

    :param rgb: The RGB color values.
    :type rgb: dict
    :param rgb['r']: The red color value (0-255).
    :type rgb['r']: int
    :param rgb['g']: The green color value (0-255).
    :type rgb['g']: int
    :param rgb['b']: The blue color value (0-255).
    :type rgb['b']: int
    :return: A dictionary representing the HSL color values.
    :rtype: dict
    :return h: The hue value (0-360).
    :rtype: int
    :return s: The saturation value (0-100).
    :rtype: int
    :return l: The lightness value (0-100).
    """
    pass  # Implementation goes here