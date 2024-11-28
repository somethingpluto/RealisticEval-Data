function squaredEuclideanDistance(vec1, vec2) {
    if (vec1.length !== vec2.length) {
        throw new Error('Vectors must have same length');
    }

    let sum = 0;
    for(let i=0; i<vec1.length; i++) {
        sum += Math.pow(vec1[i] - vec2[i], 2);
    }

    return sum;
}
describe('SquaredEuclideanDistance', () => {
    it('test standard vectors', () => {
        const vec1 = [1, 2, 3];
        const vec2 = [4, 5, 6];
        const expectedResult = 27; // (3^2 + 3^2 + 3^2)
        const result = squaredEuclideanDistance(vec1, vec2);
        expect(result).toBe(expectedResult);
    });

    it('test vectors with zeros', () => {
        const vec1 = [0, 0, 0];
        const vec2 = [0, 0, 0];
        const expectedResult = 0;
        const result = squaredEuclideanDistance(vec1, vec2);
        expect(result).toBe(expectedResult);
    });

    it('test vectors with negative values', () => {
        const vec1 = [-1, -2, -3];
        const vec2 = [-4, -5, -6];
        const expectedResult = 27; // (3^2 + 3^2 + 3^2)
        const result = squaredEuclideanDistance(vec1, vec2);
        expect(result).toBe(expectedResult);
    });

    it('test single element vectors', () => {
        const vec1 = [5];
        const vec2 = [-5];
        const expectedResult = 100; // (10^2)
        const result = squaredEuclideanDistance(vec1, vec2);
        expect(result).toBe(expectedResult);
    });
});
