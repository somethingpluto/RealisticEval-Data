const { lengthOfLIS } = require('./your_module'); // Adjust the path accordingly

describe('lengthOfLIS', () => {
  test('should return 4 for [10,9,2,5,3,7,101,18]', () => {
    expect(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])).toBe(4);
  });

  test('should return 1 for [0]', () => {
    expect(lengthOfLIS([0])).toBe(1);
  });

  test('should return 1 for []', () => {
    expect(lengthOfLIS([])).toBe(0);
  });

  test('should return 3 for [1,3,6,7,9,4,10,5,6]', () => {
    expect(lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6])).toBe(6);
  });
});