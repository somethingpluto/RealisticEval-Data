function extractCharacterBits(byteArray, char, charset = 'utf-8') {
    /**
     * Extracts the position and bits of a specific character from a byte array.
     *
     * @param {Uint8Array} byteArray - The byte array to search within
     * @param {string} char - The character to find in the byte array
     * @param {string} [charset=utf-8] - The character encoding of the byte array
     * @returns {Object|null} - An object with properties `position` and `bits` if the character is found, otherwise null.
     */

    // Convert the character to its UTF-8 encoded byte representation
    const encoder = new TextEncoder();
    const charBytes = encoder.encode(char);

    // Find the position of the character in the byte array
    let position = -1;
    for (let i = 0; i < byteArray.length; i++) {
        if (byteArray[i] === charBytes[0]) {
            position = i;
            break;
        }
    }

    // If the character was not found, return null
    if (position === -1) {
        return null;
    }

    // Get the bits of the character
    const bits = [];
    for (let i = 0; i < charBytes.length; i++) {
        bits.push((charBytes[i] >>> 7) & 1);
        bits.push((charBytes[i] >>> 6) & 1);
        bits.push((charBytes[i] >>> 5) & 1);
        bits.push((charBytes[i] >>> 4) & 1);
        bits.push((charBytes[i] >>> 3) & 1);
        bits.push((charBytes[i] >>> 2) & 1);
        bits.push((charBytes[i] >>> 1) & 1);
        bits.push(charBytes[i] & 1);
    }

    // Return the result as an object
    return {
        position,
        bits
    };
}