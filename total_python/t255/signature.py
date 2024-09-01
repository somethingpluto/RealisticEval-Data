from typing import List


def convert_image_to_bits(image_path: str) -> List:
    """
    Convert a picture to an array of binary bits. Convert it to black and white mode (only 0s and 1s, corresponding to black and white), convert the white pixel (value 255) to 1, convert the black pixel to 0, and finally store these bits in an array and return


    Args:
        image_path (str): The path to the image file.

    Returns:
        list: A list of bits (0 or 1) representing the image.
    """
