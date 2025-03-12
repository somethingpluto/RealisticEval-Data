// Start of the module
export module ColorConverter {
  /**
   * Converts a floating-point number between 0 and 1 to a color from red to green in the RGB format.
   * 
   * @param value - A float between 0 and 1.
   * @returns A tuple representing the RGB color.
   */
  export function floatToRGB(value: number): [number, number, number] {
    // ... (rest of the function remains unchanged)
  }

  /**
   * Converts a floating-point number between 0 and 1 to a color from green to blue in the RGB format.
   * 
   * @param value - A float between 0 and 1.
   * @returns A tuple representing the RGB color.
   */
  export function floatToRGBGB(value: number): [number, number, number] {
    const green = Math.round(255 * value);
    const blue = Math.round(255 * (1 - value));
    return [0, green, blue];
  }
}
// End of the module
describe('TestFloatToRGB', () => {
    it('should return pure red for value 0.0', () => {
        const result = floatToRGB(0.0);
        expect(result).toEqual([255, 0, 0]);
    });

    it('should return pure green for value 1.0', () => {
        const result = floatToRGB(1.0);
        expect(result).toEqual([0, 255, 0]);
    });

    it('should return yellow (equal mix of red and green) for value 0.5', () => {
        const result = floatToRGB(0.5);
        expect(result).toEqual([127, 127, 0]);
    });

    it('should return more red than green for value 0.25', () => {
        const result = floatToRGB(0.25);
        expect(result).toEqual([191, 63, 0]);
    });

    it('should throw an error for value outside the range [0, 1]', () => {
        expect(() => floatToRGB(1.5)).toThrow('Value must be between 0 and 1 inclusive.');
    });
});
