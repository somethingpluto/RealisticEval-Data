// Define the Coordinates type to represent a point in 2D space
type Coordinates = {
    x: number;
    y: number;
};

/**
 * Recursively calculates a point on a Bézier curve using De Casteljau's algorithm.
 *
 * @param t - A value between 0 and 1 representing the interpolation parameter.
 * @param points - An array of control points defining the Bézier curve.
 * @returns The calculated Coordinates at the given parameter t.
 */
function getBezierPoint(t: number, points: Coordinates[]): Coordinates {
    // If there's only one point, return it as the result
    if (points.length === 1) {
        return points[0];
    }

    // Create an array to hold the points for the next iteration
    const nextPoints: Coordinates[] = [];

    // Calculate the intermediate points for the next iteration
    for (let i = 0; i < points.length - 1; i++) {
        const x = (1 - t) * points[i].x + t * points[i + 1].x;
        const y = (1 - t) * points[i].y + t * points[i + 1].y;
        nextPoints.push({ x, y });
    }

    // Recursively call getBezierPoint with the new points
    return getBezierPoint(t, nextPoints);
}
