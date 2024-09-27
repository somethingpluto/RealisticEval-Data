def convert_bits_to_bytes(bits_array):
    """
    Converts an array of bits (0s and 1s) into an array of bytes.

    Args:
        bits_array (list): A list of bits (0s and 1s) to convert.

    Returns:
        list: A list of bytes represented as integers.
    """
    bytes_array = []   # Initialize an empty list to store the resulting bytes
    current_byte = 0   # Variable to build the current byte
    bit_count = 0      # Counter for the number of bits processed

    for bit in bits_array:
        # Set the corresponding bit in the current byte if the bit is 1
        if bit:
            current_byte |= 1 << (bit_count % 8)  # Use bitwise OR to set the bit

        bit_count += 1  # Increment the bit counter

        # When 8 bits have been processed, save the current byte
        if bit_count % 8 == 0:
            bytes_array.append(current_byte)  # Append the completed byte
            current_byte = 0  # Reset for the next byte

    # Handle any remaining bits that do not form a complete byte
    if bit_count % 8 != 0:
        bytes_array.append(current_byte)  # Append the last byte if not empty

    return bytes_array
