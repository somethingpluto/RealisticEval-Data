describe('TestCalculateRedProportion', () => {
    it('should return 1.0 for all fully red pixels', () => {
      const pixels: [number, number, number][] = [[255, 0, 0], [255, 0, 0], [255, 0, 0]];
      const result = calculateRedProportion(pixels);
      expect(result).toBeCloseTo(1.0);
    });
  
    it('should return 0.0 for no red component in any pixel', () => {
      const pixels: [number, number, number][] = [[0, 255, 0], [0, 0, 255], [0, 255, 255]];
      const result = calculateRedProportion(pixels);
      expect(result).toBeCloseTo(0.0);
    });
  
    it('should return 0.0 for an empty list of pixels', () => {
      const pixels: [number, number, number][] = [];
      const result = calculateRedProportion(pixels);
      expect(result).toBeCloseTo(0.0);
    });
  
    it('should return 0.0 for all black pixels', () => {
      const pixels: [number, number, number][] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];
      const result = calculateRedProportion(pixels);
      expect(result).toBeCloseTo(0.0);
    });
  });