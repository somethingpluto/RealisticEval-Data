describe('TestMinRemovalsToMakeUnique', () => {
  test('test_basic_array', () => {
      /** Test with a basic array where multiple removals are needed. */
      expect(minRemovalsToMakeUnique([3, 3, 1, 2, 2, 1])).toBe(3);
  });

  test('test_all_identical', () => {
      /** Test an array where all elements are identical. */
      expect(minRemovalsToMakeUnique([4, 4, 4, 4])).toBe(3);
  });

  test('test_all_unique', () => {
      /** Test an array where all elements are already unique. */
      expect(minRemovalsToMakeUnique([1, 2, 3, 4])).toBe(0);
  });

  test('test_empty_array', () => {
      /** Test an empty array. */
      expect(minRemovalsToMakeUnique([])).toBe(0);
  });

  test('test_complex_case', () => {
      /** Test a more complex case with a larger array. */
      expect(minRemovalsToMakeUnique([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])).toBe(6);
  });
});