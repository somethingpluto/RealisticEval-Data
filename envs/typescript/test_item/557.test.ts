// Start of the module
export module AngleConverter {
  /**
   * Converts an angle from radians to degrees.
   * @param radians - The angle in radians to convert.
   * @returns The angle in degrees.
   */
  export function radiansToDegrees(radians: number): number {
    return radians * (180 / Math.PI);
  }

  /**
   * Converts an angle from degrees to radians.
   * @param degrees - The angle in degrees to convert.
   * @returns The angle in radians.
   */
  export function degreesToRadians(degrees: number): number {
    return degrees * (Math.PI / 180);
  }
}
// End of the module
describe('radiansToDegrees', () => {
    it('should convert 0 radians to 0 degrees', () => {
        expect(radiansToDegrees(0)).toBeCloseTo(0, 5);
    });

    it('should convert π/2 radians to 90 degrees', () => {
        expect(radiansToDegrees(PI / 2)).toBeCloseTo(90, 5);
    });

    it('should convert π radians to 180 degrees', () => {
        expect(radiansToDegrees(PI)).toBeCloseTo(180, 5);
    });

    it('should convert 3π/2 radians to 270 degrees', () => {
        expect(radiansToDegrees(3 * PI / 2)).toBeCloseTo(270, 5);
    });

    it('should convert 2π radians to 360 degrees', () => {
        expect(radiansToDegrees(2 * PI)).toBeCloseTo(360, 5);
    });

    it('should convert -π/2 radians to -90 degrees', () => {
        expect(radiansToDegrees(-PI / 2)).toBeCloseTo(-90, 5);
    });

    it('should convert 4π radians to 720 degrees', () => {
        expect(radiansToDegrees(4 * PI)).toBeCloseTo(720, 5);
    });
});
