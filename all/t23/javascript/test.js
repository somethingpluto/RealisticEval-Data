describe('getLineSegmentIntersection', () => {
    test('should return the intersection point of two line segments', () => {
      const seg1 = [[0, 0], [1, 1]];
      const seg2 = [[1, 0], [0, 1]];
      const result = getLineSegmentIntersection(seg1, seg2);
      expect(result).toEqual([0.5, 0.5]);
    });
  
    test('should return null when there is no intersection', () => {
      const seg1 = [[0, 0], [1, 0]];
      const seg2 = [[2, 0], [3, 0]];
      const result = getLineSegmentIntersection(seg1, seg2);
      expect(result).toBeNull();
    });
  });