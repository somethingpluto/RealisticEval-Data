const fs = require('fs');
const path = require('path');

/**
 * Saves the provided content to a specified file after cleaning up
 * redundant whitespace.
 *
 * @param {string} content - The text content to be saved to the file.
 * @param {string} path - The file path where the content will be saved.
 */
function saveContentToFile(content, filePath) {
    // Clean up redundant whitespace
    const cleanedContent = content.replace(/\s+/g, ' ').trim();

    // Ensure the directory exists
    const dir = path.dirname(filePath);
    if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
    }

    // Write the cleaned content to the file
    fs.writeFileSync(filePath, cleanedContent, 'utf8');
}
describe('TestSaveContentToFile', () => {
    let testFilePath = 'test_output.txt';

    beforeAll(() => {
        // Set up a temporary file path for testing
        testFilePath = 'test_output.txt';
    });

    afterAll(() => {
        // Clean up the test file after all tests
        if (fs.existsSync(testFilePath)) {
            fs.unlinkSync(testFilePath);
        }
    });

    beforeEach(() => {
        // Ensure the test file is clean before each test
        if (fs.existsSync(testFilePath)) {
            fs.unlinkSync(testFilePath);
        }
    });

    afterEach(() => {
        // Clean up the test file after each test
        if (fs.existsSync(testFilePath)) {
            fs.unlinkSync(testFilePath);
        }
    });

    it('should save basic content correctly', () => {
        const content = "Hello,  World!  ";
        const expected = "Hello, World!";
        saveContentToFile(content, testFilePath);
        const result = fs.readFileSync(testFilePath, 'utf-8').trim();
        expect(result).toEqual(expected);
    });

    it('should handle multiple spaces and empty lines correctly', () => {
        const content = `

        This is a    test.

        Another line.      
        `;
        const expected = "This is a test. Another line.";
        saveContentToFile(content, testFilePath);
        const result = fs.readFileSync(testFilePath, 'utf-8').trim();
        expect(result).toEqual(expected);
    });

    it('should handle only whitespace correctly', () => {
        const content = "    \n  \n   ";
        const expected = "";
        saveContentToFile(content, testFilePath);
        const result = fs.readFileSync(testFilePath, 'utf-8').trim();
        expect(result).toEqual(expected);
    });

    it('should handle empty content correctly', () => {
        const content = "";
        const expected = "";
        saveContentToFile(content, testFilePath);
        const result = fs.readFileSync(testFilePath, 'utf-8').trim();
        expect(result).toEqual(expected);
    });
});
