/**
 * Generates the ith row of Pascal's Triangle.
 *
 * @param {number} i - Row index (0-indexed)
 * @return {Array<number>} An array representing the ith row of Pascal's Triangle
 */
function pascalTriangleRow(i) {
    if (i === 0) {
        return [1];
    }

    let row = [1];

    for (let j = 1; j < i; j++) {
        row[j] = row[j - 1] * (i - j + 1) / j;
    }

    row.push(1);

    return row;
}
describe('TestPascalTriangleRow', () => {
    it('test_row_0', () => {
        /** Test the 0th row of Pascal's Triangle. */
        expect(pascalTriangleRow(0)).toEqual([1]);
    });

    it('test_row_1', () => {
        /** Test the 1st row of Pascal's Triangle. */
        expect(pascalTriangleRow(1)).toEqual([1, 1]);
    });

    it('test_row_2', () => {
        /** Test the 2nd row of Pascal's Triangle. */
        expect(pascalTriangleRow(2)).toEqual([1, 2, 1]);
    });

    it('test_row_3', () => {
        /** Test the 3rd row of Pascal's Triangle. */
        expect(pascalTriangleRow(3)).toEqual([1, 3, 3, 1]);
    });

    it('test_row_4', () => {
        /** Test the 4th row of Pascal's Triangle. */
        expect(pascalTriangleRow(4)).toEqual([1, 4, 6, 4, 1]);
    });

    it('test_row_5', () => {
        /** Test the 5th row of Pascal's Triangle. */
        expect(pascalTriangleRow(5)).toEqual([1, 5, 10, 10, 5, 1]);
    });
});

