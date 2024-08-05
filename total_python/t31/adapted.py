def calculate_anger_level(color_values):
    total_anger = 0
    num_pixels = len(color_values)
    for color in color_values:
        r, g, b = color
        if r > (g + b) / 2:
            total_anger += r
        else:
            total_anger -= (g + b) / 2

    if total_anger == 0:
        return 120
    elif total_anger < 0:
        return map_negative_anger(total_anger, num_pixels)
    else:
        return map_positive_anger(total_anger, num_pixels)

def map_negative_anger(anger, num_pixels):
    min_anger = -255 * num_pixels
    normalized_anger = (anger - min_anger) / (-min_anger) * 40 + 60
    return find_nearest([60, 70, 80, 90, 100], normalized_anger)

def map_positive_anger(anger, num_pixels):
    max_anger = 255 * num_pixels
    normalized_anger = (anger / max_anger) * 60 + 120
    return find_nearest([120, 130, 140, 150, 160, 170, 180], normalized_anger)

def find_nearest(options, value):
    return min(options, key=lambda x: abs(x - value))

