describe('prependToEachLine', () => {
    const tempFilePath = '/tmp/testfile.txt';

    beforeEach(() => {
        // Create a temporary test file with some content
        fs.writeFileSync(tempFilePath, 'line1\nline2\nline3', 'utf8');
    });

    afterEach(() => {
        // Clean up the temporary test file after each test
        fs.unlinkSync(tempFilePath);
    });

    test('should prepend a prefix to each line', () => {
        prependToEachLine(tempFilePath, 'prefix_');

        const modifiedContent = fs.readFileSync(tempFilePath, 'utf8');
        expect(modifiedContent).toBe('prefix_line1\nprefix_line2\nprefix_line3');
    });

    test('should handle empty lines correctly', () => {
        fs.writeFileSync(tempFilePath, '\nline2\n\nline4', 'utf8');
        prependToEachLine(tempFilePath, 'prefix_');

        const modifiedContent = fs.readFileSync(tempFilePath, 'utf8');
        expect(modifiedContent).toBe('\nprefix_line2\n\nprefix_line4');
    });

    test('should handle files with no newlines correctly', () => {
        fs.writeFileSync(tempFilePath, 'line1', 'utf8');
        prependToEachLine(tempFilePath, 'prefix_');

        const modifiedContent = fs.readFileSync(tempFilePath, 'utf8');
        expect(modifiedContent).toBe('prefix_line1');
    });
});