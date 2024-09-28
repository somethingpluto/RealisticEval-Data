def convert_to_color_through_yellow(value):
    value *= 255

    # Determine the stage of interpolation
    if value <= 127.5:
        # Stage 1: Red to Yellow
        red = 255
        green = int(value) + 127.5  # Green increases from 0 to 255
        blue = 127.5
    else:
        # Stage 2: Yellow to Green
        red = int(255 - (value - 127.5))  # Red decreases from 255 to 0
        green = 255
        blue = 127.5

    return red, green, blue