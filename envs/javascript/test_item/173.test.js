/**
 * Calculate the coordinates of a cubic Bézier curve at a given parameter t (typically between 0 and 1).
 * @param {number} t  A number representing the parameter along the curve, where 0 <= t <= 1.
 * @param {Array<number>} p0 A two-element array representing the x and y coordinates of the start point.
 * @param {Array<number>} p1 A two-element array representing the x and y coordinates of the first control point.
 * @param {Array<number>} p2 A two-element array representing the x and y coordinates of the second control point.
 * @param {Array<number>} p3 A two-element array representing the x and y coordinates of the end point.
 * @return {Array<number>} A two-element array containing the x and y coordinates of the point on the curve corresponding to the parameter t.
 */
function cubicBezier(t, p0, p1, p2, p3) {
    const x = Math.pow(1 - t, 3) * p0[0] + 3 * Math.pow(1 - t, 2) * t * p1[0] + 3 * (1 - t) * Math.pow(t, 2) * p2[0] + Math.pow(t, 3) * p3[0];
    const y = Math.pow(1 - t, 3) * p0[1] + 3 * Math.pow(1 - t, 2) * t * p1[1] + 3 * (1 - t) * Math.pow(t, 2) * p2[1] + Math.pow(t, 3) * p3[1];
    return [x, y];
}
describe('cubicBezier', () => {
    test('t = 0', () => {
        const p0 = [0.0, 0.0];
        const p1 = [0.0, 1.0];
        const p2 = [1.0, 1.0];
        const p3 = [1.0, 0.0];
        const t = 0.0;
        const expected = [0.0, 0.0];
        expect(cubicBezier(t, p0, p1, p2, p3)).toEqual(expected);
    });

    test('t = 1', () => {
        const p0 = [0.0, 0.0];
        const p1 = [0.0, 1.0];
        const p2 = [1.0, 1.0];
        const p3 = [1.0, 0.0];
        const t = 1.0;
        const expected = [1.0, 0.0];
        expect(cubicBezier(t, p0, p1, p2, p3)).toEqual(expected);
    });

    test('t = 0.5', () => {
        const p0 = [0.0, 0.0];
        const p1 = [0.0, 1.0];
        const p2 = [1.0, 1.0];
        const p3 = [1.0, 0.0];
        const t = 0.5;
        const expected = [0.5, 0.75];
        expect(cubicBezier(t, p0, p1, p2, p3)).toBeCloseTo(expected[0], 9);
        expect(cubicBezier(t, p0, p1, p2, p3)).toBeCloseTo(expected[1], 9);
    });

    test('t = 0.5 with mid points', () => {
        const p0 = [0.0, 0.0];
        const p1 = [1.0, 1.0];
        const p2 = [2.0, 1.0];
        const p3 = [3.0, 0.0];
        const t = 0.5;
        const expected = [1.5, 0.75];
        expect(cubicBezier(t, p0, p1, p2, p3)).toBeCloseTo(expected[0], 9);
        expect(cubicBezier(t, p0, p1, p2, p3)).toBeCloseTo(expected[1], 9);
    });

    test('arbitrary t = 0.75', () => {
        const p0 = [0.0, 0.0];
        const p1 = [0.0, 2.0];
        const p2 = [2.0, 2.0];
        const p3 = [2.0, 0.0];
        const t = 0.75;
        const expected = [1.6875, 1.125];
        expect(cubicBezier(t, p0, p1, p2, p3)).toBeCloseTo(expected[0], 9);
        expect(cubicBezier(t, p0, p1, p2, p3)).toBeCloseTo(expected[1], 9);
    });
});
