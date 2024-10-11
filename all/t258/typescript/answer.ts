function extractCharacterBits(byteArray: Uint8Array, char: string, charset: string = 'utf-8'): [number, string] | null {
    // Convert the character to its UTF-8 encoded byte array
    const charBytes = new TextEncoder().encode(char);

    // Check if the character is in the byte array
    for (let i = 0; i < byteArray.length; i++) {
        let match = true;
        for (let j = 0; j < charBytes.length; j++) {
            if (byteArray[i + j] !== charBytes[j]) {
                match = false;
                break;
            }
        }

        if (match) {
            // Return the position and bits of the character
            return [i, char];
        }
    }

    // If the character is not found, return null
    return null;
}