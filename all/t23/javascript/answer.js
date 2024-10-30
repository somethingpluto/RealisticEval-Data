/**
 * Calculate the intersection point of two line segments, if it exists.
 *
 * @param {Array} seg1 - Coordinates of the first line segment, defined as [[x1, y1], [x2, y2]].
 * @param {Array} seg2 - Coordinates of the second line segment, defined as [[x3, y3], [x4, y4]].
 * @returns {Array|null} - The [x, y] coordinates of the intersection point if the line segments intersect,
 *                         otherwise null.
 */
function getLineSegmentIntersection(seg1, seg2) {
    const [x1, y1] = seg1[0];
    const [x2, y2] = seg1[1];
    const [x3, y3] = seg2[0];
    const [x4, y4] = seg2[1];
    const dx1 = x2 - x1;
    const dy1 = y2 - y1;
    const dx2 = x4 - x3;
    const dy2 = y4 - y3;
    const determinant = dx1 * dy2 - dx2 * dy1;
    if (Math.abs(determinant) < 1e-10) {
        return null;
    }
    const t1 = ((x3 - x1) * dy2 - (y3 - y1) * dx2) / determinant;
    const t2 = ((x3 - x1) * dy1 - (y3 - y1) * dx1) / determinant;
    const tolerance = 1e-10;
    if (0 - tolerance <= t1 && t1 <= 1 + tolerance && 0 - tolerance <= t2 && t2 <= 1 + tolerance) {
        const x = x1 + t1 * dx1;
        const y = y1 + t1 * dy1;
        return [parseFloat(x.toFixed(7)), parseFloat(y.toFixed(7))];
    }
    return null;
}