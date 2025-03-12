/**
 * Convert a hexadecimal color code to an ANSI escape code.
 *
 * @param {string} hexColor - A string representing the hexadecimal color code, e.g., '#FF5733'.
 * @returns {string} An ANSI escape code for the specified RGB color.
 */
function hexToAnsi(hexColor) {
    // Remove the '#' if it exists
    hexColor = hexColor.replace('#', '');

    // Parse the hex color into its RGB components
    const r = parseInt(hexColor.substring(0, 2), 16);
    const g = parseInt(hexColor.substring(2, 4), 16);
    const b = parseInt(hexColor.substring(4, 6), 16);

    // Convert RGB to ANSI 256 color code
    const ansiColor = 16 + (36 * Math.round(r / 255 * 5)) + (6 * Math.round(g / 255 * 5)) + Math.round(b / 255 * 5);

    // Return the ANSI escape code
    return `\x1b[38;5;${ansiColor}m`;
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
