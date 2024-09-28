def hex_to_ansi(hex_color):
    """
    Convert a hexadecimal color code to an ANSI escape code.

    Parameters:
    hex_color (str): A string representing the hexadecimal color code, e.g., '#FF5733'.

    Returns:
    str: An ANSI escape code for the specified RGB color.
    """

    # Check if the input is a valid hex color
    if len(hex_color) != 7 or hex_color[0] != '#':
        raise ValueError("Invalid hex color format. Use '#RRGGBB'.")

    # Extract the red, green, and blue components from the hex string
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)

    # Create the ANSI escape code
    ansi_code = f"\x1b[38;2;{r};{g};{b}m"

    return ansi_code