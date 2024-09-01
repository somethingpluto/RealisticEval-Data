from PIL import Image


def convert_image_to_bits(image_path):
    """
    Converts an image to a binary array representation.

    Args:
        image_path (str): The path to the image file.

    Returns:
        list: A list of bits (0 or 1) representing the image.
    """
    # Open the image using PIL
    image = Image.open(image_path)

    # Convert the image to black and white (1-bit pixels)
    image = image.convert('1')

    # Get the width and height of the image
    w, h = image.size

    # Initialize an empty list to store the bits
    bits_array = []

    # Loop over each pixel in the image
    for y in range(h):
        for x in range(w):
            # Get the pixel value (0 for black, 255 for white in '1' mode)
            pixel = image.getpixel((x, y))
            # Convert pixel to bit: 1 for white, 0 for black
            bit = 1 if pixel == 255 else 0
            bits_array.append(bit)

    return bits_array