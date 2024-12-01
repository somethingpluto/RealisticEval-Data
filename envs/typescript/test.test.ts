function removeCommonIndentation(multilineText: string): string {
    const lines = multilineText.split('\n');
    const nonEmptyLines = lines.filter(line => line.trim().length > 0);
    let minIndent = Infinity;
    for (const line of nonEmptyLines) {
        const strippedLine = line.replace(/^\s+/, '');
        const indent = line.length - strippedLine.length;
        minIndent = Math.min(minIndent, indent);
    }
    if (minIndent === Infinity) {
        return multilineText;
    }
    const sanitizedLines = lines.map(line => line.slice(minIndent));
    return sanitizedLines.join('\n');
}

describe('TestRemoveCommonIndentation', () => {
    it('should return an empty string for an empty input', () => {
        // Testing edge case with an empty string
        expect(removeCommonIndentation("")).toBe("");
    });

    it('should return the same string for a single line with no indentation', () => {
        // Testing a single line with no indentation
        const inputText = "No indentation here";
        const expectedOutput = "No indentation here";
        expect(removeCommonIndentation(inputText)).toBe(expectedOutput);
    });

    it('should remove common leading indentation for multiple lines with uniform indentation', () => {
        // Testing basic logic with uniform indentation across multiple lines
        const inputText = "    Line one\n    Line two\n    Line three";
        const expectedOutput = "Line one\nLine two\nLine three";
        expect(removeCommonIndentation(inputText)).toBe(expectedOutput);
    });

    it('should remove the minimum common indentation for lines with mixed indentation', () => {
        // Testing lines with mixed indentation levels
        const inputText = "  Line one\n  Line two\n  Line three";
        const expectedOutput = "Line one\nLine two\nLine three";
        expect(removeCommonIndentation(inputText)).toBe(expectedOutput);
    });
});

