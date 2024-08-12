def find_shiftjis_not_gbk():
    # List to store characters that are in Shift-JIS but not in GBK
    unique_to_shiftjis = []

    # Iterate over a range of Unicode code points
    # The BMP goes up to U+FFFF, which is 65535 in decimal
    for codepoint in range(65536):
        character = chr(codepoint)

        try:
            # Try encoding the character in Shift-JIS
            character.encode('shift_jis')
            try:
                # Try encoding the character in GBK
                character.encode('gbk')
            except UnicodeEncodeError:
                # If it fails, the character is not representable in GBK but is in Shift-JIS
                unique_to_shiftjis.append(character)
        except UnicodeEncodeError:
            # If it fails, the character is not representable in Shift-JIS, so we skip it
            continue

    return unique_to_shiftjis
