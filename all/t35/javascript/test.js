const isPointInPolygon = require('./path/to/your/function'); // Adjust the path accordingly

describe('Point in Polygon Tests', () => {
    let square, triangle, concave;

    beforeEach(() => {
        // Define some polygons to use in tests
        square = [[0, 0], [0, 10], [10, 10], [10, 0]];
        triangle = [[0, 0], [5, 10], [10, 0]];
        concave = [[0, 0], [5, 5], [10, 0], [5, 10], [0, 10]];
    });

    test('Point inside square', () => {
        // Point inside the square
        expect(isPointInPolygon([5, 5], square)).toBe(true);
    });

    test('Point outside square', () => {
        // Point outside the square
        expect(isPointInPolygon([15, 5], square)).toBe(false);
    });

    test('Point on edge of triangle', () => {
        // Point on the edge of the triangle
        expect(isPointInPolygon([5, 0], triangle)).toBe(false);
    });

    test('Point inside concave polygon', () => {
        // Point inside concave polygon
        expect(isPointInPolygon([5, 9], concave)).toBe(true);
    });

    test('Point outside concave polygon', () => {
        // Point outside concave polygon
        expect(isPointInPolygon([5, 1], concave)).toBe(false);
    });
});