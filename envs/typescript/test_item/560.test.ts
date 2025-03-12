// ... (previous code for context)
function getLineNumber(content: string, index: number): number {
    let line = 1;
    let charIndex = 0;
    for (const lineContent of content.split('\n')) {
        charIndex += lineContent.length + 1; // +1 for the newline character
        if (index < charIndex) {
            return line;
        }
        line++;
    }
    return line;
}
// ... (continuation of the code)
describe('getLineNumber', () => {
    test('returns 1 for the first character', () => {
        expect(getLineNumber("Line 1\nLine 2\nLine 3", 0)).toBe(1);
    });

    test('returns 1 for the last character of the first line', () => {
        expect(getLineNumber("Line 1\nLine 2\nLine 3", 5)).toBe(1);
    });

    test('returns 3 for the last character of the third line', () => {
        expect(getLineNumber("Line 1\nLine 2\nLine 3", 18)).toBe(3);
    });

    test('returns 1 for a single line string', () => {
        expect(getLineNumber("Single line string", 0)).toBe(1);
    });

    test('returns 3 for an index within a multiline string with trailing newlines', () => {
        expect(getLineNumber("Line 1\nLine 2\nLine 3\n\n", 15)).toBe(3);
    });
});
