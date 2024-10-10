describe('minReovalsToMakeUnique', () => {
  it('should return the minimum number of removals to make all numbers unique', () => {
    expect(minRemovalsToMakeUnique([3, 3, 1, 2, 2, 1])).toBe(3);
    expect(minRemovalsToMakeUnique([1, 2, 3, 4, 5])).toBe(0);
    expect(minRemovalsToMakeUnique([])).toBe(0);
    expect(minRemovalsToMakeUnique([1, 1, 1, 1, 1])).toBe(4);
    expect(minRemovalsToMakeUnique([-1, -2, -3, -4, -5])).toBe(0);
  });
});