const fs = require('fs');
const path = require('path');
const { copyFileWithBufferedStream } = require('./yourModule'); // Adjust the path accordingly

describe('File Copy Tests', () => {
    const sourceFile = 'testSourceFile.txt';
    const destinationFile = 'testDestinationFile.txt';

    beforeEach(() => {
        fs.writeFileSync(sourceFile, 'This is a test file content.'); // Set up test file
    });

    afterEach(() => {
        // Clean up files
        [sourceFile, destinationFile].forEach(file => {
            if (fs.existsSync(file)) {
                fs.unlinkSync(file);
            }
        });
    });

    test('copy file with content', async () => {
        const timeTaken = await copyFileWithBufferedStream(sourceFile, destinationFile);
        expect(fs.existsSync(destinationFile)).toBe(true);
        expect(fs.statSync(sourceFile).size).toBe(fs.statSync(destinationFile).size);
        expect(timeTaken).toBeGreaterThanOrEqual(0);
    });

    test('copy empty file', async () => {
        const emptyFile = 'emptyFile.txt';
        fs.writeFileSync(emptyFile, ''); // Create an empty file
        const destinationEmptyFile = 'destinationEmptyFile.txt';
        const timeTaken = await copyFileWithBufferedStream(emptyFile, destinationEmptyFile);
        expect(fs.existsSync(destinationEmptyFile)).toBe(true);
        expect(fs.statSync(destinationEmptyFile).size).toBe(0);
        expect(timeTaken).toBeGreaterThanOrEqual(0);
        fs.unlinkSync(emptyFile);
        fs.unlinkSync(destinationEmptyFile);
    });

    test('copy non-existent file', async () => {
        const nonExistentFilePath = 'nonExistentFile.txt';
        await expect(copyFileWithBufferedStream(nonExistentFilePath, destinationFile)).rejects.toThrow();
    });

    test('copy file overwrite', async () => {
        fs.writeFileSync(destinationFile, 'Old content');
        const timeTaken = await copyFileWithBufferedStream(sourceFile, destinationFile);
        expect(fs.existsSync(destinationFile)).toBe(true);
        expect(fs.statSync(sourceFile).size).toBe(fs.statSync(destinationFile).size);
        expect(timeTaken).toBeGreaterThan(0);
    });

    test('copy large file', async () => {
        const largeContent = Buffer.alloc(10 * 1024 * 1024); // 10 MB
        for (let i = 0; i < largeContent.length; i++) {
            largeContent[i] = i % 256;
        }
        fs.writeFileSync(sourceFile, largeContent);
        const timeTaken = await copyFileWithBufferedStream(sourceFile, destinationFile);
        expect(fs.existsSync(destinationFile)).toBe(true);
        expect(fs.statSync(sourceFile).size).toBe(fs.statSync(destinationFile).size);
        expect(timeTaken).toBeGreaterThan(0);
    });
});