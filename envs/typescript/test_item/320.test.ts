// At the start of your file, you might have an interface like this:
interface ArrayProcessor {
  getArrayAverage(array: number[]): number;
  // ... other methods
}

// Then, your class implementing the interface would look like this:
class ArrayProcessorImpl implements ArrayProcessor {
  getArrayAverage(array: number[]): number {
    if (array.length === 0) {
      return 0;
    }
    return array.reduce((acc, val) => acc + val, 0) / array.length;
  }
  // ... implementations of other methods
}

// And for the Jest unit tests:
describe('ArrayProcessorImpl', () => {
  const processor = new ArrayProcessorImpl();

  test('calculates the average of an array of numbers', () => {
    expect(processor.getArrayAverage([1, 2, 3, 4, 5])).toBe(3);
  });

  test('returns 0 for an empty array', () => {
    expect(processor.getArrayAverage([])).toBe(0);
  });

  // ... other tests
});
describe('getArrayAverage', () => {
    test('should return the average of an array of positive integers', () => {
        const result = getArrayAverage([1, 2, 3, 4, 5]);
        expect(result).toBe(3); // (1 + 2 + 3 + 4 + 5) / 5 = 3
    });

    test('should return the average of an array with negative numbers', () => {
        const result = getArrayAverage([-1, -2, -3, -4, -5]);
        expect(result).toBe(-3); // (-1 + -2 + -3 + -4 + -5) / 5 = -3
    });

    test('should return the average of an array with mixed positive and negative numbers', () => {
        const result = getArrayAverage([1, -1, 2, -2, 3, -3]);
        expect(result).toBe(0); // (1 + -1 + 2 + -2 + 3 + -3) / 6 = 0
    });

    test('should handle an empty array (edge case)', () => {
        const result = getArrayAverage([]);
        expect(result).toBeNaN(); // Division by zero, expected result is NaN
    });

    test('should return the single element when the array contains one item', () => {
        const result = getArrayAverage([7]);
        expect(result).toBe(7); // The average of [7] is 7
    });
});
