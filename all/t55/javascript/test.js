describe('minReplacementsToMakeUnique', () => {
  it('should return the minimum number of removals to make all elements unique', () => {
    expect(minRemovalsToMakeUnique([3, 3, 1, 2, 2, 1])).toBe(3);
    expect(minRemovalsToMakeUnique([4, 5, 6, 7, 8, 9])).toBe(0);
    expect(minRemovalsToMakeUnique([1, 1, 1, 1, 1])).toBe(4);
    expect(minRemovalsToMakeUnique([2, 3, 4, 5, 6, 2, 3, 4])).toBe(4);
    expect(minRemovalsToMakeUnique([])).toBe(0);
  });
});