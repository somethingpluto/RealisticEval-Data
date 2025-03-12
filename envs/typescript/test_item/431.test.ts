// Start of the module
export module GeometryUtils {

  /**
   * Determine if two rectangles intersect horizontally.
   * ... (rest of the JSDoc comment)
   */
  export function intersectHorizontally(rect1: [number, number, number, number], rect2: [number, number, number, number]): boolean {
    // ... (rest of the function)
  }

  /**
   * Determine if two rectangles intersect vertically.
   * ... (rest of the JSDoc comment)
   */
  export function intersectVertically(rect1: [number, number, number, number], rect2: [number, number, number, number]): boolean {
    const [x1, y1, x2, y2] = rect1;
    const [x3, y3, x4, y4] = rect2;

    return y1 < y4 && y3 < y2;
  }

}
// End of the module
describe('intersectHorizontally', () => {
    it('test with overlapping rectangles', () => {
        const rect1 = [0, 0, 2, 2];
        const rect2 = [1, 1, 3, 3];
        expect(intersectHorizontally(rect1, rect2)).toBe(true);
    });

    it('test with rectangles touching at a point (not overlapping)', () => {
        const rect1 = [0, 0, 1, 1];
        const rect2 = [1, 1, 2, 2];
        expect(intersectHorizontally(rect1, rect2)).toBe(true);
    });

    it('test with adjacent rectangles (no overlap)', () => {
        const rect1 = [0, 0, 2, 2];
        const rect2 = [2, 0, 3, 3];
        expect(intersectHorizontally(rect1, rect2)).toBe(true);
    });

    it('test with one rectangle fully inside another', () => {
        const rect1 = [1, 1, 4, 4];
        const rect2 = [2, 2, 3, 3];
        expect(intersectHorizontally(rect1, rect2)).toBe(true);
    });

    it('test with overlapping rectangles', () => {
        const rect1 = [-1, -1, 1, 1];
        const rect2 = [0, 0, 2, 2];
        expect(intersectHorizontally(rect1, rect2)).toBe(true);
    });
});
