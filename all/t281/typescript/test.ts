describe('squaredEuclideanDistance', () => {
    it('should calculate the squared Euclidean distance correctly', () => {
        const vec1 = [1, 2, 3];
        const vec2 = [4, 5, 6];

        const result = squaredEuclideanDistance(vec1, vec2);

        expect(result).toBe(27); // (4-1)^2 + (5-2)^2 + (6-3)^2 = 9 + 9 + 9 = 27
    });

    it('should handle vectors of different lengths', () => {
        const vec1 = [1, 2];
        const vec2 = [4, 5, 6];

        expect(() => squaredEuclideanDistance(vec1, vec2)).toThrowError('Vectors must have the same length');
    });
});