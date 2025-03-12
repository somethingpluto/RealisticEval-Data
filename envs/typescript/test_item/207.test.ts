function minChangesToSymmetric(matrix: string[][]): number {
  const n = matrix.length;
  let changes = 0;

  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      if (matrix[i][j] !== matrix[j][i]) {
        changes += Math.abs(matrix[i][j].charCodeAt(0) - matrix[j][i].charCodeAt(0));
        matrix[i][j] = matrix[j][i];
      }
    }
  }

  return changes;
}
describe("Testing minChangesToSymmetric function", () => {

    test("Already Symmetric Matrix", () => {
        const matrix: string[][] = [
            ['a', 'b', 'c'],
            ['b', 'e', 'f'],
            ['c', 'f', 'i']
        ];
        expect(minChangesToSymmetric(matrix)).toBe(0);
    });

    test("One Change Needed", () => {
        const matrix: string[][] = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['c', 'h', 'i']
        ];
        expect(minChangesToSymmetric(matrix)).toBe(2);
    });

    test("All Different Elements", () => {
        const matrix: string[][] = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i']
        ];
        expect(minChangesToSymmetric(matrix)).toBe(3);
    });

    test("Large Symmetric Matrix", () => {
        const matrix: string[][] = [
            ['a', 'b', 'c', 'd'],
            ['b', 'e', 'f', 'g'],
            ['c', 'f', 'h', 'i'],
            ['d', 'g', 'i', 'j']
        ];
        expect(minChangesToSymmetric(matrix)).toBe(0);
    });

    test("Multiple Changes Needed", () => {
        const matrix: string[][] = [
            ['a', 'x', 'c', 'd'],
            ['y', 'e', 'f', 'g'],
            ['z', 'h', 'i', 'j'],
            ['d', 'g', 'k', 'l']
        ];
        expect(minChangesToSymmetric(matrix)).toBe(4);
    });

});
