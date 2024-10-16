/**
 * Calculate the coordinates of a cubic Bézier curve at a given parameter t (typically between 0 and 1).
 * @param t  A number representing the parameter along the curve, where 0 <= t <= 1.
 * @param p0 A tuple of numbers representing the x and y coordinates of the start point.
 * @param p1 A tuple of numbers representing the x and y coordinates of the first control point.
 * @param p2 A tuple of numbers representing the x and y coordinates of the second control point.
 * @param p3 A tuple of numbers representing the x and y coordinates of the end point.
 * @return   A tuple of numbers containing the x and y coordinates of the point on the curve corresponding to the parameter t.
 */
function cubicBezier(
    t: number,
    p0: [number, number],
    p1: [number, number],
    p2: [number, number],
    p3: [number, number]
): [number, number] {
    const x = Math.pow(1 - t, 3) * p0[0]
            + 3 * Math.pow(1 - t, 2) * t * p1[0]
            + 3 * (1 - t) * Math.pow(t, 2) * p2[0]
            + Math.pow(t, 3) * p3[0];

    const y = Math.pow(1 - t, 3) * p0[1]
            + 3 * Math.pow(1 - t, 2) * t * p1[1]
            + 3 * (1 - t) * Math.pow(t, 2) * p2[1]
            + Math.pow(t, 3) * p3[1];

    return [x, y];
}