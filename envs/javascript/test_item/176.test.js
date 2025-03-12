class Point {
    /**
     * Creates an instance of Point.
     * @param {number} x - The x-coordinate of the point.
     * @param {number} y - The y-coordinate of the point.
     */
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }

    /**
     * Calculate the Euclidean distance to another point.
     * @param {Point} other - The other point.
     * @returns {number} The distance to the other point.
     */
    distanceTo(other) {
        return Math.sqrt((this.x - other.x) ** 2 + (this.y - other.y) ** 2);
    }
}

/**
 * Find the k nearest neighbors to the query point.
 * @param {Point[]} points - An array of Point objects representing the available points in the space.
 * @param {Point} queryPoint - The Point object for which we want to find the nearest neighbors.
 * @param {number} k - The number of nearest neighbors to find.
 * @returns {Point[]} An array of the k nearest Point objects to the query point.
 */
function findKNearestNeighbors(points, queryPoint, k) {
    // Calculate distances from the query point to all other points
    const distances = points.map(point => ({
        point,
        distance: queryPoint.distanceTo(point)
    }));

    // Sort the points by distance
    distances.sort((a, b) => a.distance - b.distance);

    // Return the k nearest points
    return distances.slice(0, k).map(item => item.point);
}
describe('Point', () => {
    test('find k nearest neighbors simple case', () => {
        const points = [
            new Point(1, 2),
            new Point(3, 4),
            new Point(1, -1),
            new Point(5, 2)
        ];
        const queryPoint = new Point(2, 2);
        const k = 2;
        const result = findKNearestNeighbors(points, queryPoint, k);

        expect(result.length).toBe(2);
        expect(containsPoint(result, new Point(1, 2))).toBe(true);
        expect(containsPoint(result, new Point(3, 4))).toBe(true);
    });

    test('find k nearest neighbors exact match', () => {
        const points = [
            new Point(1, 2),
            new Point(2, 2),
            new Point(3, 3)
        ];
        const queryPoint = new Point(2, 2);
        const k = 1;
        const result = findKNearestNeighbors(points, queryPoint, k);

        expect(result.length).toBe(1);
        expect(result[0].x).toBeCloseTo(2.0, 3); // delta equivalent
        expect(result[0].y).toBeCloseTo(2.0, 3); // delta equivalent
    });

    test('find k nearest neighbors larger k', () => {
        const points = [
            new Point(1, 2),
            new Point(3, 4),
            new Point(1, -1),
            new Point(5, 2)
        ];
        const queryPoint = new Point(2, 2);
        const k = 5; // k is larger than the number of points
        const result = findKNearestNeighbors(points, queryPoint, k);

        expect(result.length).toBe(4);
    });

    test('find k nearest neighbors empty points', () => {
        const points = [];
        const queryPoint = new Point(2, 2);
        const k = 3;
        const result = findKNearestNeighbors(points, queryPoint, k);

        expect(result.length).toBe(0);
    });

    test('find k nearest neighbors all points equidistant', () => {
        const points = [
            new Point(2, 3),
            new Point(3, 2),
            new Point(1, 2),
            new Point(2, 1)
        ];
        const queryPoint = new Point(2, 2);
        const k = 2;
        const result = findKNearestNeighbors(points, queryPoint, k);

        expect(result.length).toBe(2);
        expect(containsPoint(result, new Point(2, 3))).toBe(true);
        expect(containsPoint(result, new Point(3, 2))).toBe(true);
    });
});
