/**
 * Calculates the toroidal difference between two points.
 *
 * @param {Object} thisPoint - The first point with properties x and y.
 * @param {Object} otherPoint - The second point with properties x and y.
 * @param {number} width - The width of the toroidal space.
 * @param {number} height - The height of the toroidal space.
 * @returns {Array} - An array containing the x and y differences, accounting for wrap-around.
 */
function toroidalDiff(thisPoint, otherPoint, width, height) {
    let dx = Math.abs(thisPoint.x - otherPoint.x);
    let dy = Math.abs(thisPoint.y - otherPoint.y);
    let xDiff = Math.min(dx, width - dx);
    let yDiff = Math.min(dy, height - dy);
    return [xDiff, yDiff];
}
describe('toroidalDiff', () => {
    test('should return the direct difference when no wrapping is needed', () => {
        const thisPoint = { x: 2, y: 3 };
        const otherPoint = { x: 5, y: 6 };
        const width = 10;
        const height = 10;
        const result = toroidalDiff(thisPoint, otherPoint, width, height);
        expect(result).toEqual([-3, -3]);
    });

    test('should handle wrapping around the x dimension', () => {
        const thisPoint = { x: 9, y: 5 };
        const otherPoint = { x: 1, y: 5 };
        const width = 10;
        const height = 10;
        const result = toroidalDiff(thisPoint, otherPoint, width, height);
        expect(result).toEqual([-2, 0]); // dx wraps around the toroidal boundary
    });

    test('should handle wrapping around the y dimension', () => {
        const thisPoint = { x: 4, y: 9 };
        const otherPoint = { x: 4, y: 1 };
        const width = 10;
        const height = 10;
        const result = toroidalDiff(thisPoint, otherPoint, width, height);
        expect(result).toEqual([0, -2]); // dy wraps around the toroidal boundary
    });

    test('should handle wrapping around both x and y dimensions', () => {
        const thisPoint = { x: 9, y: 9 };
        const otherPoint = { x: 1, y: 1 };
        const width = 10;
        const height = 10;
        const result = toroidalDiff(thisPoint, otherPoint, width, height);
        expect(result).toEqual([-2, -2]); // Both dx and dy wrap around
    });

    test('should return the direct difference for points at the same position', () => {
        const thisPoint = { x: 5, y: 5 };
        const otherPoint = { x: 5, y: 5 };
        const width = 10;
        const height = 10;
        const result = toroidalDiff(thisPoint, otherPoint, width, height);
        expect(result).toEqual([0, 0]); // No difference
    });
});
