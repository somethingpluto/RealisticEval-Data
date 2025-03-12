import { isPalindrome } from './utils';

/**
 * Filters out the number of palindromes within any number `n`.
 * Palindrome numbers are numbers that read the same forwards and backwards, such as 121, 1331.
 *
 * @param n - The range number
 * @returns An array of palindrome numbers
 */
function getPalindromeList(n: number): number[] {
  const palindromes: number[] = [];
  for (let i = 1; i <= n; i++) {
    if (isPalindrome(i)) {
      palindromes.push(i);
    }
  }
  return palindromes;
}
describe('getPalindromeList', () => {
    /**
     * Test case for the first palindrome
     */
    it('should return [0] for n = 1', () => {
        expect(getPalindromeList(1)).toEqual([0], 'The first palindrome should be 0');
    });

    /**
     * Test case for the tenth palindrome, transitioning to double digits
     */
    it('should return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] for n = 10', () => {
        expect(getPalindromeList(10)).toEqual(
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            'The tenth palindrome should be [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]'
        );
    });

    /**
     * Test case for the 100th palindrome, transitioning to triple digits
     */
    it('should return the correct palindromes for n = 100', () => {
        expect(getPalindromeList(100)).toEqual(
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99],
            'The 100th palindrome should be [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99]'
        );
    });

    /**
     * Test case for a larger number, e.g., the 1000th palindrome
     */
    it('should return the correct palindromes for n = 1000', () => {
        expect(getPalindromeList(1000)).toEqual(
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 303, 313, 323, 333, 343, 353, 363, 373, 383, 393, 404, 414, 424, 434, 444, 454, 464, 474, 484, 494, 505, 515, 525, 535, 545, 555, 565, 575, 585, 595, 606, 616, 626, 636, 646, 656, 666, 676, 686, 696, 707, 717, 727, 737, 747, 757, 767, 777, 787, 797, 808, 818, 828, 838, 848, 858, 868, 878, 888, 898, 909, 919, 929, 939, 949, 959, 969, 979, 989, 999],
            'The 1000th palindrome should be [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 303, 313, 323, 333, 343, 353, 363, 373, 383, 393, 404, 414, 424, 434, 444, 454, 464, 474, 484, 494, 505, 515, 525, 535, 545, 555, 565, 575, 585, 595, 606, 616, 626, 636, 646, 656, 666, 676, 686, 696, 707, 717, 727, 737, 747, 757, 767, 777, 787, 797, 808, 818, 828, 838, 848, 858, 868, 878, 888, 898, 909, 919, 929, 939, 949, 959, 969, 979, 989, 999]'
        );
    });
});
