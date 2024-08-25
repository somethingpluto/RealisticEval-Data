def extract_character_bits(byte_array: bytes, char: str, charset='utf-8') -> int:
    """
    given a character set, extract the position of a specific character from a byte array. First, determine whether the desired character exists in the character set, and if so, calculate the character's position in the byte array, and extract the character's bits
    Args:
        byte_array (bytes): The byte array to search within.
        char (str): The character to find in the byte array.
        charset (str): The character encoding of the byte array.

    Returns:
        The position if the character is found otherwise None
    """
