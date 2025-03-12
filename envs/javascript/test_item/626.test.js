const fs = require('fs');
const readline = require('readline');

/**
 * Reads a file from the specified path, processes each line to remove inline comments,
 * removes line breaks, and returns an array of the processed line contents.
 *
 * @param {string} path - The path to the file to be read.
 * @returns {string[]} An array of strings, each representing a processed line from the file.
 */
function readFileAndProcessLines(path) {
    return new Promise((resolve, reject) => {
        const processedLines = [];

        const readStream = fs.createReadStream(path, { encoding: 'utf8' });
        const rl = readline.createInterface({
            input: readStream,
            crlfDelay: Infinity
        });

        rl.on('line', (line) => {
            // Remove inline comments (assuming comments start with '//')
            const commentIndex = line.indexOf('//');
            if (commentIndex !== -1) {
                line = line.substring(0, commentIndex);
            }

            // Remove any trailing whitespace and line breaks
            line = line.trim();

            // Only add non-empty lines to the result
            if (line) {
                processedLines.push(line);
            }
        });

        rl.on('close', () => {
            resolve(processedLines);
        });

        readStream.on('error', (err) => {
            reject(err);
        });
    });
}
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
