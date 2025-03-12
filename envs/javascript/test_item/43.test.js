/**
 * Converts RGB color to HSV color.
 * 
 * @param {number} r - The red value (0-255)
 * @param {number} g - The green value (0-255)
 * @param {number} b - The blue value (0-255)
 * 
 * @returns {Array<number>} An array representing the HSV values [H, S, V]
 */
function rgbToHsv(r, g, b) {
    r = r / 255;
    g = g / 255;
    b = b / 255;

    const max = Math.max(r, g, b);
    const min = Math.min(r, g, b);
    const delta = max - min;

    let h, s, v;

    if (delta === 0) {
        h = 0;
    } else if (max === r) {
        h = ((g - b) / delta) % 6;
    } else if (max === g) {
        h = ((b - r) / delta) + 2;
    } else {
        h = ((r - g) / delta) + 4;
    }

    h = Math.round(h * 60);
    if (h < 0) h += 360;

    v = Math.round(max * 100);

    if (max === 0) {
        s = 0;
    } else {
        s = Math.round((delta / max) * 100);
    }

    return [h, s, v];
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
