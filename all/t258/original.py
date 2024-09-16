font_width = 16
font_height = 36
font_chars = "CRHpm1234567890.°%$Є"


def bytes_get_character(bytes_array, character):
    if character not in font_chars:
        return

    char_bits = []

    char_index = font_chars.index(character)
    char_width = int(font_width / 8)

    for y in range(font_height):
        bit_offset = int(char_width * char_index + (len(font_chars) * char_width * y))
        for x in range(char_width):
            for xi in range(8):
                pixel_bit = int((int(bytes_array[bit_offset + x]) & (2 ** xi)) == (2 ** xi))
                char_bits.append(pixel_bit)

    return char_bits
