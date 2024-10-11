describe('calculateEuclideanDistance', () => {
    it('should calculate the Euclidean distance between two points correctly', () => {
        const point1: [number, number] = [0, 0];
        const point2: [number, number] = [3, 4];
        const expectedDistance = 5;

        const result = calculateEuclideanDistance(point1, point2);

        expect(result).toBe(expectedDistance);
    });

    it('should handle different coordinates', () => {
        const point1: [number, number] = [1, 2];
        const point2: [number, number] = [-1, -2];
        const expectedDistance = Math.sqrt(8); // sqrt((2-(-1))^2 + (2-(-2))^2)

        const result = calculateEuclideanDistance(point1, point2);

        expect(result).toBeCloseTo(expectedDistance);
    });
});