/**
 * Formats a string into a commented block with a specified maximum line length.
 *
 * @param {string} string - The input string to format.
 * @param {number} [max_length=60] - Maximum length of each line in the output.
 * @returns {string} A formatted string with each line prefixed by '# ' and not exceeding the specified max_length.
 */
function formatComment(string, max_length = 60) {
    // Split the input string into words
    const words = string.split(' ');
    let result = [];
    let currentLine = '# ';

    // Iterate through each word
    for (const word of words) {
        // Check if adding the word to the current line would exceed the max_length
        if (currentLine.length + word.length + 1 > max_length) {
            // If it does, push the current line to the result and start a new line
            result.push(currentLine.trim());
            currentLine = '# ' + word + ' ';
        } else {
            // Otherwise, add the word to the current line
            currentLine += word + ' ';
        }
    }

    // Push the last line to the result
    result.push(currentLine.trim());

    // Join the result array into a single string with newline characters
    return result.join('\n');
}
describe('TestFormatComment', () => {
    it('test with a short string that fits within max_length', () => {
        const inputString = "This is a test.";
        const expectedOutput = "# This is a test.";
        expect(formatComment(inputString)).toBe(expectedOutput);
    });

    it('test with a longer string that exceeds max_length', () => {
        const inputString = "This is a test of the format_comment function which should wrap long lines correctly.";
        const expectedOutput = 
            "# This is a test of the format_comment function which should\n" +
            "# wrap long lines correctly.";
        expect(formatComment(inputString, 60)).toBe(expectedOutput);
    });

    it('test with multiple lines of input', () => {
        const inputString = "First line.\nSecond line that is quite long and needs to be wrapped.";
        const expectedOutput = 
            "# First line.\n" +
            "# Second line that is quite long and needs to be wrapped.";
        expect(formatComment(inputString, 60)).toBe(expectedOutput);
    });

    it('test with a line that is exactly max_length characters long', () => {
        const inputString = "A".repeat(60); // 60 characters long
        const expectedOutput = "# " + "A".repeat(60);
        expect(formatComment(inputString, 60)).toBe(expectedOutput);
    });

    it('test with an empty string', () => {
        const inputString = "";
        const expectedOutput = "# ";
        expect(formatComment(inputString)).toBe(expectedOutput);
    });
});
