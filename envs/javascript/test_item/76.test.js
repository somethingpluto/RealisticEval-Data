/**
 * Removes the common leading indentation from each line in a given multi-line string,
 * preserving the relative indentation of the text.
 *
 * @param {string} multilineText - The input string containing multiple lines.
 * @returns {string} The sanitized string with common leading indentation removed.
 */
function removeCommonIndentation(multilineText) {
    // Split the input string into an array of lines
    const lines = multilineText.split('\n');

    // Filter out empty lines to avoid counting them in the indentation calculation
    const nonEmptyLines = lines.filter(line => line.trim().length > 0);

    // Find the minimum indentation level by counting leading spaces/tabs
    let minIndent = Infinity;
    for (const line of nonEmptyLines) {
        const leadingWhitespace = line.match(/^\s*/)[0];
        minIndent = Math.min(minIndent, leadingWhitespace.length);
    }

    // If no common indentation is found, return the original text
    if (minIndent === Infinity) {
        return multilineText;
    }

    // Remove the common leading indentation from each line
    const sanitizedLines = lines.map(line => line.slice(minIndent));

    // Join the sanitized lines back into a single string
    return sanitizedLines.join('\n');
}
describe('TestRemoveCommonIndentation', () => {
    it('should return an empty string for an empty input', () => {
        // Testing edge case with an empty string
        expect(removeCommonIndentation("")).toEqual("");
    });

    it('should return the same string as input for a single line with no indentation', () => {
        // Testing a single line with no indentation
        expect(removeCommonIndentation("No indentation here")).toEqual("No indentation here");
    });

    it('should remove common leading indentation for multiple lines with uniform indentation', () => {
        // Testing basic logic with uniform indentation across multiple lines
        const inputText = "    Line one\n    Line two\n    Line three";
        const expectedOutput = "Line one\nLine two\nLine three";
        expect(removeCommonIndentation(inputText)).toEqual(expectedOutput);
    });

    it('should remove the minimum common indentation for lines with mixed indentation', () => {
        // Testing lines with mixed indentation levels
        const inputText = "  Line one\n  Line two\n  Line three";
        const expectedOutput = "Line one\nLine two\nLine three";
        expect(removeCommonIndentation(inputText)).toEqual(expectedOutput);
    });
});

