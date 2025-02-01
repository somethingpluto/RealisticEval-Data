/**
 * Check whether a point is on a line formed by two points, such as point C is on a line formed by points A and B.
 * 
 * @param {Array<number>} A - Point A [x, y]
 * @param {Array<number>} B - Point B [x, y]
 * @param {Array<number>} C - Point C [x, y]
 * @returns {boolean} - True if point C is on the line formed by points A and B, false otherwise.
 */
function isPointOnLine(A, B, C) {
    // Check if the point C is collinear with points A and B
    // Using the area of the triangle formed by the three points, if it's zero, they are collinear
    const area = A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1]);
    if (area === 0) {
        // Check if point C lies on the segment AB
        // Using the dot product to check if the point C is between A and B
        const dotProduct = (C[0] - A[0]) * (B[0] - A[0]) + (C[1] - A[1]) * (B[1] - A[1]);
        const squaredLengthAB = (B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2;
        return dotProduct >= 0 && dotProduct <= squaredLengthAB;
    }
    return false;
}
describe('TestPointOnLine', () => {
    test('should return true when point C is on the line formed by points A and B', () => {
        const A = [0, 0];
        const B = [10, 10];
        const C = [5, 5];
        expect(isPointOnLine(A, B, C)).toBe(true);
    });

    test('should return false when point C is not on the line formed by points A and B', () => {
        const A = [0, 0];
        const B = [10, 10];
        const C = [5, 6];
        expect(isPointOnLine(A, B, C)).toBe(false);
    });

    test('should return true for a vertical line', () => {
        const A = [5, 0];
        const B = [5, 10];
        const C = [5, 5];
        expect(isPointOnLine(A, B, C)).toBe(true);
    });

    test('should return true for a horizontal line', () => {
        const A = [0, 5];
        const B = [10, 5];
        const C = [5, 5];
        expect(isPointOnLine(A, B, C)).toBe(true);
    });

    test('should return false for a point not on a vertical line', () => {
        const A = [5, 0];
        const B = [5, 10];
        const C = [6, 5];
        expect(isPointOnLine(A, B, C)).toBe(false);
    });
});
