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