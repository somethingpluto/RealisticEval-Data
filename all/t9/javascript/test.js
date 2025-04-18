describe('TestPointOnLine', () => {
    test('should return true when point C is on the line formed by points A and B', () => {
        const A = [0, 0];
        const B = [10, 10];
        const C = [5, 5];
        expect(isPointOnLine(A, B, C)).toBe(true);
    });

    test('should return false when point C is not on the line formed by points A and B', () => {
        const A = [0, 0];
        const B = [10, 10];
        const C = [5, 6];
        expect(isPointOnLine(A, B, C)).toBe(false);
    });

    test('should return true for a vertical line', () => {
        const A = [5, 0];
        const B = [5, 10];
        const C = [5, 5];
        expect(isPointOnLine(A, B, C)).toBe(true);
    });

    test('should return true for a horizontal line', () => {
        const A = [0, 5];
        const B = [10, 5];
        const C = [5, 5];
        expect(isPointOnLine(A, B, C)).toBe(true);
    });

    test('should return false for a point not on a vertical line', () => {
        const A = [5, 0];
        const B = [5, 10];
        const C = [6, 5];
        expect(isPointOnLine(A, B, C)).toBe(false);
    });
});