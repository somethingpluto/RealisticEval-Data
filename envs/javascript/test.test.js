function saveContentToFile(content, path) {
    const lines = content.split('\n').filter(line => line.trim().length > 0).map(line => line.trim());
    content = lines.join('\n');

    // Replace multiple spaces with a single space.
    content = content.replace(/\s+/g, ' ');

    // Write the cleaned content to the specified file.
    const fs = require('fs');
    fs.writeFileSync(path, content, { encoding: 'utf-8' });
}

import * as fs from 'fs';

describe('TestSaveContentToFile', () => {
    let testFilePath: string;

    beforeEach(() => {
        // Set up a temporary file path for testing
        testFilePath = 'test_output.txt';
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
