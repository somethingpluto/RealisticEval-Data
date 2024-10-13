def binary_string_to_uint8_array(binary_str: str) -> bytearray:
    """
    Stores a second-level string in a set of 8-bit conversion integers in a bytearray and returns.

    Args:
        binary_str (str): The binary string to be converted.

    Returns:
        bytearray: The resulting bytearray containing the binary data.
    """
    # Calculate the number of bytes needed to represent the binary string
    byte_count = (len(binary_str) + 7) // 8  # Equivalent to Math.ceil(len(binary_str) / 8)
    byte_array = bytearray(byte_count)

    # Convert each 8-character segment of the binary string into a byte and store in byte_array
    for i in range(byte_count):
        byte_segment = binary_str[i * 8:(i + 1) * 8]  # Extract 8 characters
        byte_array[i] = int(byte_segment, 2)  # Convert binary segment to byte

    return byte_array
