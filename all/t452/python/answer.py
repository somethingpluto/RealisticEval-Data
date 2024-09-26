def convert_bits_to_bytes(bits_array):
    """
    Converts an array of bits (0s and 1s) into an array of bytes.

    Parameters:
    bits_array (List[int]): A list of bits (0s and 1s) to be converted.

    Returns:
    List[int]: A list of bytes (each byte is an integer) constructed from the input bits.
    """

    # Initialize an empty list to store the resulting bytes
    bytes_array = []
    new_byte = 0  # This will hold the current byte being formed
    bit_count = 0  # Counter to track the number of bits processed

    # Iterate over each bit in the input bits_array
    for bit in bits_array:
        # If the current bit is 1, set the corresponding bit in new_byte
        if bit:
            new_byte |= 1 << (bit_count % 8)  # Using bitwise OR to set the bit

        bit_count += 1  # Increment the bit counter

        # Check if we have processed 8 bits (a complete byte)
        if bit_count % 8 == 0:
            # Append the constructed byte to the bytes_array
            bytes_array.append(new_byte)
            new_byte = 0  # Reset new_byte for the next byte

    # Handle any remaining bits that don't form a complete byte
    if bit_count % 8 != 0:
        bytes_array.append(new_byte)

    return bytes_array