/**
 * Calculate the maximum width of each column in a list of lists where each sub-list represents a row of table data.
 *
 * @param {Array<Array<string>>} data - A two-dimensional array containing rows of data, where each inner array contains string elements representing the values in each column.
 * @returns {Array<number>} An array containing the maximum width (in characters) of each column across all rows. The width of a column is defined by the longest string present in that column.
 */
function calculateColumnWidths(data) {
    if (data.length === 0) return [];

    const numColumns = data[0].length;
    const columnWidths = new Array(numColumns).fill(0);

    for (const row of data) {
        for (let col = 0; col < numColumns; col++) {
            const cellWidth = row[col].length;
            if (cellWidth > columnWidths[col]) {
                columnWidths[col] = cellWidth;
            }
        }
    }

    return columnWidths;
}
describe('TestCalculateColumnWidths', () => {

    it('should handle a standard case', () => {
        const data = [
            ["Name", "Age", "City"],
            ["Alice", "22", "New York"],
            ["Bob", "30", "San Francisco"]
        ];
        const expected = [5, 3, 13];
        expect(calculateColumnWidths(data)).toEqual(expected);
    });

    it('should handle a single element case', () => {
        const data = [["Name"]];
        const expected = [4];
        expect(calculateColumnWidths(data)).toEqual(expected);
    });

    it('should handle varied length cases', () => {
        const data = [
            ["a", "bb", "ccc"],
            ["dddd", "ee", "f"]
        ];
        const expected = [4, 2, 3];
        expect(calculateColumnWidths(data)).toEqual(expected);
    });

    it('should handle all empty strings', () => {
        const data = [
            ["", "", ""],
            ["", "", ""]
        ];
        const expected = [0, 0, 0];
        expect(calculateColumnWidths(data)).toEqual(expected);
    });

    it('should handle mixed content', () => {
        const data = [
            ["1234", "567", "890"],
            ["abc", "defg", "h"]
        ];
        const expected = [4, 4, 3];
        expect(calculateColumnWidths(data)).toEqual(expected);
    });

    it('should handle a single column with multiple rows', () => {
        const data = [
            ["one"],
            ["two"],
            ["three"]
        ];
        const expected = [5];
        expect(calculateColumnWidths(data)).toEqual(expected);
    });
});
