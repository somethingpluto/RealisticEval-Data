describe('squaredEuclideanDistance', () => {

    it('should calculate the squared euclidean distance correctly', () => {
        const vec1 = [3, 4];
        const vec2 = [6, 8];
        expect(squaredEuclideanDistance(vec1, vec2)).toBe(25);
    });

    it('should handle vectors of different lengths', () => {
        const vec1 = [1, 2, 3];
        const vec2 = [4, 5];
        expect(() => squaredEuclideanDistance(vec1, vec2)).toThrowError();
    });
});