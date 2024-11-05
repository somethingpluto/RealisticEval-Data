function extractCharacterBits(byteArray: Uint8Array, char: string, charset: string = 'utf-8'): [number, string] | null {
    try {
        // Decode byte array to string using the specified character set
        const string = new TextDecoder(charset).decode(byteArray);
        
        // Check if the character is in the decoded string
        if (string.includes(char)) {
            const position = string.indexOf(char);
            
            // Find the byte position of the character
            const bytePosition = new TextEncoder().encode(string.slice(0, position)).length;
            
            // Determine the length of the character in bytes
            const charLength = new TextEncoder().encode(char).length;
            
            // Extract the bits corresponding to the character
            const bits = byteArray.subarray(bytePosition, bytePosition + charLength);
            
            // Convert bits to a human-readable binary string
            const bitsAsString = Array.from(bits).map(byte => `${byte.toString(2).padStart(8, '0')}`).join(' ');
            
            return [position, bitsAsString];
        } else {
            console.log(`The character '${char}' is not in the byte array.`);
            return null;
        }
    } catch (error) {
        if (error instanceof Error && error.name === 'SyntaxError') {
            console.log("Failed to decode the byte array.");
        }
        return null;
    }
}