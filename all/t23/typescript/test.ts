describe('TestLineSegmentIntersection', () => {
  it('should find the intersection correctly', () => {
      const seg1: [number, number][] = [[1, 1], [4, 4]];
      const seg2: [number, number][] = [[1, 4], [4, 1]];
      const expected: [number, number] = [2.5, 2.5];
      const result = getLineSegmentIntersection(seg1, seg2);
      expect(result).toEqual(expected);
  });

  it('should return null when there is no intersection', () => {
      const seg1: [number, number][] = [[1, 1], [2, 2]];
      const seg2: [number, number][] = [[3, 3], [4, 4]];
      const result = getLineSegmentIntersection(seg1, seg2);
      expect(result).toBeNull();
  });

  it('should return null for parallel segments', () => {
      const seg1: [number, number][] = [[1, 1], [2, 2]];
      const seg2: [number, number][] = [[1, 2], [2, 3]];
      const result = getLineSegmentIntersection(seg1, seg2);
      expect(result).toBeNull();
  });

  it('should return null when there is no intersection due to offset', () => {
      const seg1: [number, number][] = [[1, 1], [3, 3]];
      const seg2: [number, number][] = [[3, 2], [4, 2]];
      const result = getLineSegmentIntersection(seg1, seg2);
      expect(result).toBeNull();
  });

  it('should find the intersection with large coordinates correctly', () => {
      const seg1: [number, number][] = [[1000, 1000], [2000, 2000]];
      const seg2: [number, number][] = [[1000, 2000], [2000, 1000]];
      const expected: [number, number] = [1500.0, 1500.0];
      const result = getLineSegmentIntersection(seg1, seg2);
      expect(result).toEqual(expected);
  });
});