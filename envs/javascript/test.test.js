function hexToAnsi(hexColor) {
    /**
     * Convert a hexadecimal color code to an ANSI escape code.
     *
     * Parameters:
     * hexColor (string): A string representing the hexadecimal color code, e.g., '#FF5733'.
     *
     * Returns:
     * string: An ANSI escape code for the specified RGB color.
     */

    // Check if the input is a valid hex color
    if (hexColor.length !== 7 || hexColor[0] !== '#') {
        throw new Error("Invalid hex color format. Use '#RRGGBB'.");
    }

    // Extract the red, green, and blue components from the hex string
    const r = parseInt(hexColor.substring(1, 3), 16);
    const g = parseInt(hexColor.substring(3, 5), 16);
    const b = parseInt(hexColor.substring(5, 7), 16);

    // Create the ANSI escape code
    const ansiCode = `\x1b[38;2;${r};${g};${b}m`;

    return ansiCode;
}
describe('TestHexToAnsi', () => {
    describe('testValidColors', () => {
        it('should handle valid hex color inputs correctly', () => {
            expect(hexToAnsi('#FF5733')).toBe('\x1b[38;2;255;87;51m');
            expect(hexToAnsi('#00FF00')).toBe('\x1b[38;2;0;255;0m');
            expect(hexToAnsi('#0000FF')).toBe('\x1b[38;2;0;0;255m');
        });
    });

    describe('testBlackAndWhite', () => {
        it('should handle black and white colors correctly', () => {
            expect(hexToAnsi('#000000')).toBe('\x1b[38;2;0;0;0m'); // Black
            expect(hexToAnsi('#FFFFFF')).toBe('\x1b[38;2;255;255;255m'); // White
        });
    });
});
