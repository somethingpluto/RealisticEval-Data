function getLineSegmentIntersection(seg1, seg2) {
    /**
     * Calculate the intersection point of two line segments, if it exists.
     *
     * @param {Array} seg1 - Coordinates of the first line segment, defined as [[x1, y1], [x2, y2]].
     * @param {Array} seg2 - Coordinates of the second line segment, defined as [[x3, y3], [x4, y4]].
     * @returns {Array|null} - The [x, y] coordinates of the intersection point if the line segments intersect,
     *                        otherwise null.
     */

    // Extract points
    const [[x1, y1], [x2, y2]] = seg1;
    const [[x3, y3], [x4, y4]] = seg2;

    // Calculate denominators
    const denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4);

    // Check if lines are parallel or coincident
    if (denominator === 0) return null;

    // Calculate intersection point
    const t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denominator;
    const u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denominator;

    // Check if intersection point lies on both segments
    if (t >= 0 && t <= 1 && u >= 0 && u <= 1) {
        return [(x1 + t * (x2 - x1)), (y1 + t * (y2 - y1))];
    }

    return null;
}