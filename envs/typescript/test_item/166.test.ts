export function nextGreatestLetter(letters: string[], target: string): string {
    let left = 0;
    let right = letters.length - 1;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (letters[mid] <= target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return letters[left % letters.length];
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

