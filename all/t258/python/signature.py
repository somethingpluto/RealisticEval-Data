from typing import Tuple, List


def extract_character_bits(byte_array: bytes, char: str, charset='utf-8') -> Tuple[int, str]:
    """
    Extracts the position and bits of a specific character from a byte array.

    Args:
        byte_array (bytes): The byte array to search within
        char (str): The character to find in the byte array
        charset (str): The character encoding of the byte array

    Returns:
        A tuple of (position, bits) if the character is found, otherwise None.
    """
