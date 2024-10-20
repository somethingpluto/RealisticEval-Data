import * as fs from 'fs';

describe('File Operations', () => {
    const testFile = 'testFile.txt';

    beforeEach(() => {
        fs.writeFileSync(testFile, Buffer.from('Test content'));
    });

    afterEach(() => {
        if (fs.existsSync(testFile)) {
            fs.unlinkSync(testFile);
        }
    });

    test('read file with content', () => {
        const content = readFileToByteArray(testFile);
        expect(content).toEqual(Buffer.from('Test content'));
    });

    test('read empty file', () => {
        const emptyFile = 'emptyFile.txt';
        fs.writeFileSync(emptyFile, '');
        const content = readFileToByteArray(emptyFile);
        expect(content.length).toBe(0);
        fs.unlinkSync(emptyFile);
    });

    test('read non-existent file', () => {
        const nonExistentFilePath = 'nonExistentFile.txt';
        expect(() => readFileToByteArray(nonExistentFilePath)).toThrow();
    });

    test('read file with special characters', () => {
        const specialContent = 'Special content: !@#$%^&*()_+';
        fs.writeFileSync(testFile, Buffer.from(specialContent));
        const content = readFileToByteArray(testFile);
        expect(content).toEqual(Buffer.from(specialContent));
    });

    test('read large file', () => {
        const largeContent = Buffer.from(Array.from({ length: 256 }, (_, i) => i).flatMap(i => Array(10).fill(i)));
        fs.writeFileSync(testFile, largeContent);
        const content = readFileToByteArray(testFile);
        expect(content).toEqual(largeContent);
    });
});