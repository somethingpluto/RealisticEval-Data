import re

def is_background_too_dark_or_bright(computed_style):
    """Detecting the light or dark state of the background element and returning the corresponding description string.

    Args:
        computed_style (str): The computed background color in 'rgb(r, g, b)' format.

    Returns:
        str: "dark" if the background is too dark, "bright" if it is too bright, or "normal" if it is neither.
    """
    # Extract the background color as a string (assumed to be in 'rgb(r, g, b)' format)
    background_color = computed_style

    # Convert the background color to RGB components
    rgb = list(map(int, re.findall(r'\d+', background_color)))
    r, g, b = rgb

    # Calculate the perceived brightness using the formula
    brightness = (r * 299 + g * 587 + b * 114) / 1000

    # Define thresholds for darkness and brightness
    dark_threshold = 125
    bright_threshold = 200

    # Determine and return the background brightness level
    if brightness < dark_threshold:
        return "dark"
    elif brightness > bright_threshold:
        return "bright"
    else:
        return "normal"
