// ... (previous code for context)
function reverseRange(v: number[], a: number, b: number): void {
  if (a < 0 || b >= v.length || a > b) {
    throw new Error('Invalid range');
  }
  while (a < b) {
    [v[a], v[b]] = [v[b], v[a]];
    a++;
    b--;
  }
}
// ... (continuation of the code)
describe("reverseRange function", () => {
    test("Reverse entire array", () => {
        const v = [1, 2, 3, 4, 5];
        reverseRange(v, 0, 4);
        const expected = [5, 4, 3, 2, 1];
        expect(v).toEqual(expected);
    });

    test("Reverse subrange in the middle", () => {
        const v = [1, 2, 3, 4, 5, 6, 7, 8];
        reverseRange(v, 2, 5);
        const expected = [1, 2, 6, 5, 4, 3, 7, 8];
        expect(v).toEqual(expected);
    });

    test("Reverse a single element range", () => {
        const v = [1, 2, 3, 4, 5];
        reverseRange(v, 2, 2);
        const expected = [1, 2, 3, 4, 5];
        expect(v).toEqual(expected);
    });

    test("Reverse range with invalid indices", () => {
        const v = [1, 2, 3, 4, 5];
        reverseRange(v, -1, 3);  // Invalid start index
        const expected = [1, 2, 3, 4, 5]; // No change
        expect(v).toEqual(expected);
    });

    test("Reverse range at the end of the array", () => {
        const v = [1, 2, 3, 4, 5, 6];
        reverseRange(v, 3, 5);
        const expected = [1, 2, 3, 6, 5, 4];
        expect(v).toEqual(expected);
    });
});
