// ... (previous code for context)

function getLineSegmentIntersection(seg1: [number, number][], seg2: [number, number][]): [number, number] | null {
    // ... (existing code)

    // Check if the intersection point is within both segments
    const isWithinSeg1 = (t: number) => t >= 0 && t <= 1;
    const isWithinSeg2 = (u: number) => u >= 0 && u <= 1;

    if (isWithinSeg1(t) && isWithinSeg2(u)) {
        return [x, y];
    }

    return null;
}

// ... (rest of the code)
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
