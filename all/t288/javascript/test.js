describe('Bresenham Line Algorithm', () => {
  it('should return an empty array for equal start and end points', () => {
    const result = bresenhamLine(0, 0, 0, 0);
    expect(result).toEqual([]);
  });

  it('should return the start and end points when they are different', () => {
    const result = bresenhamLine(0, 0, 3, 4);
    expect(result).toEqual([[0, 0], [1, 1], [2, 2], [3, 3]]);
  });

  it('should handle vertical lines correctly', () => {
    const result = bresenhamLine(2, 1, 2, 5);
    expect(result).toEqual([[2, 1], [2, 2], [2, 3], [2, 4], [2, 5]]);
  });

  it('should handle horizontal lines correctly', () => {
    const result = bresenhamLine(1, 3, 5, 3);
    expect(result).toEqual([[1, 3], [2, 3], [3, 3], [4, 3], [5, 3]]);
  });

  it('should handle diagonal lines correctly', () => {
    const result = bresenhamLine(0, 0, 3, 3);
    expect(result).toEqual([[0, 0], [1, 1], [2, 2], [3, 3]]);
  });
});