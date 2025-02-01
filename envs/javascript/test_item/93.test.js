/**
 * produces a character array of length 52 containing all lowercase uppercase letters in alphabetical order
 *
 * @returns {string[]} An array of alphabet characters from 'a' to 'z' and 'A' to 'Z'.
 */
function getAllAlphabets() {
    const alphabets = [];
    for (let i = 0; i < 26; i++) {
        alphabets.push(String.fromCharCode(97 + i)); // lowercase letters
        alphabets.push(String.fromCharCode(65 + i)); // uppercase letters
    }
    return alphabets;
}
describe('getAllAlphabets', () => {
    test('should return an array of 52 characters', () => {
        const result = getAllAlphabets();
        expect(result).toHaveLength(52);
    });

    test('should start with lowercase letters from a to z', () => {
        const result = getAllAlphabets();
        const lowercaseAlphabets = result.slice(0, 26);
        expect(lowercaseAlphabets).toEqual([
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]);
    });

    test('should end with uppercase letters from A to Z', () => {
        const result = getAllAlphabets();
        const uppercaseAlphabets = result.slice(26);
        expect(uppercaseAlphabets).toEqual([
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]);
    });

    test('should return "a" as the first element', () => {
        const result = getAllAlphabets();
        expect(result[0]).toBe('a');
    });

    test('should return "Z" as the last element', () => {
        const result = getAllAlphabets();
        expect(result[result.length - 1]).toBe('Z');
    });
});
