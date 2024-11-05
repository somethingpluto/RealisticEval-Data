function extractCharacterBits(byteArray, char, charset = 'utf-8') {
    try {
        // Decode byte array to string using the specified character set
        const decoder = new TextDecoder(charset);
        const string = decoder.decode(byteArray);
    } catch (error) {
        console.log("Failed to decode the byte array.");
        return undefined;
    }

    // Check if the character is in the decoded string
    if (string.includes(char)) {
        const position = string.indexOf(char);

        // Find the byte position of the character
        const bytePosition = string.slice(0, position).length;

        // Determine the length of the character in bytes
        const charLength = new TextEncoder().encode(char).length;

        // Extract the bits corresponding to the character
        const bits = byteArray.slice(bytePosition, bytePosition + charLength);

        // Convert bits to a human-readable binary string
        const bitsAsString = bits.map(byte => byte.toString(2).padStart(8, '0')).join(' ');

        return [position, bitsAsString];
    } else {
        console.log(`The character '${char}' is not in the byte array.`);
        return undefined;
    }
}