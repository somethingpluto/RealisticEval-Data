def hex_string_to_byte_array(hex_str: str) -> bytes:
    # If the length of the hex string is odd, prepend a '0'
    if len(hex_str) % 2 == 1:
        hex_str = "0" + hex_str

    # Convert hex string to bytes
    length = len(hex_str)
    data = bytearray(length // 2)

    for i in range(0, length, 2):
        # Calculate the byte value from two hex characters
        data[i // 2] = (int(hex_str[i], 16) << 4) + int(hex_str[i + 1], 16)

    return bytes(data)  # Convert bytearray to bytes