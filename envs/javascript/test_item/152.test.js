/**
 * Converts a given string into its corresponding mathematical sans-serif italic characters.
 *
 * @param input The input string to be converted.
 * @returns The converted string with each character replaced by its mathematical sans-serif italic equivalent.
 */
function convertToMathematicalSansSerifItalic(input) {
    const charMap = {
        'A': '𝘈', 'B': '𝘉', 'C': '𝘊', 'D': '𝘋', 'E': '𝘌', 'F': '𝘍', 'G': '𝘎',
        'H': '𝘏', 'I': '𝘐', 'J': '𝘑', 'K': '𝘒', 'L': '𝘓', 'M': '𝘔', 'N': '𝘕',
        'O': '𝘖', 'P': '𝘗', 'Q': '𝘘', 'R': '𝘙', 'S': '𝘚', 'T': '𝘛', 'U': '𝘜',
        'V': '𝘝', 'W': '𝘞', 'X': '𝘟', 'Y': '𝘠', 'Z': '𝘡',
        'a': '𝘢', 'b': '𝘣', 'c': '𝘤', 'd': '𝘥', 'e': '𝘦', 'f': '𝘧', 'g': '𝘨',
        'h': '𝘩', 'i': '𝘪', 'j': '𝘫', 'k': '𝘬', 'l': '𝘭', 'm': '𝘮', 'n': '𝘯',
        'o': '𝘰', 'p': '𝘱', 'q': '𝘲', 'r': '𝘳', 's': '𝘴', 't': '𝘵', 'u': '𝘶',
        'v': '𝘷', 'w': '𝘸', 'x': '𝘹', 'y': '𝘺', 'z': '𝘻'
    };

    return input.split('').map(char => charMap[char] || char).join('');
}
describe('convertToMathematicalSansSerifItalic', () => {
    test('should return an empty string when input is an empty string', () => {
        const input = '';
        const result = convertToMathematicalSansSerifItalic(input);
        expect(result).toBe(''); // Edge case: empty string
    });

    test('should correctly convert all uppercase and lowercase letters to mathematical sans-serif italic', () => {
        const input = 'HelloWorld';
        const result = convertToMathematicalSansSerifItalic(input);
        expect(result).toBe('𝑯𝒆𝒍𝒍𝒐𝑾𝒐𝒓𝒍𝒅'); // Basic logic: mixed case
    });

    test('should leave characters unchanged if they have no corresponding mathematical sans-serif italic equivalent', () => {
        const input = '12345!@#';
        const result = convertToMathematicalSansSerifItalic(input);
        expect(result).toBe('𝟣𝟤𝟥𝟦𝟧!@#'); // Basic logic: numbers with special characters
    });

    test('should handle input with a mix of convertible and non-convertible characters', () => {
        const input = 'Math123!';
        const result = convertToMathematicalSansSerifItalic(input);
        expect(result).toBe('𝑴𝒂𝒕𝒉𝟣𝟤𝟥!'); // Basic logic: mix of letters, numbers, and special characters
    });

    test('should handle edge case where input is at the boundary of supported characters', () => {
        const input = 'A0z9';
        const result = convertToMathematicalSansSerifItalic(input);
        expect(result).toBe('𝑨𝟢𝒛𝟫'); // Boundary values: 'A', '0', 'z', '9'
    });
});
