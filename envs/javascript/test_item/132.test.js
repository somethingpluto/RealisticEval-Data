const fs = require('fs');import { readFile as fsReadFile, writeFile as fsWriteFile } from 'fs';

/**
 * Reads the content of a file synchronously and returns it as a string.
 *
 * @param {string} filePath - The path to the file to be read.
 * @returns {string} - The content of the file as a UTF-8 encoded string.
 * @throws {Error} - Throws an error if the file cannot be read.
 */
function readFile(filePath) {
  try {
    const content = fsReadFile(filePath, 'utf8');
    return content;
  } catch (error) {
    throw new Error(`Failed to read file: ${error.message}`);
  }
}

/**
 * Writes question to a file synchronously.
 *
 * @param {string} filePath - The path to the file where question will be written.
 * @param {string} data - The question to be written to the file.
 * @throws {Error} - Throws an error if the file cannot be written.
 */
function writeFile(filePath, data) {
  try {
    fsWriteFile(filePath, data, 'utf8');
  } catch (error) {
    throw new Error(`Failed to write to file: ${error.message}`);
  }
}
// Mock fs in your Jest tests
jest.mock('fs');

describe('File Utility Functions', () => {
    afterEach(() => {
        jest.clearAllMocks();
    });

    test('readFile should return file content as a string', () => {
        const mockContent = 'Hello, world!';
        fs.readFileSync.mockReturnValue(mockContent);

        const result = readFile('/path/to/file.txt');
        expect(result).toBe(mockContent);
        expect(fs.readFileSync).toHaveBeenCalledWith('/path/to/file.txt', 'utf8');
    });

    test('readFile should return an empty string for an empty file', () => {
        const mockContent = '';
        fs.readFileSync.mockReturnValue(mockContent);

        const result = readFile('/path/to/emptyfile.txt');
        expect(result).toBe(mockContent);
        expect(fs.readFileSync).toHaveBeenCalledWith('/path/to/emptyfile.txt', 'utf8');
    });

    test('readFile should throw an error if file cannot be read', () => {
        fs.readFileSync.mockImplementation(() => {
            throw new Error('File not found');
        });

        expect(() => readFile('/invalid/path.txt')).toThrow();
    });

    test('writeFile should throw an error if file cannot be written', () => {
        fs.writeFileSync.mockImplementation(() => {
            throw new Error('Permission denied');
        });

        expect(() => writeFile('/invalid/path.txt', 'data')).toThrow();
    });
    test('readFile should handle large files correctly', () => {
        const mockContent = 'a'.repeat(10000); // 10,000 characters long string
        fs.readFileSync.mockReturnValue(mockContent);

        const result = readFile('/path/to/largefile.txt');
        expect(result).toBe(mockContent);
        expect(fs.readFileSync).toHaveBeenCalledWith('/path/to/largefile.txt', 'utf8');
    });
});

