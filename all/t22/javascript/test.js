describe('TestCalculateEuclideanDistance', () => {
    it('should calculate the distance correctly', () => {
        const point1 = [0, 0];
        const point2 = [3, 4];
        const expectedDistance = 5.0;
        expect(calculateEuclideanDistance(point1, point2)).toBe(expectedDistance);
    });

    it('should handle negative coordinates correctly', () => {
        const point1 = [-1, -1];
        const point2 = [-4, -5];
        const expectedDistance = 5.0;
        expect(calculateEuclideanDistance(point1, point2)).toBe(expectedDistance);
    });

    it('should return 0 when both points are the same', () => {
        const point1 = [2, 3];
        const point2 = [2, 3];
        const expectedDistance = 0.0;
        expect(calculateEuclideanDistance(point1, point2)).toBe(expectedDistance);
    });

    it('should handle large coordinates correctly', () => {
        const point1 = [1e6, 1e6];
        const point2 = [1e6 + 3, 1e6 + 4];
        const expectedDistance = 5.0;
        expect(calculateEuclideanDistance(point1, point2)).toBe(expectedDistance);
    });

    it('should throw a TypeError for invalid input', () => {
        expect(() => calculateEuclideanDistance("invalid", [0, 0])).toThrow(TypeError);
    });
});