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