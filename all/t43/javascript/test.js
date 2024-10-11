describe('rgbToHsv function', () => {
    it('converts RGB (0, 0, 255) to HSV (240, 100, 100)', () => {
      const result = rgbToHsv(0, 0, 255);
      expect(result).toEqual([240, 100, 100]);
    });
  
    // Add more tests here for other cases...
  });