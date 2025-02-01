/**
 * Check whether two rectangles intersect in the vertical direction.
 *
 * Each rectangle is defined by an array [x1, y1, x2, y2], where:
 * - [x1, y1] are the coordinates of the bottom-left corner.
 * - [x2, y2] are the coordinates of the top-right corner.
 *
 * @param {Array} rect1 - The first rectangle defined by [x1, y1, x2, y2].
 * @param {Array} rect2 - The second rectangle defined by [x1, y1, x2, y2].
 * @returns {boolean} - True if the rectangles intersect vertically, False otherwise.
 */
function intersectVertically(rect1, rect2) {
    // Extract the y-coordinates of the bottom and top of each rectangle
    const y1Top = rect1[3];
    const y1Bottom = rect1[1];
    const y2Top = rect2[3];
    const y2Bottom = rect2[1];

    // Check if the rectangles intersect vertically
    return !(y1Top < y2Bottom || y2Top < y1Bottom);
}
describe('intersectVertically', () => {
    it('should return true for overlapping rectangles', () => {
        const rect1 = [0, 0, 2, 2];
        const rect2 = [1, 1, 3, 3];
        expect(intersectVertically(rect1, rect2)).toBe(true);
    });

    it('should return true for overlapping rectangles', () => {
        const rect1 = [-1, -1, 1, 1];
        const rect2 = [0, 0, 2, 2];
        expect(intersectVertically(rect1, rect2)).toBe(true);
    });

    it('should return true for partially overlapping rectangles vertically', () => {
        const rect1 = [0, 1, 2, 4];
        const rect2 = [1, 0, 3, 2];
        expect(intersectVertically(rect1, rect2)).toBe(true);
    });

    it('should return true for identical rectangles', () => {
        const rect1 = [0, 0, 2, 2];
        const rect2 = [0, 0, 2, 2];
        expect(intersectVertically(rect1, rect2)).toBe(true);
    });

    it('should return true when one rectangle is completely inside the other', () => {
        const rect1 = [0, 0, 4, 4];
        const rect2 = [1, 1, 2, 2];
        expect(intersectVertically(rect1, rect2)).toBe(true);
    });
});
