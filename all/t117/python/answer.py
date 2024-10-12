def rgb_to_hsl(r, g, b):
    # Convert RGB to the [0, 1] range
    r /= 255
    g /= 255
    b /= 255

    max_val = max(r, g, b)
    min_val = min(r, g, b)

    # Initialize HSL values
    h, s, l = 0, 0, (max_val + min_val) / 2

    if max_val == min_val:
        h = s = 0  # Achromatic
    else:
        d = max_val - min_val
        s = d / (2 - max_val - min_val) if l > 0.5 else d / (max_val + min_val)

        if max_val == r:
            h = (g - b) / d + (6 if g < b else 0)
        elif max_val == g:
            h = (b - r) / d + 2
        elif max_val == b:
            h = (r - g) / d + 4

        h /= 6

    # Convert hue to degrees
    h = round(h * 360)
    # Convert saturation and lightness to percentage
    s = round(s * 100)
    l = round(l * 100)

    return {'h': h, 's': s, 'l': l}
