def uint8_array_to_base64(uint8_array: bytearray) -> str:
    base64 = ""
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    for i in range(0, len(uint8_array), 3):
        a = uint8_array[i]
        b = uint8_array[i + 1] if i + 1 < len(uint8_array) else 0  # Use 0 if b is undefined
        c = uint8_array[i + 2] if i + 2 < len(uint8_array) else 0  # Use 0 if c is undefined

        index1 = a >> 2
        index2 = ((a & 0x03) << 4) | (b >> 4)
        index3 = ((b & 0x0f) << 2) | (c >> 6)
        index4 = c & 0x3f

        base64 += (
            characters[index1] +
            characters[index2] +
            (characters[index3] if i + 1 < len(uint8_array) else "=") +
            (characters[index4] if i + 2 < len(uint8_array) else "=")
        )

    return base64