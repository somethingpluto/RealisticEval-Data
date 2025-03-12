/**
 * Transpose a given matrix (2D array).
 *
 * @param {Array<Array<number>>} matrix - The input 2D array to be transposed.
 * @returns {Array<Array<number>>} The transposed 2D array.
 */
function transposeMatrix(matrix) {
    // Check if the matrix is empty or not a valid 2D array
    if (!Array.isArray(matrix) || matrix.length === 0 || !Array.isArray(matrix[0]) || matrix[0].length === 0) {
        return [];
    }

    // Get the number of rows and columns in the original matrix
    const rows = matrix.length;
    const cols = matrix[0].length;

    // Initialize the transposed matrix with the correct dimensions
    const transposedMatrix = Array.from({ length: cols }, () => Array(rows).fill(0));

    // Fill the transposed matrix
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            transposedMatrix[j][i] = matrix[i][j];
        }
    }

    return transposedMatrix;
}
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
