const fs = require('fs');

/**
 * Reads the content of the file specified by the file path and returns it as a byte array.
 *
 * @param {string} filePath - The path to the file that needs to be read.
 * @returns {Buffer} A byte array containing the content of the file.
 */
function readFileToByteArray(filePath) {
    try {
        const fileContent = fs.readFileSync(filePath);
        return fileContent;
    } catch (error) {
        throw new Error(`Failed to read file: ${error.message}`);
    }
}
const fs = require('fs');
const path = require('path');
describe('File Operations', () => {
    let testFile;

    beforeEach(() => {
        testFile = 'testFile.txt';
        fs.writeFileSync(testFile, Buffer.from('Test content'));
    });

    afterEach(() => {
        if (fs.existsSync(testFile)) {
            fs.unlinkSync(testFile);
        }
    });

    test('reading a file with content', () => {
        /** 
         * Test reading a file that exists and has content.
         */
        const content = readFileToByteArray(testFile);
        expect(content).toEqual(Buffer.from('Test content'));
    });

    test('reading an empty file', () => {
        /** 
         * Test reading an empty file.
         */
        const emptyFile = 'emptyFile.txt';
        fs.closeSync(fs.openSync(emptyFile, 'w')); // Create an empty file
        const content = readFileToByteArray(emptyFile);
        expect(content.length).toBe(0);
        fs.unlinkSync(emptyFile); // Cleanup
    });

    test('reading a non-existent file', () => {
        /** 
         * Test reading a file that does not exist.
         */
        const nonExistentFilePath = 'nonExistentFile.txt';
        expect(() => readFileToByteArray(nonExistentFilePath)).toThrow();
    });

    test('reading a file with special characters', () => {
        /** 
         * Test reading a file with special characters in its content.
         */
        const specialContent = 'Special content: !@#$%^&*()_+';
        fs.writeFileSync(testFile, Buffer.from(specialContent));
        const content = readFileToByteArray(testFile);
        expect(content).toEqual(Buffer.from(specialContent));
    });

    test('reading a large file', () => {
        /** 
         * Test reading a large file.
         */
        const largeContent = Buffer.from([...Array(256).keys()].flatMap(i => new Array(10 * 1024).fill(i))); // 10 MB
        fs.writeFileSync(testFile, largeContent);
        const content = readFileToByteArray(testFile);
        expect(content).toEqual(largeContent);
    });
});
