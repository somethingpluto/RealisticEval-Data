def convert_bits_to_bytes(bits_array):
    bytes_array = []
    new_byte = 0
    bit_count = 0
    for bit in bits_array:
        if bit:
            new_byte |= 2 ** (bit_count % 8)
        bit_count += 1
        if (bit_count % 8) == 0:
            bytes_array.append(new_byte)
            new_byte = 0

    return bytes_array
