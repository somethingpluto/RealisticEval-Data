font_chars = "CRHpm1234567890.°%$Є"
font_width = 16
font_height = 36


def bits_get_character(bits_array, character):
    if character not in font_chars:
        return

    char_bits = []

    char_index = font_chars.index(character)
    char_width = font_width

    for y in range(font_height):
        bit_offset = int(char_width * char_index + (len(font_chars) * char_width * y))
        for x in range(char_width):
            pixel_bit = bits_array[bit_offset + x]
            char_bits.append(pixel_bit)

    return char_bits
