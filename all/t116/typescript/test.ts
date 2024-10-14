describe('toroidalDiff', () => {
    test('should return the direct difference when no wrapping is needed', () => {
        const thisPoint: Point = { x: 2, y: 3 };
        const otherPoint: Point = { x: 5, y: 6 };
        const width = 10;
        const height = 10;
        const result = toroidalDiff(thisPoint, otherPoint, width, height);
        expect(result).toEqual([-3, -3]);
    });

    test('should handle wrapping around the x dimension', () => {
        const thisPoint: Point = { x: 9, y: 5 };
        const otherPoint: Point = { x: 1, y: 5 };
        const width = 10;
        const height = 10;
        const result = toroidalDiff(thisPoint, otherPoint, width, height);
        expect(result).toEqual([-2, 0]); // dx wraps around the toroidal boundary
    });

    test('should handle wrapping around the y dimension', () => {
        const thisPoint: Point = { x: 4, y: 9 };
        const otherPoint: Point = { x: 4, y: 1 };
        const width = 10;
        const height = 10;
        const result = toroidalDiff(thisPoint, otherPoint, width, height);
        expect(result).toEqual([0, -2]); // dy wraps around the toroidal boundary
    });

    test('should handle wrapping around both x and y dimensions', () => {
        const thisPoint: Point = { x: 9, y: 9 };
        const otherPoint: Point = { x: 1, y: 1 };
        const width = 10;
        const height = 10;
        const result = toroidalDiff(thisPoint, otherPoint, width, height);
        expect(result).toEqual([-2, -2]); // Both dx and dy wrap around
    });

    test('should return the direct difference for points at the same position', () => {
        const thisPoint: Point = { x: 5, y: 5 };
        const otherPoint: Point = { x: 5, y: 5 };
        const width = 10;
        const height = 10;
        const result = toroidalDiff(thisPoint, otherPoint, width, height);
        expect(result).toEqual([0, 0]); // No difference
    });
});