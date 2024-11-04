/**
 * Generates integer coordinates on the line from (x1, y1) to (x2, y2) using Bresenham's line algorithm.
 *
 * Bresenham's algorithm calculates the points of an approximately straight line between two given points on a grid.
 * It is particularly well-suited for computer graphics where an efficient, integer-based algorithm is needed to
 * determine which points should be rasterized to represent the line.
 *
 * @param {number} x1 - The x-coordinate of the starting point of the line.
 * @param {number} y1 - The y-coordinate of the starting point of the line.
 * @param {number} x2 - The x-coordinate of the ending point of the line.
 * @param {number} y2 - The y-coordinate of the ending point of the line.
 * @returns {Array.<Array.<number>>} An array where each sub-array contains the x and y coordinates of a point on the line.
 */
function bresenhamLine(x1, y1, x2, y2) {
    const points = [];
    
    const dx = x2 - x1;
    const dy = y2 - y1;
    const absDx = Math.abs(dx);
    const absDy = Math.abs(dy);
    const signX = dx > 0 ? 1 : -1;
    const signY = dy > 0 ? 1 : -1;

    let err = absDx - absDy;

    while (true) {
        points.push([x1, y1]); // Add the current point to the list of points

        if (x1 === x2 && y1 === y2) break; // Exit condition

        const err2 = err * 2;

        if (err2 > -absDy) {
            err -= absDy;
            x1 += signX;
        }
        if (err2 < absDx) {
            err += absDx;
            y1 += signY;
        }
    }

    return points;
}