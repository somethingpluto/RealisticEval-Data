describe('Point', () => {
    test('find k nearest neighbors simple case', () => {
        const points = [
            new Point(1, 2),
            new Point(3, 4),
            new Point(1, -1),
            new Point(5, 2)
        ];
        const queryPoint = new Point(2, 2);
        const k = 2;
        const result = findKNearestNeighbors(points, queryPoint, k);

        expect(result.length).toBe(2);
        expect(containsPoint(result, new Point(1, 2))).toBe(true);
        expect(containsPoint(result, new Point(3, 4))).toBe(true);
    });

    test('find k nearest neighbors exact match', () => {
        const points = [
            new Point(1, 2),
            new Point(2, 2),
            new Point(3, 3)
        ];
        const queryPoint = new Point(2, 2);
        const k = 1;
        const result = findKNearestNeighbors(points, queryPoint, k);

        expect(result.length).toBe(1);
        expect(result[0].x).toBeCloseTo(2.0, 3); // delta equivalent
        expect(result[0].y).toBeCloseTo(2.0, 3); // delta equivalent
    });

    test('find k nearest neighbors larger k', () => {
        const points = [
            new Point(1, 2),
            new Point(3, 4),
            new Point(1, -1),
            new Point(5, 2)
        ];
        const queryPoint = new Point(2, 2);
        const k = 5; // k is larger than the number of points
        const result = findKNearestNeighbors(points, queryPoint, k);

        expect(result.length).toBe(4);
    });

    test('find k nearest neighbors empty points', () => {
        const points = [];
        const queryPoint = new Point(2, 2);
        const k = 3;
        const result = findKNearestNeighbors(points, queryPoint, k);

        expect(result.length).toBe(0);
    });

    test('find k nearest neighbors all points equidistant', () => {
        const points = [
            new Point(2, 3),
            new Point(3, 2),
            new Point(1, 2),
            new Point(2, 1)
        ];
        const queryPoint = new Point(2, 2);
        const k = 2;
        const result = findKNearestNeighbors(points, queryPoint, k);

        expect(result.length).toBe(2);
        expect(containsPoint(result, new Point(2, 3))).toBe(true);
        expect(containsPoint(result, new Point(3, 2))).toBe(true);
    });
});