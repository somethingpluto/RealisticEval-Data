// Start of the module
export module ColorConverter {
  /**
   * Converts an RGB color to an HSV color.
   * 
   * Example:
   *   Input: 0, 0, 255
   *   Output: [240, 100, 100]
   * 
   * @param r - The red value of the RGB color (0-255).
   * @param g - The green value of the RGB color (0-255).
   * @param b - The blue value of the RGB color (0-255).
   * @returns A tuple representing the HSV color values [H, S, V].
   */
  export function rgbToHsv(r: number, g: number, b: number): [number, number, number] {
    // ... (rest of the function remains unchanged)
  }

  /**
   * Converts an HSV color to an RGB color.
   * 
   * Example:
   *   Input: [240, 100, 100]
   *   Output: [0, 0, 255]
   * 
   * @param h - The hue value of the HSV color (0-360).
   * @param s - The saturation value of the HSV color (0-100).
   * @param v - The value (brightness) value of the HSV color (0-100).
   * @returns A tuple representing the RGB color values [R, G, B].
   */
  export function hsvToRgb(h: number, s: number, v: number): [number, number, number] {
    // ... (implementation of hsvToRgb function)
  }
}
// End of the module
describe('Test RGB to HSV Conversion', () => {
  it('should convert pure red color correctly', () => {
      // Test conversion of pure red color
      const r = 255;
      const g = 0;
      const b = 0;
      const expectedResult: [number, number, number] = [0, 100, 100];  // Hue should be 0, Saturation 100, Value 100 for red
      const result = rgbToHsv(r, g, b);
      expect(result).toEqual(expectedResult);
  });

  it('should convert pure green color correctly', () => {
      // Test conversion of pure green color
      const r = 0;
      const g = 255;
      const b = 0;
      const expectedResult: [number, number, number] = [120, 100, 100];  // Hue should be 120, Saturation 100, Value 100 for green
      const result = rgbToHsv(r, g, b);
      expect(result).toEqual(expectedResult);
  });

  it('should convert pure blue color correctly', () => {
      // Test conversion of pure blue color
      const r = 0;
      const g = 0;
      const b = 255;
      const expectedResult: [number, number, number] = [240, 100, 100];  // Hue should be 240, Saturation 100, Value 100 for blue
      const result = rgbToHsv(r, g, b);
      expect(result).toEqual(expectedResult);
  });

  it('should convert white color correctly', () => {
      // Test conversion of white color
      const r = 255;
      const g = 255;
      const b = 255;
      const expectedResult: [number, number, number] = [0, 0, 100];  // Hue is undefined, typically 0; Saturation 0, Value 100 for white
      const result = rgbToHsv(r, g, b);
      expect(result).toEqual(expectedResult);
  });

  it('should convert black color correctly', () => {
      // Test conversion of black color
      const r = 0;
      const g = 0;
      const b = 0;
      const expectedResult: [number, number, number] = [0, 0, 0];  // Hue is undefined, typically 0; Saturation 0, Value 0 for black
      const result = rgbToHsv(r, g, b);
      expect(result).toEqual(expectedResult);
  });
});
