// ... (previous code for context)

function findPowers(num: number): [number, number] | null {
  if (num <= 0) return null;

  let powerOf2 = 0;
  let powerOf3 = 0;

  while (num % 2 === 0) {
    num /= 2;
    powerOf2++;
  }

  while (num % 3 === 0) {
    num /= 3;
    powerOf3++;
  }

  if (num === 1) {
    return [powerOf2, powerOf3];
  } else {
    return null;
  }
}

// ... (rest of the code)
describe('TestFindPowers', () => {
  describe('test valid cases', () => {
    it('should handle numbers with only 2\'s and 3\'s as prime factors', () => {
      expect(findPowers(18)).toEqual([1, 2]);  // 18 = 2^1 * 3^2
      expect(findPowers(8)).toEqual([3, 0]);   // 8 = 2^3 * 3^0
      expect(findPowers(27)).toEqual([0, 3]);  // 27 = 2^0 * 3^3
      expect(findPowers(12)).toEqual([2, 1]);  // 12 = 2^2 * 3^1
      expect(findPowers(1)).toEqual([0, 0]);   // 1 = 2^0 * 3^0
    });
  });

  describe('test invalid cases', () => {
    it('should return null for numbers with prime factors other than 2 and 3', () => {
      expect(findPowers(7)).toBeNull();    // 7 is a prime factor
      expect(findPowers(14)).toBeNull();   // 14 = 2^1 * 7^1 (contains 7)
      expect(findPowers(10)).toBeNull();   // 10 = 2^1 * 5^1 (contains 5)
    });
  });

  describe('test large numbers', () => {
    it('should handle large numbers with only 2 and 3 as prime factors', () => {
      expect(findPowers(864)).toEqual([5, 3]);  // 864 = 2^5 * 3^3
      expect(findPowers(729)).toEqual([0, 6]);  // 729 = 2^0 * 3^6
    });
  });

  describe('test edge cases', () => {
    it('should handle minimal inputs', () => {
      expect(findPowers(2)).toEqual([1, 0]);   // 2 = 2^1 * 3^0
      expect(findPowers(3)).toEqual([0, 1]);   // 3 = 2^0 * 3^1
    });
  });
});
