def find_tempo(pixels):
    anger_value = 0
    for pixel in pixels:
        red = pixel[0]
        blue = pixel[1]
        green = pixel[2]
        # so if pixel is "angry"
        if red > (green+blue)/2:
            anger_value += red
        else:
            anger_value -= (green+blue)/2
    # Define the range of values to transform to.

    # below lines are generated through chatgpt
    if anger_value == 0:
        transformed_anger = 120
    elif anger_value < 0:
        # Normalize negative anger_value to the range of -255 to 0 for a single pixel.
        # For all pixels, it would be -255 * len(pixels) to 0.
        max_negative_anger = -255 * len(pixels)
        # Normalize and then linearly map it to the range 60-100.
        normalized_anger = (anger_value - max_negative_anger) / (-max_negative_anger) * 40 + 60
        # Find the closest value in the anger_range to the normalized_anger.
        transformed_anger = min([60, 70, 80, 90,100], key=lambda x: abs(x - normalized_anger))
    else:
        # Positive anger_value: Normalize to the range 0 to 255 for a single pixel.
        # For all pixels, it would be 0 to 255 * len(pixels).
        max_positive_anger = 255 * len(pixels)
        # Normalize and then linearly map it to the range 120-180.
        normalized_anger = (anger_value / max_positive_anger) * 60 + 120
        # Find the closest value in the anger_range to the normalized_anger.
        transformed_anger = min([120,130,140, 150,160, 170,180], key=lambda x: abs(x - normalized_anger))

    return transformed_anger