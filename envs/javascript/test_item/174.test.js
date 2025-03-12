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
    const MAX_ITERATIONS = 100;
    const TOLERANCE = 1e-6;

    // Helper function to evaluate the x-coordinate of the Bézier curve at a given t
    function bezierX(t) {
        return (1 - t) * (1 - t) * p0.x + 2 * (1 - t) * t * p1.x + t * t * p2.x;
    }

    // Initial guesses for the secant method
    let t0 = 0;
    let t1 = 1;
    let x0 = bezierX(t0);
    let x1 = bezierX(t1);

    // Iterate using the secant method
    for (let i = 0; i < MAX_ITERATIONS; i++) {
        // Calculate the next t using the secant method formula
        let tNext = t1 - (x1 - targetX) * ((t1 - t0) / (x1 - x0));

        // Evaluate the x-coordinate at the new t
        let xNext = bezierX(tNext);

        // Check if the new t is close enough to the targetX
        if (Math.abs(xNext - targetX) < TOLERANCE) {
            return tNext;
        }

        // Update the values for the next iteration
        t0 = t1;
        t1 = tNext;
        x0 = x1;
        x1 = xNext;
    }

    // If no precise value is found, return the best approximation
    return t1;
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
