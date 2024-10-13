def base64_encode(data):
    """Encode a bytes-like object to Base64."""
    base64_chars = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz"
        "0123456789+/"
    )
    
    encoded_string = []
    val = 0
    valb = -6

    for c in data:
        val = (val << 8) + c
        valb += 8
        while valb >= 0:
            encoded_string.append(base64_chars[(val >> valb) & 0x3F])
            valb -= 6
    
    if valb > -6:
        encoded_string.append(base64_chars[((val << 8) >> (valb + 8)) & 0x3F])
    
    # Add padding with '=' to make the length a multiple of 4
    while len(encoded_string) % 4:
        encoded_string.append('=')

    return ''.join(encoded_string)
