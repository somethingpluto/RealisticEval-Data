def rgb_to_hsl(r: int, g: int, b: int) -> dict:
    # Check if RGB values are within the valid range
    if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
        raise ValueError('Invalid RGB value. Each value must be between 0 and 255.')

    # Normalize RGB values to the range [0, 1]
    r /= 255
    g /= 255
    b /= 255

    # Calculate max and min of the normalized RGB values
    max_val = max(r, g, b)
    min_val = min(r, g, b)

    # Initialize H, S, L values
    h = s = 0
    l = (max_val + min_val) / 2

    # If max and min are not equal, calculate H and S
    if max_val != min_val:
        d = max_val - min_val
        s = d / (2 - max_val - min_val) if l > 0.5 else d / (max_val + min_val)

        # Calculate Hue
        if max_val == r:
            h = (g - b) / d + (6 if g < b else 0)
        elif max_val == g:
            h = (b - r) / d + 2
        elif max_val == b:
            h = (r - g) / d + 4

        h /= 6

    # Return HSL values, rounding H, S, and L to the nearest integer
    return {
        'h': round(h * 360),
        's': round(s * 100),
        'l': round(l * 100)
    }
