describe('calculateEuclideanDistance', () => {
    test('should calculate the Euclidean distance between two points correctly', () => {
        const point1 = [3, 4];
        const point2 = [6, 8];
        const expectedDistance = 5;

        expect(calculateEuclideanDistance(point1, point2)).toBe(expectedDistance);
    });

    test('should handle floating-point coordinates correctly', () => {
        const point1 = [0.5, 0.5];
        const point2 = [1.5, 2.5];
        const expectedDistance = Math.sqrt(2);

        expect(calculateEuclideanDistance(point1, point2)).toBeCloseTo(expectedDistance, 6);
    });

    test('should handle points with negative coordinates correctly', () => {
        const point1 = [-1, -1];
        const point2 = [1, 1];
        const expectedDistance = 2 * Math.sqrt(2);

        expect(calculateEuclideanDistance(point1, point2)).toBe(expectedDistance);
    });
});