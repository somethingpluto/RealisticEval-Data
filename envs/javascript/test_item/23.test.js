/**
 * Calculates the intersection point of two line segments, if it exists.
 *
 * @param {Array} seg1 - Coordinates of the first line segment, defined as [[x1, y1], [x2, y2]].
 * @param {Array} seg2 - Coordinates of the second line segment, defined as [[x3, y3], [x4, y4]].
 * @returns {Array|null} - The [x, y] coordinates of the intersection point if the line segments intersect,
 *                         otherwise null.
 */
function getLineSegmentIntersection(seg1, seg2) {
    const [p1, p2] = seg1;
    const [p3, p4] = seg2;

    const x1 = p1[0], y1 = p1[1];
    const x2 = p2[0], y2 = p2[1];
    const x3 = p3[0], y3 = p3[1];
    const x4 = p4[0], y4 = p4[1];

    const denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1);

    if (denom === 0) {
        return null; // Lines are parallel
    }

    const ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom;
    const ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denom;

    if (ua < 0 || ua > 1 || ub < 0 || ub > 1) {
        return null; // Intersection point is outside the segments
    }

    const x = x1 + ua * (x2 - x1);
    const y = y1 + ua * (y2 - y1);

    return [x, y];
}
describe('TestLineSegmentIntersection', () => {
    it('should find the intersection at (2.5, 2.5)', () => {
        const seg1 = [[1, 1], [4, 4]];
        const seg2 = [[1, 4], [4, 1]];
        const expected = [2.5, 2.5];
        const result = getLineSegmentIntersection(seg1, seg2);
        expect(result).toEqual(expected);
    });

    it('should return null when there is no intersection', () => {
        const seg1 = [[1, 1], [2, 2]];
        const seg2 = [[3, 3], [4, 4]];
        const result = getLineSegmentIntersection(seg1, seg2);
        expect(result).toBeNull();
    });

    it('should return null for parallel segments', () => {
        const seg1 = [[1, 1], [2, 2]];
        const seg2 = [[1, 2], [2, 3]];
        const result = getLineSegmentIntersection(seg1, seg2);
        expect(result).toBeNull();
    });

    it('should return null when there is no intersection due to offset', () => {
        const seg1 = [[1, 1], [3, 3]];
        const seg2 = [[3, 2], [4, 2]];
        const result = getLineSegmentIntersection(seg1, seg2);
        expect(result).toBeNull();
    });

    it('should find the intersection at (1500.0, 1500.0) with large coordinates', () => {
        const seg1 = [[1000, 1000], [2000, 2000]];
        const seg2 = [[1000, 2000], [2000, 1000]];
        const expected = [1500.0, 1500.0];
        const result = getLineSegmentIntersection(seg1, seg2);
        expect(result).toEqual(expected);
    });
});
