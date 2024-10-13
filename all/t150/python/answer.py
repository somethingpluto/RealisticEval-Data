def rgb_to_hex(rgb):
    """
    Convert an RGB color object to a HEX color string.

    :param rgb: A dictionary containing the red, green, and blue components of the color.
    :returns: A string representing the HEX color code.
    """
    r, g, b = rgb['r'], rgb['g'], rgb['b']

    def component_to_hex(c):
        if not isinstance(c, (int, float)) or c < 0 or c > 255:
            print("Invalid RGB component:", c)
            return "00"
        hex_value = hex(int(c))[2:]  # Convert to hex and remove '0x'
        return hex_value.zfill(2)  # Pad with zero if necessary

    return f'#{component_to_hex(r)}{component_to_hex(g)}{component_to_hex(b)}'


def hex_to_rgb(hex):
    """
    Convert a HEX color string to an RGB color object.

    :param hex: A string representing the HEX color code.
    :returns: A dictionary containing the red, green, and blue components of the color, or None if the HEX code is invalid.
    """
    def is_valid_hex(hex):
        shorthand_regex = r'^#?([a-f\d])([a-f\d])([a-f\d])$'
        hex = re.sub(shorthand_regex, lambda m: m.group(1) * 2 + m.group(2) * 2 + m.group(3) * 2, hex)
        return bool(re.match(r'^#?([a-f\d]{6})$', hex, re.IGNORECASE))

    if not is_valid_hex(hex):
        print("Invalid HEX color:", hex)
        return None

    full_hex = hex.lstrip('#')  # Remove the leading '#' if present
    r = int(full_hex[0:2], 16)
    g = int(full_hex[2:4], 16)
    b = int(full_hex[4:6], 16)
    
    return {'r': r, 'g': g, 'b': b}