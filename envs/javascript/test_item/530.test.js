/**
 * Creates a matrix with the specified number of rows and columns,
 * filled with the given initial value.
 *
 * @param {number} rows - The number of rows in the matrix.
 * @param {number} columns - The number of columns in the matrix.
 * @param {*} initialValue - The value to fill the matrix with.
 *                          It can be of any type (number, string, object, etc.).
 * @returns {Array} A two-dimensional array (matrix) filled with the initial value.
 */
function createMatrix(rows, columns, initialValue) {
    const matrix = [];
    for (let i = 0; i < rows; i++) {
        const row = [];
        for (let j = 0; j < columns; j++) {
            row.push(initialValue);
        }
        matrix.push(row);
    }
    return matrix;
}
describe('createMatrix', () => {
    test('should create a 2x2 matrix filled with zeros', () => {
        const result = createMatrix(2, 2, 0);
        expect(result).toEqual([[0, 0], [0, 0]]);
    });

    test('should create a 3x3 matrix filled with ones', () => {
        const result = createMatrix(3, 3, 1);
        expect(result).toEqual([[1, 1, 1], [1, 1, 1], [1, 1, 1]]);
    });

    test('should create a 4x5 matrix filled with a string', () => {
        const result = createMatrix(4, 5, 'test');
        expect(result).toEqual([
            ['test', 'test', 'test', 'test', 'test'],
            ['test', 'test', 'test', 'test', 'test'],
            ['test', 'test', 'test', 'test', 'test'],
            ['test', 'test', 'test', 'test', 'test'],
        ]);
    });

    test('should create a 0x0 matrix', () => {
        const result = createMatrix(0, 0, null);
        expect(result).toEqual([]);
    });

    test('should create a 1x1 matrix with a boolean', () => {
        const result = createMatrix(1, 1, true);
        expect(result).toEqual([[true]]);
    });
    test('should create a 5x5 matrix filled with negative numbers', () => {
        const result = createMatrix(5, 5, -1);
        expect(result).toEqual([
            [-1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1],
        ]);
    });

});
