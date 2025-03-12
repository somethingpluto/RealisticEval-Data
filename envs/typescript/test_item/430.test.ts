// Start of the module
export module GeometryUtils {

  /**
   * Check whether two rectangles intersect in the vertical direction.
   * ... [rest of the JSDoc comment]
   */
  export function intersectVertically(rect1: [number, number, number, number], rect2: [number, number, number, number]): boolean {
    // ... [rest of the function code]
  }

  /**
   * Check whether two rectangles intersect in the horizontal direction.
   * ... [rest of the JSDoc comment]
   */
  export function intersectHorizontally(rect1: [number, number, number, number], rect2: [number, number, number, number]): boolean {
    const [x1, y1, x2, y2] = rect1;
    const [x3, y3, x4, y4] = rect2;
    return x1 < x4 && x2 > x3;
  }

}
// End of the module
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
