def convert_range_to_color_yellow_green_change(value):
    """
    Convert a value in the range [0, 1] to an RGB color that transitions 
    from red to yellow and then from yellow to green.

    Parameters:
        value (float): A float value in the range [0, 1] representing the 
                       interpolation position.

    Returns:
        tuple: A tuple containing the RGB color values (red, green, blue).
    """
    
    # Scale the input value from the range [0, 1] to [0, 255]
    scaled_value = value * 255

    # Initialize RGB components
    red = 0
    green = 0
    blue = 127.5  # Blue component is fixed at 127.5 throughout

    # Determine the stage of interpolation based on the scaled value
    if scaled_value <= 127.5:
        # Stage 1: Transitioning from Red (255, 0, 127.5) to Yellow (255, 255, 127.5)
        red = 255  # Red component is fixed at 255
        # Green increases linearly from 127.5 to 255
        green = int(scaled_value) + 127.5  
    else:
        # Stage 2: Transitioning from Yellow (255, 255, 127.5) to Green (0, 255, 127.5)
        # Red decreases linearly from 255 to 0
        red = int(255 - (scaled_value - 127.5))  
        green = 255  # Green component is fixed at 255

    # Return the RGB color as a tuple
    return red, green, blue