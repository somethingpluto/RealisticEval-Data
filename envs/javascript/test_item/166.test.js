/**
 * Finds and returns the smallest letter in a sorted array that is larger than the given target letter.
 * If the target letter is greater than or equal to all letters in the array, the function returns the first letter in the array.
 *
 * @param {string[]} letters - A sorted array of letters.
 * @param {string} target - The target letter to find the next greatest letter for.
 * @returns {string} The smallest letter in the array that is larger than the target letter.
 */
export function nextGreatestLetter(letters, target) {
    const len = letters.length;
    let low = 0, high = len - 1;
    while (low <= high) {
        const mid = Math.floor((low + high) / 2);
        if (letters[mid] > target) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return letters[low % len];
}
describe('nextGreatestLetter', () => {

    test('should return the first letter when target is greater than all letters in the array', () => {
        const letters = ['c', 'f', 'j'];
        const target = 'j';
        const result = nextGreatestLetter(letters, target);
        expect(result).toBe('c'); // Expected output: 'c'
    });

    test('should return the next greatest letter for a typical input', () => {
        const letters = ['c', 'f', 'j'];
        const target = 'a';
        const result = nextGreatestLetter(letters, target);
        expect(result).toBe('c'); // Expected output: 'c'
    });

    test('should handle the edge case where target is in between two letters', () => {
        const letters = ['c', 'f', 'j'];
        const target = 'd';
        const result = nextGreatestLetter(letters, target);
        expect(result).toBe('f'); // Expected output: 'f'
    });

    test('should return the first letter when the target is equal to the largest letter', () => {
        const letters = ['a', 'b', 'c', 'd'];
        const target = 'd';
        const result = nextGreatestLetter(letters, target);
        expect(result).toBe('a'); // Expected output: 'a'
    });

    test('should return the correct letter when the array contains only one letter', () => {
        const letters = ['a'];
        const target = 'z';
        const result = nextGreatestLetter(letters, target);
        expect(result).toBe('a'); // Expected output: 'a'
    });

});
