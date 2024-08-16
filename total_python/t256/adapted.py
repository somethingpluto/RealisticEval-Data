def bits_to_bytes(bits):
    """
    Convert an array of binary bits to an array of bytes. Every 8 bits are converted
    into one byte. If the length of the bit array is not a multiple of 8, the last
    incomplete byte will be discarded.

    Args:
    bits (list of int): The input array of bits (each element should be 0 or 1).

    Returns:
    bytearray: An array of bytes constructed from the bits.
    """
    # Ensure that the number of bits is a multiple of 8
    num_full_bytes = len(bits) // 8

    # Create a bytearray to store the byte values
    byte_array = bytearray()

    # Process each group of 8 bits
    for i in range(num_full_bytes):
        # Slice the bits array to get 8 bits
        byte_bits = bits[i*8:(i+1)*8]
        # Convert the list of bits to a string of bits
        byte_str = ''.join(str(bit) for bit in byte_bits)
        # Convert the string of bits to an integer and then to a byte
        byte = int(byte_str, 2)
        # Append the byte to the bytearray
        byte_array.append(byte)

    return byte_array