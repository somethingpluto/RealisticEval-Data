function findShiftJisNotGbk(): string[] {
    // Array to store characters that are in Shift-JIS but not in GBK
    const uniqueToShiftJis: string[] = [];

    // Iterate over a range of Unicode code points
    // The BMP goes up to U+FFFF, which is 65535 in decimal
    for (let codepoint = 0; codepoint < 65536; codepoint++) {
        const character = String.fromCodePoint(codepoint);

        try {
            // Try encoding the character in Shift-JIS
            Buffer.from(character, 'shift-jis').toString('shift-jis');
            try {
                // Try encoding the character in GBK
                Buffer.from(character, 'gbk').toString('gbk');
            } catch (error) {
                // If it fails, the character is not representable in GBK but is in Shift-JIS
                uniqueToShiftJis.push(character);
            }
        } catch (error) {
            // If it fails, the character is not representable in Shift-JIS, so we skip it
            continue;
        }
    }

    return uniqueToShiftJis;
}