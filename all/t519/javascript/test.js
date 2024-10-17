describe('TestTransposeMatrix', () => {
    it('test_square_matrix', () => {
        // Test transposing a square matrix
        const matrix = [[1, 2], [3, 4]];
        const expected = [[1, 3], [2, 4]];
        const result = transposeMatrix(matrix);
        expect(result).toEqual(expected);
    });

    it('test_rectangular_matrix', () => {
        // Test transposing a rectangular matrix
        const matrix = [[1, 2, 3], [4, 5, 6]];
        const expected = [[1, 4], [2, 5], [3, 6]];
        const result = transposeMatrix(matrix);
        expect(result).toEqual(expected);
    });

    it('test_matrix_with_empty_rows', () => {
        // Test transposing a matrix with an empty row
        const matrix = [[], []];
        const expected = [];
        const result = transposeMatrix(matrix);
        expect(result).toEqual(expected);
    });

    it('test_single_element_matrix', () => {
        // Test transposing a matrix with a single element
        const matrix = [[5]];
        const expected = [[5]];
        const result = transposeMatrix(matrix);
        expect(result).toEqual(expected);
    });
});