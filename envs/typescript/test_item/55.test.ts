function minRemovalsToMakeUnique(nums: number[]): number {
    const countMap = new Map<number, number>();
    let removals = 0;

    nums.forEach(num => {
        const count = (countMap.get(num) || 0) + 1;
        countMap.set(num, count);
    });

    const sortedCounts = Array.from(countMap.values()).sort((a, b) => b - a);

    for (let i = 1; i < sortedCounts.length; ) {
        if (sortedCounts[i] >= sortedCounts[i - 1]) {
            removals += sortedCounts[i] - 1;
            i += sortedCounts[i] - 1;
        } else {
            i++;
        }
    }

    return removals;
}
describe('minRemovalsToMakeUnique', () => {
  it('test with a basic array where multiple removals are needed', () => {
    expect(minRemovalsToMakeUnique([3, 3, 1, 2, 2, 1])).toBe(3);
  });

  it('test an array where all elements are identical', () => {
    expect(minRemovalsToMakeUnique([4, 4, 4, 4])).toBe(3);
  });

  it('test an array where all elements are already unique', () => {
    expect(minRemovalsToMakeUnique([1, 2, 3, 4])).toBe(0);
  });

  it('test an empty array', () => {
    expect(minRemovalsToMakeUnique([])).toBe(0);
  });

  it('test a more complex case with a larger array', () => {
    expect(minRemovalsToMakeUnique([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])).toBe(6);
  });
});
