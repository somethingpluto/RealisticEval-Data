// Start of the TypeScript file

import { Color } from 'color';

/**
 * Converts a hexadecimal color code to an ANSI escape code.
 * @param hexColor - A string representing the hexadecimal color code, e.g., '#FF5733'.
 * @returns An ANSI escape code for the specified RGB color.
 */
function hexToAnsi(hexColor: string): string {
  // Validate the input
  if (!/^#[0-9A-F]{6}$/i.test(hexColor)) {
    throw new Error('Invalid hexadecimal color code');
  }

  // Convert hex to RGB
  const rgbColor = Color(hexColor).rgb().string();

  // Convert RGB to ANSI
  const ansiColor = rgbToAnsi(rgbColor);

  return ansiColor;
}

/**
 * Converts an RGB color string to an ANSI escape code.
 * @param rgbColor - A string representing the RGB color, e.g., 'rgb(255,87,51)'.
 * @returns An ANSI escape code for the specified RGB color.
 */
function rgbToAnsi(rgbColor: string): string {
  // Extract RGB values
  const rgbValues = rgbColor.match(/\d+/g).map(Number);
  const [r, g, b] = rgbValues;

  // Calculate ANSI code
  const ansiCode = 16 + Math.round(r / 255 * 36) + Math.round(g / 255 * 6) + Math.round(b / 255);

  return `\x1b[38;5;${ansiCode}m`;
}

// End of the TypeScript file
describe('TestHexToAnsi', () => {
    describe('testValidColors', () => {
        it('should correctly convert valid hex color inputs', () => {
            expect(hexToAnsi('#FF5733')).toBe('\x1b[38;2;255;87;51m');
            expect(hexToAnsi('#00FF00')).toBe('\x1b[38;2;0;255;0m');
            expect(hexToAnsi('#0000FF')).toBe('\x1b[38;2;0;0;255m');
        });
    });

    describe('testBlackAndWhite', () => {
        it('should correctly handle black and white colors', () => {
            expect(hexToAnsi('#000000')).toBe('\x1b[38;2;0;0;0m'); // Black
            expect(hexToAnsi('#FFFFFF')).toBe('\x1b[38;2;255;255;255m'); // White
        });
    });
});
