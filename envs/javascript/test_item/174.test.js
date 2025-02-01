/**
 * Finds the parameter `t` corresponding to a given x-coordinate `targetX`
 * on a quadratic Bézier curve defined by control points p0, p1, and p2.
 * The function uses the secant method to iteratively approach the value of `t`
 * where the Bézier curve intersects with the vertical line at `targetX`.
 *
 * @param {number} targetX - The x-coordinate for which we want to find the corresponding
 *                parameter `t` on the Bézier curve.
 * @param {number} p0 - The first control point of the Bézier curve, representing the
 *            starting point.
 * @param {number} p1 - The second control point of the Bézier curve, affecting the curve's
 *            shape.
 * @param {number} p2 - The third control point of the Bézier curve, representing the
 *            ending point.
 * @return {number} The parameter `t` (in the range [0, 1]) for which the Bézier curve
 *         evaluated at `t` is closest to `targetX`. If no precise value is
 *         found within the specified tolerance and iterations, the function
 *         returns the best approximation.
 */
function findTForX(targetX, p0, p1, p2) {
    const tolerance = 0.00001;
    let t0 = 0;
    let t1 = 1;
    let t = 0.5;

    while (Math.abs(bezierX(t, p0, p1, p2) - targetX) > tolerance) {
        if (bezierX(t, p0, p1, p2) === targetX) {
            break;
        }

        if (bezierX(t0, p0, p1, p2) === bezierX(t1, p0, p1, p2)) {
            // If both t0 and t1 produce the same x value, we cannot proceed
            // with the secant method, so we return the best approximation.
            return t;
        }

        t = t1 - (bezierX(t1, p0, p1, p2) - targetX) * (t1 - t0) / (bezierX(t1, p0, p1, p2) - bezierX(t0, p0, p1, p2));
        t0 = t1;
        t1 = t;
    }

    return t;
}

function bezierX(t, p0, p1, p2) {
    return (1 - t) * (1 - t) * p0 + 2 * (1 - t) * t * p1 + t * t * p2;
}
describe('TestFindTForX', () => {
    test('findTForX at start', () => {
        const p0 = 0.0, p1 = 0.5, p2 = 1.0;
        const targetX = 0.0;
        const t = findTForX(targetX, p0, p1, p2);
        expect(t).toBeCloseTo(0.0, TOLERANCE);
    });

    test('findTForX at end', () => {
        const p0 = 0.0, p1 = 0.5, p2 = 1.0;
        const targetX = 1.0;
        const t = findTForX(targetX, p0, p1, p2);
        expect(t).toBeCloseTo(1.0, TOLERANCE);
    });

    test('findTForX mid curve', () => {
        const p0 = 0.0, p1 = 0.5, p2 = 1.0;
        const targetX = 0.25;
        const t = findTForX(targetX, p0, p1, p2);
        expect(t).toBeCloseTo(0.25, TOLERANCE);
    });

    test('findTForX near mid curve', () => {
        const p0 = 0.0, p1 = 1.0, p2 = 2.0;
        const targetX = 1.5;
        const t = findTForX(targetX, p0, p1, p2);
        expect(t).toBeCloseTo(0.75, TOLERANCE);
    });
});
