/**
 * Extracts the string contained in the first pair of braces `{}` from the input string.
 *
 * @param {string} input - The input string from which the braces content will be extracted.
 * @return {string} A substring enclosed within the first pair of braces, or an error message if braces are missing.
 */
function extractStringFromBraces(input) {
    const openingBraceIndex = input.indexOf('{');
    const closingBraceIndex = input.indexOf('}');

    if (openingBraceIndex === -1 || closingBraceIndex === -1) {
        return 'Error: Missing braces';
    }

    if (openingBraceIndex > closingBraceIndex) {
        return 'Error: Braces are not properly balanced';
    }

    return input.substring(openingBraceIndex + 1, closingBraceIndex);
}
describe("Test cases for extractStringFromBraces function", () => {

    test("Basic extraction", () => {
        const input = "This is a sample text with some data {data: \"value\"} and more text.";
        const result = extractStringFromBraces(input);
        expect(result).toBe("{data: \"value\"}");
    });

    test("No braces", () => {
        const input = "This string has no braces.";
        const result = extractStringFromBraces(input);
        expect(result).toBe("No opening brace found.");
    });

    test("Only opening brace", () => {
        const input = "This string has an opening brace { but no closing brace.";
        const result = extractStringFromBraces(input);
        expect(result).toBe("No closing brace found.");
    });

    test("Only closing brace", () => {
        const input = "This string has a closing brace } but no opening brace.";
        const result = extractStringFromBraces(input);
        expect(result).toBe("No opening brace found.");
    });

    test("Multiple braces", () => {
        const input = "First {first} and second {second} braces.";
        const result = extractStringFromBraces(input);
        expect(result).toBe("{first}");
    });

    test("Empty braces", () => {
        const input = "This string has empty braces {} and some text.";
        const result = extractStringFromBraces(input);
        expect(result).toBe("{}");
    });
});
