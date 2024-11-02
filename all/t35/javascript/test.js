describe('TestPointInPolygon', () => {
    let square = [[0, 0], [0, 10], [10, 10], [10, 0]];
    let triangle = [[0, 0], [5, 10], [10, 0]];
    let concave = [[0, 0], [5, 5], [10, 0], [5, 10], [0, 10]];

    it('should determine if a point is inside the square', () => {
        // Point inside the square
        expect(isPointInPolygon([5, 5], square)).toBe(true);
    });

    it('should determine if a point is outside the square', () => {
        // Point outside the square
        expect(isPointInPolygon([15, 5], square)).toBe(false);
    });

    it('should determine if a point is on the edge of the triangle', () => {
        // Point on the edge of the triangle
        expect(isPointInPolygon([5, 0], triangle)).toBe(false);
    });

    it('should determine if a point is inside a concave polygon', () => {
        // Point inside concave polygon
        expect(isPointInPolygon([5, 9], concave)).toBe(true);
    });

    it('should determine if a point is outside a concave polygon', () => {
        // Point outside concave polygon
        expect(isPointInPolygon([5, 1], concave)).toBe(false);
    });
});