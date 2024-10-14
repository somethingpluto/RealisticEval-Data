def rgb_to_hsl(rgb: dict) -> dict:
    """
    Converts RGB color values to HSL (Hue, Saturation, Lightness) color values.

    The input RGB values should be in the range of 0 to 255, and the output HSL values will have:
    - `h` (Hue) in the range of 0 to 360,
    - `s` (Saturation) in the range of 0 to 100 (percentage),
    - `l` (Lightness) in the range of 0 to 100 (percentage).

    Args:
        rgb (dict): The RGB color values.
            - rgb['r'] (int): The red color value (0-255).
            - rgb['g'] (int): The green color value (0-255).
            - rgb['b'] (int): The blue color value (0-255).

    Returns:
        dict: A dictionary representing the HSL color values.
            - h (int): The hue value (0-360).
            - s (int): The saturation value (0-100).
            - l (int): The lightness value (0-100).
    """