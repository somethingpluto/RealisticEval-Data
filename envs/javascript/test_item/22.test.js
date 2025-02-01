/**
 * calculates the Euclidean distance between two points in a 2D space.
 *
 * @param {Array<number>} point1 - The first point as an array of coordinates [x1, y1].
 * @param {Array<number>} point2 - The second point as an array of coordinates [x2, y2].
 * @returns {number} The Euclidean distance between the two points.
 */
function calculateEuclideanDistance(point1, point2) {
    const dx = point2[0] - point1[0];
    const dy = point2[1] - point1[1];
    return Math.sqrt(dx * dx + dy * dy);
}
describe('TestCalculateEuclideanDistance', () => {
    it('should calculate the distance correctly', () => {
        const point1 = [0, 0];
        const point2 = [3, 4];
        const expectedDistance = 5.0;
        expect(calculateEuclideanDistance(point1, point2)).toBe(expectedDistance);
    });

    it('should handle negative coordinates correctly', () => {
        const point1 = [-1, -1];
        const point2 = [-4, -5];
        const expectedDistance = 5.0;
        expect(calculateEuclideanDistance(point1, point2)).toBe(expectedDistance);
    });

    it('should return 0 when both points are the same', () => {
        const point1 = [2, 3];
        const point2 = [2, 3];
        const expectedDistance = 0.0;
        expect(calculateEuclideanDistance(point1, point2)).toBe(expectedDistance);
    });

    it('should handle large coordinates correctly', () => {
        const point1 = [1e6, 1e6];
        const point2 = [1e6 + 3, 1e6 + 4];
        const expectedDistance = 5.0;
        expect(calculateEuclideanDistance(point1, point2)).toBe(expectedDistance);
    });

    it('should throw a TypeError for invalid input', () => {
        expect(() => calculateEuclideanDistance("invalid", [0, 0])).toThrow(TypeError);
    });
});
