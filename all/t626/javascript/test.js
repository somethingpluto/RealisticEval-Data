const fs = require('fs');

describe('TestAnswer', () => {
    const testFilePath = 'testFile.txt';

    beforeEach(() => {
        /** 
         * Create a temporary file for testing.
         * This will create an empty file at the start of each test.
         */
        fs.writeFileSync(testFilePath, '');
    });

    function writeToFile(content) {
        /**
         * Helper method to write to the test file.
         */
        fs.writeFileSync(testFilePath, content);
    }

    test('processing of normal input', () => {
        /** 
         * Test processing of normal input.
         */
        writeToFile("Line 1\nLine 2 # Comment\nLine 3\n");
        const result = readFileAndProcessLines(testFilePath);
        expect(result).toEqual(["Line 1", "Line 2", "Line 3"]);
    });

    test('processing when only comments are present', () => {
        /** 
         * Test processing when only comments are present.
         */
        writeToFile("# This is a comment\n# Another comment\n");
        const result = readFileAndProcessLines(testFilePath);
        expect(result).toEqual([]);
    });

    test('processing with empty lines', () => {
        /** 
         * Test processing with empty lines.
         */
        writeToFile("Line 1\n\nLine 2\n\n\nLine 3 # Comment\n");
        const result = readFileAndProcessLines(testFilePath);
        expect(result).toEqual(["Line 1", "Line 2", "Line 3"]);
    });

    test('processing when there are no inline comments', () => {
        /** 
         * Test processing when there are no inline comments.
         */
        writeToFile("Line 1\nLine 2\nLine 3\n");
        const result = readFileAndProcessLines(testFilePath);
        expect(result).toEqual(["Line 1", "Line 2", "Line 3"]);
    });

    test('processing with only new lines', () => {
        /** 
         * Test processing with only new lines.
         */
        writeToFile("\n\n\n\n");
        const result = readFileAndProcessLines(testFilePath);
        expect(result).toEqual([]);
    });

    test('processing with mixed content', () => {
        /** 
         * Test processing with mixed content.
         */
        writeToFile("Valid line\n# This is a comment\nLine 2\n# Another comment\n\nLine 3 # End of line comment\n");
        const result = readFileAndProcessLines(testFilePath);
        expect(result).toEqual(["Valid line", "Line 2", "Line 3"]);
    });

    afterEach(() => {
        /** 
         * Cleanup after tests.
         * This removes the test file created during tests.
         */
        try {
            fs.unlinkSync(testFilePath);
        } catch (err) {
            // Ignore if the file doesn't exist
        }
    });
});