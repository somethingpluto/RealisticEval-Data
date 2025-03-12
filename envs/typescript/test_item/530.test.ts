// ... (previous code for context)
export function createMatrix<T>(rows: number, columns: number, initialValue: T): T[][] {
    if (rows < 0 || columns < 0) {
        throw new Error('Rows and columns must be non-negative.');
    }
    return Array.from({ length: rows }, () => Array.from({ length: columns }, () => initialValue));
}
// ... (continuation of the code if necessary)
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
