/**
 * Extracts the first complete JSON object from a given string.
 *
 * The function looks for the first occurrence of an opening curly brace '{'
 * and searches for the corresponding closing curly brace '}'. It tracks
 * the balance of braces to ensure that the JSON object is complete.
 *
 * If a complete JSON object is found, it returns the substring that
 * represents that object. If no opening brace is found or if the braces
 * are unbalanced (i.e., incomplete), it returns an empty string.
 *
 * @param {string} response - The input string from which to extract the JSON object.
 * @return {string} A string containing the first complete JSON object, or an
 *         empty string if no complete object is found.
 */
function extractJson(response) {
    let openBraceIndex = response.indexOf('{');
    if (openBraceIndex === -1) {
        return '';
    }

    let closeBraceIndex = openBraceIndex + 1;
    let braceBalance = 1;

    while (braceBalance > 0 && closeBraceIndex < response.length) {
        if (response[closeBraceIndex] === '{') {
            braceBalance++;
        } else if (response[closeBraceIndex] === '}') {
            braceBalance--;
        }
        closeBraceIndex++;
    }

    if (braceBalance === 0) {
        return response.substring(openBraceIndex, closeBraceIndex);
    } else {
        return '';
    }
}
describe('extractJson', () => {
    test("returns an empty string for input without '{'", () => {
        const input = "No braces here";
        expect(extractJson(input)).toBe("");
    });

    test("extracts a single JSON object", () => {
        const input = "Here is some text before { \"key\": \"value\" } and some text after.";
        expect(extractJson(input)).toBe("{ \"key\": \"value\" }");
    });

    test("handles nested JSON objects", () => {
        const input = "Some text { \"outer\": { \"inner\": \"value\" } } more text.";
        expect(extractJson(input)).toBe("{ \"outer\": { \"inner\": \"value\" } }");
    });

    test("returns an empty string for unmatched braces", () => {
        const input = "Here is an incomplete JSON { \"key\": \"value\" ";
        expect(extractJson(input)).toBe("");
    });

    test("returns the correct JSON when multiple braces are present", () => {
        const input = "Start { { \"key\": \"value\" } and some other text { \"another\": \"object\" }} end.";
        expect(extractJson(input)).toBe("{ { \"key\": \"value\" } and some other text { \"another\": \"object\" }}");
    });

    test("extracts the first JSON object when multiple are present", () => {
        const input = "Text before { \"first\": \"value1\" } text in between { \"second\": \"value2\" }";
        expect(extractJson(input)).toBe("{ \"first\": \"value1\" }");
    });
});
