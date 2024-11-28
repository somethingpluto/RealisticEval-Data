function squaredEuclideanDistance(vec1: number[], vec2: number[]): number {
    /**
     * Compute the squared Euclidean distance between two vectors.
     *
     * @param {number[]} vec1 - First vector.
     * @param {number[]} vec2 - Second vector.
     * @returns {number} - Euclidean distance between vec1 and vec2.
     */
    if (vec1.length !== vec2.length) {
        throw new Error("Vectors must have the same length");
    }

    let sum = 0;
    for (let i = 0; i < vec1.length; i++) {
        sum += Math.pow(vec1[i] - vec2[i], 2);
    }
    return sum;
}
describe('SquaredEuclideanDistance', () => {
    describe('test_standard_vectors', () => {
        it('should calculate the squared distance correctly for typical vectors', () => {
            const vec1 = [1, 2, 3];
            const vec2 = [4, 5, 6];
            const expectedResult = 27; // (3^2 + 3^2 + 3^2)
            const result = squaredEuclideanDistance(vec1, vec2);
            expect(result).toBe(expectedResult);
        });
    });

    describe('test_vectors_with_zeros', () => {
        it('should handle vectors that include zero values', () => {
            const vec1 = [0, 0, 0];
            const vec2 = [0, 0, 0];
            const expectedResult = 0;
            const result = squaredEuclideanDistance(vec1, vec2);
            expect(result).toBe(expectedResult);
        });
    });

    describe('test_vectors_with_negative_values', () => {
        it('should handle vectors that include negative values', () => {
            const vec1 = [-1, -2, -3];
            const vec2 = [-4, -5, -6];
            const expectedResult = 27; // (3^2 + 3^2 + 3^2)
            const result = squaredEuclideanDistance(vec1, vec2);
            expect(result).toBe(expectedResult);
        });
    });

    describe('test_single_element_vectors', () => {
        it('should handle single element vectors', () => {
            const vec1 = [5];
            const vec2 = [-5];
            const expectedResult = 100; // (10^2)
            const result = squaredEuclideanDistance(vec1, vec2);
            expect(result).toBe(expectedResult);
        });
    });
});
