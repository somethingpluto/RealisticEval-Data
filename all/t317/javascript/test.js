// Jest test cases for countLetters function
describe('countLetters', () => {
    test('should return the correct count for a string with only letters', () => {
        const result = countLetters('HelloWorld');
        expect(result).toBe(10); // 'HelloWorld' contains ten letters
    });

    test('should return 0 for a string with no letters', () => {
        const result = countLetters('12345!@#$%');
        expect(result).toBe(0); // '12345!@#$%' contains no letters
    });

    test('should return the correct count for a string with mixed characters', () => {
        const result = countLetters('H3ll0 W0rld!');
        expect(result).toBe(7); // 'H3ll0 W0rld!' contains seven letters
    });

    test('should return the correct count for a string with uppercase and lowercase letters', () => {
        const result = countLetters('JavaScript');
        expect(result).toBe(10); // 'JavaScript' contains ten letters
    });

    test('should return 0 for an empty string', () => {
        const result = countLetters('');
        expect(result).toBe(0); // An empty string contains no letters
    });
});