/**
 * Extracts the contents of the outermost brackets from the input string.
 * For example:
 *   input: "Text [with [nested] brackets] and more text"
 *   output: "with [nested] brackets"
 * 
 * @param {string} s - The input string containing brackets.
 * @returns {string} - The contents within the outermost brackets, or an empty string if no brackets are found.
 */
function extractOutermostBrackets(s) {
    let depth = 0;
    let start = -1;
    let end = -1;

    for (let i = 0; i < s.length; i++) {
        if (s[i] === '[') {
            if (depth === 0) {
                start = i + 1;
            }
            depth++;
        } else if (s[i] === ']') {
            depth--;
            if (depth === 0) {
                end = i;
                break;
            }
        }
    }

    if (start !== -1 && end !== -1) {
        return s.substring(start, end);
    }

    return '';
}
describe('TestExtractOutermostBrackets', () => {
    it('should extract single parentheses', () => {
        expect(extractOutermostBrackets("Text (example) more text")).toBe("example");
    });

    it('should extract nested brackets', () => {
        expect(extractOutermostBrackets("Text {with some {nested} brackets}")).toBe("with some {nested} brackets");
    });

    it('should extract square brackets', () => {
        expect(extractOutermostBrackets("Text [with [nested] brackets] and more text")).toBe("with [nested] brackets");
    });

    it('should extract mixed bracket types', () => {
        expect(extractOutermostBrackets("Mixed (types {of brackets [in use]})")).toBe("types {of brackets [in use]}");
    });

    it('should return an empty string when no brackets are present', () => {
        expect(extractOutermostBrackets("No brackets here")).toBe("");
    });
});
