/**
 * Recursively calculates a point on a Bézier curve using De Casteljau's algorithm.
 *
 * @param {number} t - A value between 0 and 1 representing the interpolation parameter.
 * @param {Array<{x: number, y: number}>} points - An array of control points defining the Bézier curve.
 * @returns {{x: number, y: number}} The calculated Coordinates at the given parameter t.
 */
function getBezierPoint(t, points) {
    // Base case: if there's only one point left, return it
    if (points.length === 1) {
        return points[0];
    }

    // Recursive case: calculate new points by interpolating between each pair of points
    let newPoints = [];
    for (let i = 0; i < points.length - 1; i++) {
        let x = (1 - t) * points[i].x + t * points[i + 1].x;
        let y = (1 - t) * points[i].y + t * points[i + 1].y;
        newPoints.push({ x, y });
    }

    // Recursively call the function with the new set of points
    return getBezierPoint(t, newPoints);
}
describe('getBezierPoint', () => {
    // Test case 1: Test with a simple linear curve
    test('should return the midpoint of two points', () => {
        const points = [{ x: 0, y: 0 }, { x: 2, y: 2 }];
        const result = getBezierPoint(0.5, points);
        expect(result).toEqual({ x: 1, y: 1 });
    });

    // Test case 2: Test with three points (quadratic curve)
    test('should return the correct point on a quadratic Bézier curve', () => {
        const points = [
            { x: 0, y: 0 },
            { x: 1, y: 2 },
            { x: 2, y: 0 }
        ];
        const result = getBezierPoint(0.5, points);
        expect(result).toEqual({ x: 1, y: 1 });
    });

    // Test case 3: Test with four points (cubic curve)
    test('should return the correct point on a cubic Bézier curve', () => {
        const points = [
            { x: 0, y: 0 },
            { x: 1, y: 3 },
            { x: 3, y: 1 },
            { x: 4, y: 0 }
        ];
        const result = getBezierPoint(0.5, points);
        expect(result).toEqual({ x: 2, y: 1.5 });
    });

    // Test case 4: Test with single point (edge case)
    test('should return the only point when there is a single control point', () => {
        const points = [{ x: 5, y: 5 }];
        const result = getBezierPoint(0.5, points);
        expect(result).toEqual({ x: 5, y: 5 });
    });

    // Test case 5: Test with extreme t value (0)
    test('should return the first control point when t is 0', () => {
        const points = [
            { x: 0, y: 0 },
            { x: 5, y: 5 }
        ];
        const result = getBezierPoint(0, points);
        expect(result).toEqual({ x: 0, y: 0 });
    });

    // Test case 6: Test with extreme t value (1)
    test('should return the last control point when t is 1', () => {
        const points = [
            { x: 0, y: 0 },
            { x: 5, y: 5 }
        ];
        const result = getBezierPoint(1, points);
        expect(result).toEqual({ x: 5, y: 5 });
    });
});
