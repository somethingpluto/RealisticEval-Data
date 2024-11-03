function base64Encode(data: Uint8Array): string {
    const base64Chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    let encodedString = '';
    let val = 0;
    let valb = -6;

    for (const c of data) {
        val = (val << 8) + c;
        valb += 8;
        while (valb >= 0) {
            encodedString += base64Chars[(val >> valb) & 0x3F];
            valb -= 6;
        }
    }

    if (valb > -6) {
        encodedString += base64Chars[((val << 8) >> (valb + 8)) & 0x3F];
    }

    while (encodedString.length % 4) {
        encodedString += '=';
    }

    return encodedString;
}