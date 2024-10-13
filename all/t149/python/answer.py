def hsl_to_rgb(hue: float, saturation: float, lightness: float) -> dict:
    """
    Converts an HSL color value to RGB.
    Assumes hue is in [0, 360] and saturation, lightness are in [0, 1]
    and returns r, g, and b in the set [0, 255].

    :param hue: The hue of the color (0-360)
    :param saturation: The saturation of the color (0-1)
    :param lightness: The lightness of the color (0-1)
    :return: A dictionary containing the red, green, and blue channels.
    """
    
    # Initialize r, g, b
    if saturation == 0:
        # Achromatic case (saturation = 0), r, g, and b are the same.
        r = g = b = lightness
    else:
        # Chromatic case (saturation != 0)
        def hue_to_rgb(p: float, q: float, t: float) -> float:
            if t < 0:
                t += 1
            if t > 1:
                t -= 1
            if t < 1 / 6:
                return p + (q - p) * 6 * t
            if t < 1 / 2:
                return q
            if t < 2 / 3:
                return p + (q - p) * (2 / 3 - t) * 6
            return p

        q = lightness * (1 + saturation) if lightness < 0.5 else lightness + saturation - lightness * saturation
        p = 2 * lightness - q
        r = hue_to_rgb(p, q, hue / 360 + 1 / 3)
        g = hue_to_rgb(p, q, hue / 360)
        b = hue_to_rgb(p, q, hue / 360 - 1 / 3)

    # Convert r, g, b from [0,1] range to [0,255] range
    return {
        'r': round(r * 255),
        'g': round(g * 255),
        'b': round(b * 255)
    }