/**
 * Check whether a point is on a line formed by two points, such as point C is on a line formed by points A and B.
 * 
 * @param {Array<number>} A - Point A [x, y]
 * @param {Array<number>} B - Point B [x, y]
 * @param {Array<number>} C - Point C [x, y]
 * @returns {boolean} - True if point C is on the line formed by points A and B, false otherwise.
 */
function isPointOnLine(A, B, C) {
    // Extract coordinates
    const [Ax, Ay] = A;
    const [Bx, By] = B;
    const [Cx, Cy] = C;

    // Calculate the cross product of vectors AB and AC
    const crossProduct = (Bx - Ax) * (Cy - Ay) - (By - Ay) * (Cx - Ax);

    // If the cross product is zero, point C lies on the line formed by points A and B
    return crossProduct === 0;
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
