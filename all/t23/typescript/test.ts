describe('getLineSegmentIntersection', () => {
    it('should return the intersection point of two line segments', () => {
      const seg1 = [[0, 0], [1, 1]];
      const seg2 = [[1, 0], [0, 1]];
      const expectedIntersection = [0.5, 0.5];
      const result = getLineSegmentIntersection(seg1, seg2);
      expect(result).toEqual(expectedIntersection);
    });
  
    it('should return null if the line segments do not intersect', () => {
      const seg1 = [[0, 0], [1, 1]];
      const seg2 = [[2, 2], [3, 3]];
      const result = getLineSegmentIntersection(seg1, seg2);
      expect(result).toBeNull();
    });
  });