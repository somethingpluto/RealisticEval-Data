import { Vector } from './Vector';

/**
 * Computes the squared Euclidean distance between two vectors.
 *
 * @param vec1 - The first vector.
 * @param vec2 - The second vector.
 * @returns The squared Euclidean distance between vec1 and vec2.
 * @throws {Error} If the vectors are of different lengths.
 */
function squaredEuclideanDistance(vec1: Vector, vec2: Vector): number {
  if (vec1.length !== vec2.length) {
    throw new Error('Vectors must be of the same length.');
  }

  return vec1.reduce((acc, val, index) => acc + Math.pow(val - vec2[index], 2), 0);
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
