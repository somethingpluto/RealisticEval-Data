/**
 * Converts RGB color to HSV color.
 * 
 * Example:
 *   Input: 0, 0, 255
 *   Output: [240, 100, 100]
 * 
 * @param {number} r - The red value (0-255)
 * @param {number} g - The green value (0-255)
 * @param {number} b - The blue value (0-255)
 * 
 * @returns {Array<number>} An array representing the HSV values [H, S, V]
 */
function rgbToHsv(r, g, b) {
    r /= 255, g /= 255, b /= 255;
    var max = Math.max(r, g, b), min = Math.min(r, g, b);
    var h, s, v = max;

    var d = max - min;
    s = max === 0 ? 0 : d / max;

    if (max === min) {
        h = 0; // achromatic
    } else {
        switch (max) {
            case r: h = (g - b) / d + (g < b ? 6 : 0); break;
            case g: h = (b - r) / d + 2; break;
            case b: h = (r - g) / d + 4; break;
        }
        h /= 6;
    }

    return [Math.round(h * 360), Math.round(s * 100), Math.round(v * 100)];
}
describe('Test RGB to HSV Conversion', () => {
  it('converts pure red color correctly', () => {
      // Test conversion of pure red color
      const r = 255;
      const g = 0;
      const b = 0;
      const expectedResult = [0, 100, 100];  // Hue should be 0, Saturation 1, Value 1 for red
      const result = rgbToHsv(r, g, b);
      expect(result).toEqual(expectedResult);
  });

  it('converts pure green color correctly', () => {
      // Test conversion of pure green color
      const r = 0;
      const g = 255;
      const b = 0;
      const expectedResult = [120, 100, 100];  // Hue should be 120, Saturation 1, Value 1 for green
      const result = rgbToHsv(r, g, b);
      expect(result).toEqual(expectedResult);
  });

  it('converts pure blue color correctly', () => {
      // Test conversion of pure blue color
      const r = 0;
      const g = 0;
      const b = 255;
      const expectedResult = [240, 100, 100];  // Hue should be 240, Saturation 1, Value 1 for blue
      const result = rgbToHsv(r, g, b);
      expect(result).toEqual(expectedResult);
  });

  it('converts white color correctly', () => {
      // Test conversion of white color
      const r = 255;
      const g = 255;
      const b = 255;
      const expectedResult = [0, 0, 100];  // Hue is undefined, typically 0; Saturation 0, Value 1 for white
      const result = rgbToHsv(r, g, b);
      expect(result).toEqual(expectedResult);
  });

  it('converts black color correctly', () => {
      // Test conversion of black color
      const r = 0;
      const g = 0;
      const b = 0;
      const expectedResult = [0, 0, 0];  // Hue is undefined, typically 0; Saturation 0, Value 0 for black
      const result = rgbToHsv(r, g, b);
      expect(result).toEqual(expectedResult);
  });
});
