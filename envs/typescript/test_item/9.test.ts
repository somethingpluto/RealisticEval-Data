// Start of the code context
import { Point } from './Point';

/**
 * Check whether a point C is on a line segment formed by points A and B.
 * 
 * @param A - Point A coordinates [x, y]
 * @param B - Point B coordinates [x, y]
 * @param C - Point C coordinates [x, y]
 * @returns true if point C is on the line segment formed by points A and B, false otherwise.
 */
function isPointOnLineSegment(A: Point, B: Point, C: Point): boolean {
    // Check if point C is collinear with A and B
    const collinear = (A.x * (B.y - C.y) + B.x * (C.y - A.y) + C.x * (A.y - B.y)) === 0;
    // Check if point C is within the bounds of the line segment AB
    const withinBounds = C.x >= Math.min(A.x, B.x) && C.x <= Math.max(A.x, B.x) &&
                           C.y >= Math.min(A.y, B.y) && C.y <= Math.max(A.y, B.y);
    return collinear && withinBounds;
}
// End of the code context
describe('isPointOnLine', () => {
    test('should return true when point C is on the line formed by points A and B', () => {
        const A: [number, number] = [0, 0];
        const B: [number, number] = [10, 10];
        const C: [number, number] = [5, 5];
        expect(isPointOnLine(A, B, C)).toBe(true);
    });

    test('should return false when point C is not on the line formed by points A and B', () => {
        const A: [number, number] = [0, 0];
        const B: [number, number] = [10, 10];
        const C: [number, number] = [5, 6];
        expect(isPointOnLine(A, B, C)).toBe(false);
    });

    test('should return true for a vertical line', () => {
        const A: [number, number] = [5, 0];
        const B: [number, number] = [5, 10];
        const C: [number, number] = [5, 5];
        expect(isPointOnLine(A, B, C)).toBe(true);
    });

    test('should return true for a horizontal line', () => {
        const A: [number, number] = [0, 5];
        const B: [number, number] = [10, 5];
        const C: [number, number] = [5, 5];
        expect(isPointOnLine(A, B, C)).toBe(true);
    });

    test('should return false for a point not on a vertical line', () => {
        const A: [number, number] = [5, 0];
        const B: [number, number] = [5, 10];
        const C: [number, number] = [6, 5];
        expect(isPointOnLine(A, B, C)).toBe(false);
    });
});
