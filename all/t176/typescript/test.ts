describe('findKNearestNeighbors', () => {
    
    const containsPoint = (points: Point[], point: Point): boolean => {
        return points.some(p => 
            Math.abs(p.x - point.x) < 0.001 && Math.abs(p.y - point.y) < 0.001
        );
    };

    test('simple case', () => {
        const points: Point[] = [
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

    test('exact match', () => {
        const points: Point[] = [
            new Point(1, 2),
            new Point(2, 2),
            new Point(3, 3)
        ];
        const queryPoint = new Point(2, 2);
        const k = 1;
        const result = findKNearestNeighbors(points, queryPoint, k);

        expect(result.length).toBe(1);
        expect(Math.abs(result[0].x - 2.0)).toBeLessThan(0.001);
        expect(Math.abs(result[0].y - 2.0)).toBeLessThan(0.001);
    });

    test('larger k', () => {
        const points: Point[] = [
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

    test('empty points', () => {
        const points: Point[] = [];
        const queryPoint = new Point(2, 2);
        const k = 3;
        const result = findKNearestNeighbors(points, queryPoint, k);

        expect(result.length).toBe(0);
    });

    test('all points equidistant', () => {
        const points: Point[] = [
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