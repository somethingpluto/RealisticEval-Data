/**
 * Evaluates the quadratic Bézier curve at parameter t with given control points.
 *
 * @param t - The parameter along the Bézier curve (0 <= t <= 1).
 * @param p0 - The first control point.
 * @param p1 - The second control point.
 * @param p2 - The third control point.
 * @returns The x-coordinate of the Bézier curve at parameter t.
 */
function bezierCurve(t: number, p0: number, p1: number, p2: number): number {
    return (1 - t) * (1 - t) * p0 + 2 * (1 - t) * t * p1 + t * t * p2;
}

/**
 * Finds the parameter `t` corresponding to a given x-coordinate `targetX`
 * on a quadratic Bézier curve defined by control points p0, p1, and p2.
 * The function uses the secant method to iteratively approach the value of `t`
 * where the Bézier curve intersects with the vertical line at `targetX`.
 *
 * @param targetX - The x-coordinate for which we want to find the corresponding
 *                parameter `t` on the Bézier curve.
 * @param p0 - The first control point of the Bézier curve, representing the
 *            starting point.
 * @param p1 - The second control point of the Bézier curve, affecting the curve's
 *            shape.
 * @param p2 - The third control point of the Bézier curve, representing the
 *            ending point.
 * @returns The parameter `t` (in the range [0, 1]) for which the Bézier curve
 *         evaluated at `t` is closest to `targetX`. If no precise value is
 *         found within the specified tolerance and iterations, the function
 *         returns the best approximation.
 */
function findTForX(targetX: number, p0: number, p1: number, p2: number): number {
    let t0 = 0.0;
    let t1 = 1.0;
    const tolerance = 1e-6;
    const maxIterations = 100;

    let x0 = bezierCurve(t0, p0, p1, p2) - targetX;
    let x1 = bezierCurve(t1, p0, p1, p2) - targetX;

    for (let i = 0; i < maxIterations; i++) {
        if (Math.abs(x1 - x0) < tolerance) {
            break;
        }

        let t2 = t1 - x1 * (t1 - t0) / (x1 - x0);
        let x2 = bezierCurve(t2, p0, p1, p2) - targetX;

        if (Math.abs(x2) < tolerance) {
            return t2;
        }

        t0 = t1;
        x0 = x1;
        t1 = t2;
        x1 = x2;
    }

    return t1; // Return the best approximation found
}
