describe('rgbToHsv', () => {
  it('should convert RGB (0, 0, 255) to HSV (240, 100, 100)', () => {
      const result = rgbToHsv(0, 0, 255);
      expect(result).toEqual([240, 100, 100]);
  });

  // Add more test cases here...
});