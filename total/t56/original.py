def find_shiftjis_not_in_gbk_full():
    """generated by chatgpt, find characters that exist in the Shift-JIS encoding but not in the GBK encoding"""
    start = 0x0000  # Starting from the beginning of Unicode range
    end = 0xFFFF  # Up to the Basic Multilingual Plane
    shiftjis_not_in_gbk = []
    for codepoint in range(start, end):
        character = chr(codepoint)
        try:
            # Try encoding the character in Shift JIS
            sjis_encoded = character.encode("shift_jis")
            try:
                # Try encoding the character in GBK
                gbk_encoded = character.encode("gbk")
            except UnicodeEncodeError:
                # If encoding in GBK fails, add to the list
                shiftjis_not_in_gbk.append(character)
        except UnicodeEncodeError:
            pass

    return shiftjis_not_in_gbk