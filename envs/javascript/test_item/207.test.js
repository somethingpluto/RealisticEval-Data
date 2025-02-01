/**
 * Convert a given square character matrix into a symmetric matrix and calculate the minimum number of character replacements required to achieve symmetry.
 *
 * @param {Array<Array<string>>} matrix - A 2D array of characters representing the matrix to be analyzed.
 * @return {number} - The minimum number of element changes required to make the matrix symmetric.
 */
function minChangesToSymmetric(matrix) {
    let changes = 0;
    const n = matrix.length;

    for (let i = 0; i < n; i++) {
        for (let j = 0; j <= i; j++) {
            if (matrix[i][j] !== matrix[j][i]) {
                changes++;
            }
        }
    }

    return changes;
}
describe("minChangesToSymmetric function", () => {

    test("Already Symmetric Matrix", () => {
        const matrix = [
            ['a', 'b', 'c'],
            ['b', 'e', 'f'],
            ['c', 'f', 'i']
        ];
        expect(minChangesToSymmetric(matrix)).toBe(0);
    });

    test("One Change Needed", () => {
        const matrix = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['c', 'h', 'i']
        ];
        expect(minChangesToSymmetric(matrix)).toBe(2);
    });

    test("All Different Elements", () => {
        const matrix = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i']
        ];
        expect(minChangesToSymmetric(matrix)).toBe(3);
    });

    test("Large Symmetric Matrix", () => {
        const matrix = [
            ['a', 'b', 'c', 'd'],
            ['b', 'e', 'f', 'g'],
            ['c', 'f', 'h', 'i'],
            ['d', 'g', 'i', 'j']
        ];
        expect(minChangesToSymmetric(matrix)).toBe(0);
    });

    test("Multiple Changes Needed", () => {
        const matrix = [
            ['a', 'x', 'c', 'd'],
            ['y', 'e', 'f', 'g'],
            ['z', 'h', 'i', 'j'],
            ['d', 'g', 'k', 'l']
        ];
        expect(minChangesToSymmetric(matrix)).toBe(4);
    });
});
