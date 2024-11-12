/**
 * Transforms the input text by finding and modifying patterns that match the format '(*...*)'.
 * Specifically, it removes any asterisks inside the parentheses while preserving the outer format.
 * For example:
 *     input: *he*l*lo*
 *     output: *hello*
 *
 * @param {string} text - The input text containing patterns to be transformed.
 * @returns {string} - The transformed text with asterisks inside '(*...*)' patterns removed.
 */
function removeInnerAsterisks(text: string): string {
    // Regular expression to find patterns like (*...*)
    const pattern = /\(\*(.*?)\*\)/g;

    // Function to replace matched patterns
    const replaceAsterisks = (match: string, content: string): string => {
        const cleanedContent = content.replace(/\*/g, ''); // Remove inner asterisks
        return `(*${cleanedContent}*)`; // Return the modified format
    };

    // Substitute the pattern in text with the processed content
    return text.replace(pattern, replaceAsterisks);
}

describe('removeInnerAsterisks', () => {
    test('basic case', () => {
        const text = "Hello (*wo*rld*)!";
        const expected = "Hello (*world*)!";
        expect(removeInnerAsterisks(text)).toBe(expected);
    });

    test('multiple asterisks', () => {
        const text = "(*he*l*lo*)";
        const expected = "(*hello*)";
        expect(removeInnerAsterisks(text)).toBe(expected);
    });

    test('no asterisks inside', () => {
        const text = "(*hello*)";
        const expected = "(*hello*)";
        expect(removeInnerAsterisks(text)).toBe(expected);
    });

    test('multiple patterns', () => {
        const text = "(*hi*), (*there*), (*world*)!";
        const expected = "(*hi*), (*there*), (*world*)!";
        expect(removeInnerAsterisks(text)).toBe(expected);
    });

    test('no matching pattern', () => {
        const text = "This is a test without matching parentheses.";
        const expected = "This is a test without matching parentheses.";
        expect(removeInnerAsterisks(text)).toBe(expected);
    });
});

