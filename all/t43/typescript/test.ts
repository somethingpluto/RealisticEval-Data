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