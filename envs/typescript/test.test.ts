function intersectVertically(rect1: [number, number, number, number], rect2: [number, number, number, number]): boolean {
    /**
     * Determine if two rectangles intersect vertically.
     *
     * Each rectangle is defined by a tuple (x1, y1, x2, y2), where:
     * - (x1, y1) are the coordinates of the bottom-left corner.
     * - (x2, y2) are the coordinates of the top-right corner.
     *
     * @param rect1 - The first rectangle defined by (x1, y1, x2, y2).
     * @param rect2 - The second rectangle defined by (x1, y1, x2, y2).
     * @returns True if the rectangles intersect vertically, False otherwise.
     */
    return !(rect1[3] < rect2[1] || rect2[3] < rect1[1]);
}
describe('intersectVertically', () => {
  it('should return true for overlapping rectangles', () => {
    const rect1: [number, number, number, number] = [0, 0, 2, 2];
    const rect2: [number, number, number, number] = [1, 1, 3, 3];
    expect(intersectVertically(rect1, rect2)).toBe(true);
  });

  it('should return true for overlapping rectangles with negative coordinates', () => {
    const rect1: [number, number, number, number] = [-1, -1, 1, 1];
    const rect2: [number, number, number, number] = [0, 0, 2, 2];
    expect(intersectVertically(rect1, rect2)).toBe(true);
  });

  it('should return true for partially overlapping rectangles vertically', () => {
    const rect1: [number, number, number, number] = [0, 1, 2, 4];
    const rect2: [number, number, number, number] = [1, 0, 3, 2];
    expect(intersectVertically(rect1, rect2)).toBe(true);
  });

  it('should return true for identical rectangles', () => {
    const rect1: [number, number, number, number] = [0, 0, 2, 2];
    const rect2: [number, number, number, number] = [0, 0, 2, 2];
    expect(intersectVertically(rect1, rect2)).toBe(true);
  });

  it('should return true when one rectangle is completely inside the other', () => {
    const rect1: [number, number, number, number] = [0, 0, 4, 4];
    const rect2: [number, number, number, number] = [1, 1, 2, 2];
    expect(intersectVertically(rect1, rect2)).toBe(true);
  });
});
