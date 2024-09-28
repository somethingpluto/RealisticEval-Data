import { isPointInPolygon } from './path-to-your-isPointInPolygon-file'; // Adjust the import path

describe('isPointInPolygon', () => {
    let square: [number, number][];
    let triangle: [number, number][];
    let concave: [number, number][];

    beforeEach(() => {
        // Define some polygons to use in tests
        square = [[0, 0], [0, 10], [10, 10], [10, 0]];
        triangle = [[0, 0], [5, 10], [10, 0]];
        concave = [[0, 0], [5, 5], [10, 0], [5, 10], [0, 10]];
    });

    test('Point inside the square', () => {
        // Point inside the square
        expect(isPointInPolygon([5, 5], square)).toBe(true);
    });

    test('Point outside the square', () => {
        // Point outside the square
        expect(isPointInPolygon([15, 5], square)).toBe(false);
    });

    test('Point on the edge of the triangle', () => {
        // Point on the edge of the triangle
        expect(isPointInPolygon([5, 0], triangle)).toBe(false);
    });

    test('Point inside concave polygon', () => {
        // Point inside the concave polygon
        expect(isPointInPolygon([5, 9], concave)).toBe(true);
    });

    test('Point outside concave polygon', () => {
        // Point outside the concave polygon
        expect(isPointInPolygon([5, 1], concave)).toBe(false);
    });
});