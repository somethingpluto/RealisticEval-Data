/**
 * Extracts the contents of the outermost brackets from the input string.
 * 
 * @param {string} s - The input string containing brackets.
 * @returns {string} - The contents within the outermost brackets, or an empty string if no brackets are found.
 */
function extractOutermostBrackets(s) {
    let startIndex = s.indexOf('[');
    let endIndex = -1;
    let bracketCount = 0;

    if (startIndex === -1) {
        return '';
    }

    for (let i = startIndex; i < s.length; i++) {
        if (s[i] === '[') {
            bracketCount++;
        } else if (s[i] === ']') {
            bracketCount--;
            if (bracketCount === 0) {
                endIndex = i;
                break;
            }
        }
    }

    if (endIndex === -1) {
        return '';
    }

    return s.substring(startIndex + 1, endIndex);
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
