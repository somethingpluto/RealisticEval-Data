/**
 * Determine if two rectangles intersect horizontally.
 *
 * Each rectangle is defined by an array [x1, y1, x2, y2], where:
 * - [x1, y1] are the coordinates of the bottom-left corner.
 * - [x2, y2] are the coordinates of the top-right corner.
 *
 * @param {Array} rect1 - The first rectangle defined by [x1, y1, x2, y2].
 * @param {Array} rect2 - The second rectangle defined by [x1, y1, x2, y2].
 * @returns {boolean} - True if the rectangles intersect horizontally, False otherwise.
 */
function intersectHorizontally(rect1, rect2) {
    // Extract the y-coordinates of the bottom and top of each rectangle
    const y1Top = rect1[3];
    const y2Top = rect2[3];
    const y1Bottom = rect1[1];
    const y2Bottom = rect2[1];

    // Check if the rectangles intersect horizontally
    return !(y1Top < y2Bottom || y2Top < y1Bottom);
}
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
