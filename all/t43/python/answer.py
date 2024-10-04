def rgb_to_hsv(r, g, b):
    # Normalize the RGB values by dividing by 255
    r, g, b = r / 255.0, g / 255.0, b / 255.0

    # Find the minimum and maximum values among R, G, and B
    max_rgb = max(r, g, b)
    min_rgb = min(r, g, b)
    delta = max_rgb - min_rgb

    # Calculate H (Hue)
    if delta == 0:
        h = 0
    elif max_rgb == r:
        h = ((g - b) / delta) % 6
    elif max_rgb == g:
        h = ((b - r) / delta) + 2
    else:
        h = ((r - g) / delta) + 4

    h *= 60  # Convert to degrees on the color circle

    # Calculate S (Saturation)
    if max_rgb == 0:
        s = 0
    else:
        s = delta / max_rgb

    # V (Value) is equal to max_rgb
    v = max_rgb

    return (h, s*100, v*100)
