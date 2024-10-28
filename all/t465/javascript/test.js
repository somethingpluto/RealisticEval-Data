const math = require('mathjs');

describe('TestMatrixVectorMultiplication', () => {
    it('test_case_1', () => {
        // Test with a simple 2x2 matrix and a 2-element vector
        const matrix = [[1, 2], [3, 4]];
        const vector = [5, 6];
        const expected_result = [17, 39];  // [1*5 + 2*6, 3*5 + 4*6]
        expect(matrixVectorMultiplication(matrix, vector)).toEqual(expected_result);
    });

    it('test_case_2', () => {
        // Test with a 3x3 matrix and a 3-element vector
        const matrix = [[1, 0, 2], [0, 1, 2], [1, 1, 0]];
        const vector = [3, 4, 5];
        const expected_result = [13, 14, 7];  // [1*3 + 0*4 + 2*5, 0*3 + 1*4 + 2*5, 1*3 + 1*4 + 0*5]
        expect(matrixVectorMultiplication(matrix, vector)).toEqual(expected_result);
    });

    it('test_case_3', () => {
        // Test with a zero matrix and a vector
        const matrix = [[0, 0], [0, 0]];
        const vector = [1, 1];
        const expected_result = [0, 0];  // Zero matrix multiplied by any vector yields zero
        expect(matrixVectorMultiplication(matrix, vector)).toEqual(expected_result);
    });

    it('test_case_4', () => {
        // Test with a matrix having negative values
        const matrix = [[-1, -2], [-3, -4]];
        const vector = [1, 1];
        const expected_result = [-3, -7];  // [-1*1 + -2*1, -3*1 + -4*1]
        expect(matrixVectorMultiplication(matrix, vector)).toEqual(expected_result);
    });

    it('test_case_5', () => {
        // Test with non-square matrix (2x3) and a compatible vector (3-element)
        const matrix = [[1, 2, 3], [4, 5, 6]];
        const vector = [1, 0, 1];
        const expected_result = [4, 10];  // [1*1 + 2*0 + 3*1, 4*1 + 5*0 + 6*1]
        expect(matrixVectorMultiplication(matrix, vector)).toEqual(expected_result);
    });
});