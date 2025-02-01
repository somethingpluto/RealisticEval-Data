/**
 * Formats a string by prepending '> ' to each line and ensuring proper
 * formatting of code blocks.
 *
 * @param {string} x - The input string to be formatted. If the input is not a
 *                     string, it will be converted to one.
 * @returns {string} - The formatted string with each line prefixed by '> ' and
 *                     with balanced code block delimiters.
 */
function formatStr(x) {
    if (typeof x !== 'string') {
        x = String(x);
    }

    const lines = x.split('\n');
    const formattedLines = [];

    let codeBlockDepth = 0;
    for (const line of lines) {
        if (line.startsWith('
describe('TestFormatStr', () => {
    it('test_simple_string', () => {
        // Test a simple string input.
        const inputStr = "Hello, World!";
        const expectedOutput = "> Hello, World!";
        expect(formatStr(inputStr)).toBe(expectedOutput);
    });

    it('test_multiline_string', () => {
        // Test a multiline string input.
        const inputStr = "Line 1\nLine 2\nLine 3";
        const expectedOutput = "> Line 1\n> Line 2\n> Line 3";
        expect(formatStr(inputStr)).toBe(expectedOutput);
    });

    it('test_code_block_delimiters_even', () => {
        // Test a string with an even number of code block delimiters.
        const inputStr = "Some code:\n```\nprint('Hello')\n```";
        const expectedOutput = "> Some code:\n> ```\n> print('Hello')\n> ```";
        expect(formatStr(inputStr)).toBe(expectedOutput);
    });

    it('test_code_block_delimiters_odd', () => {
        // Test a string with an odd number of code block delimiters.
        const inputStr = "Some code:\n```\nprint('Hello')";
        const expectedOutput = "> Some code:\n> ```\n> print('Hello')\n> ```";
        expect(formatStr(inputStr)).toBe(expectedOutput);
    });

    it('test_non_string_input', () => {
        // Test non-string input (e.g., integer) to ensure it's converted.
        const inputValue = 123;
        const expectedOutput = "> 123";
        expect(formatStr(inputValue)).toBe(expectedOutput);
    });
});
