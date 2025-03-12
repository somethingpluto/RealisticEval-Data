/**
 * Determine if the point (x, y) is inside the given polygon.
 * The polygon is defined as an array of tuples [x, y] representing the vertices.
 *
 * @param {Array} point - An array [x, y] representing the point to check.
 * @param {Array} polygon - An array of arrays [x, y] representing the vertices of the polygon.
 * @returns {boolean} - True if the point is inside the polygon, False otherwise.
 */
function isPointInPolygon(point, polygon) {
    const [x, y] = point;
    let inside = false;

    for (let i = 0, j = polygon.length - 1; i < polygon.length; j = i++) {
        const [xi, yi] = polygon[i];
        const [xj, yj] = polygon[j];

        const intersect = ((yi > y) !== (yj > y)) &&
                          (x < (xj - xi) * (y - yi) / (yj - yi) + xi);
        if (intersect) inside = !inside;
    }

    return inside;
}
describe('TestPointInPolygon', () => {
    beforeEach(() => {
        // Define some polygons to use in tests
        this.square = [[0, 0], [0, 10], [10, 10], [10, 0]];
        this.triangle = [[0, 0], [5, 10], [10, 0]];
        this.concave = [[0, 0], [5, 5], [10, 0], [5, 10], [0, 10]];
    });

    it('should determine if a point is inside the square', () => {
        // Point inside the square
        expect(isPointInPolygon([5, 5], this.square)).toBe(true);
    });

    it('should determine if a point is outside the square', () => {
        // Point outside the square
        expect(isPointInPolygon([15, 5], this.square)).toBe(false);
    });

    it('should determine if a point is on the edge of the triangle', () => {
        // Point on the edge of the triangle
        expect(isPointInPolygon([5, 0], this.triangle)).toBe(false);
    });

    it('should determine if a point is inside a concave polygon', () => {
        // Point inside concave polygon
        expect(isPointInPolygon([5, 9], this.concave)).toBe(true);
    });

    it('should determine if a point is outside a concave polygon', () => {
        // Point outside concave polygon
        expect(isPointInPolygon([5, 1], this.concave)).toBe(false);
    });
});
