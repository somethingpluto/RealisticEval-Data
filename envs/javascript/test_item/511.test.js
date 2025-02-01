/**
 * Convert a hexadecimal color code to an ANSI escape code.
 *
 * @param {string} hexColor - A string representing the hexadecimal color code, e.g., '#FF5733'.
 * @returns {string} An ANSI escape code for the specified RGB color.
 */
function hexToAnsi(hexColor) {
    // Remove the hash at the start if it exists
    hexColor = hexColor.replace(/^#/, '');

    // Parse the hexadecimal values
    let r = parseInt(hexColor.substr(0, 2), 16);
    let g = parseInt(hexColor.substr(2, 2), 16);
    let b = parseInt(hexColor.substr(4, 2), 16);

    // Convert RGB to ANSI escape code
    return `\u001b[38;2;${r};${g};${b}m`;
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
