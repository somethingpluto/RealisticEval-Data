describe('getLineSegmentIntersection', () => {
    test('intersecting lines', () => {
        expect(getLineSegmentIntersection([[1, 1], [4, 4]], [[1, 4], [4, 1]])).toEqual([2.5, 2.5]);
    });

    test('parallel lines', () => {
        expect(getLineSegmentIntersection([[1, 1], [4, 4]], [[2, 2], [5, 5]])).toBeNull();
    });

    test('no intersection', () => {
        expect(getLineSegmentIntersection([[1, 1], [2, 2]], [[3, 3], [4, 4]])).toBeNull();
    });

    test('intersection in the middle', () => {
        const result = getLineSegmentIntersection([[0, 0], [4, 4]], [[0, 4], [4, 0]]);
        expect(result).not.toBeNull();
        if (result !== null) { // Type guard for precise TypeScript handling
            expect(result[0]).toBeCloseTo(2, 7);
            expect(result[1]).toBeCloseTo(2, 7);
        }
    });

    test('identical segments', () => {
        expect(getLineSegmentIntersection([[1, 1], [4, 4]], [[1, 1], [4, 4]])).toBeNull();
    });
});