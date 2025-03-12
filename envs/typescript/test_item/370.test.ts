// ... (previous code for context)

function decompose(n: number, shape: number[]): [number, ...number[]] {
  if (n < 0 || n >= shape.reduce((acc, val) => acc * val, 1)) {
    throw new Error('Index out of bounds');
  }
  const indices: number[] = [];
  for (let i = shape.length - 1; i >= 0; i--) {
    indices.push(Math.floor(n % shape[i]));
    n = Math.floor(n / shape[i]);
  }
  return indices.reverse() as [number, ...number[]];
}

// ... (rest of the code)
describe('TestDecomposeFunction', () => {
  it('should handle edge case with larger shape', () => {
    expect(decompose(60, [4, 4, 4])).toEqual([3, 3, 0]);
  });

  it('should handle the last valid index', () => {
    expect(decompose(63, [4, 4, 4])).toEqual([3, 3, 3]);
  });

  it('should handle single dimension case', () => {
    expect(decompose(2, [5])).toEqual([2]);
  });

  it('should throw an error for invalid cases', () => {
    // Test case 5: Out of bounds case (negative index)
    expect(() => decompose(-1, [3, 4, 5])).toThrow('Index out of bounds');

    // Test case 6: Out of bounds case (index too large)
    expect(() => decompose(100, [3, 4, 5])).toThrow('Index out of bounds');
  });
});
