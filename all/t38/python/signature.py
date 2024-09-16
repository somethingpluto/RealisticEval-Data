def rainbowHexGenerator(num_intermediates: int, include_endpoints=False):
    """
    generates a color spectrum list containing the main rainbow colors and the gradient colors between them. The function takes two parameters: num_intermediates specifies the number of intermediate colors to be generated between each two major colors;include_endpoints determines whether to add a gradient from the last color back to the first color at the end of the color spectrum
    Args:
        num_intermediates (int): The number of intermediate colors that need to be generated between each pair of main rainbow colors. If set to 0, no intermediate colors are generated, and only the original seven rainbow colors are returned. If set to a positive integer, the function generates a specified number of transition colors between adjacent colors, creating a smoother color gradient.

        include_endpoints (bool): Do you add a transition from the last color (purple) back to the first color (red) at the end of the spectrum


    Returns:
        The list contains a series of hexadecimal color codes that represent the colors of rainbows and the gradient colors between them

    """
