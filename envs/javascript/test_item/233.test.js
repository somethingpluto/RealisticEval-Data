/**
 * Removes comments from the provided string. Comments start with a '#' and end at the newline.
 * 
 * Example:
 *   Input: "Hello, world! # This is a comment"
 *   Output: "Hello, world!"
 * 
 * @param {string} string - The input string containing potential comments.
 * @returns {string} The string with all comments removed.
 */
function removeComments(string) {
    return string.split('\n').map(line => line.split('#')[0].trim()).join(' ').trim();
}
describe('TestRemoveComments', () => {
    describe('test_single_line_comment', () => {
        it('should handle a single line comment correctly', () => {
            const inputString = "Hello, world!# This is a comment";
            const expectedOutput = "Hello, world!";
            expect(removeComments(inputString)).toEqual(expectedOutput);
        });
    });

    describe('test_no_comments', () => {
        it('should handle a string with no comments correctly', () => {
            const inputString = "Hello, world!\nPython is fun!";
            const expectedOutput = "Hello, world!\nPython is fun!";
            expect(removeComments(inputString)).toEqual(expectedOutput);
        });
    });

    describe('test_empty_string', () => {
        it('should handle an empty string correctly', () => {
            const inputString = "";
            const expectedOutput = "";
            expect(removeComments(inputString)).toEqual(expectedOutput);
        });
    });

    describe('test_comments_only', () => {
        it('should handle a string where all lines are comments correctly', () => {
            const inputString = "# comment only line\n#another comment line";
            const expectedOutput = "\n";
            expect(removeComments(inputString)).toEqual(expectedOutput);
        });
    });
});
