import * as fs from 'fs';
import * as path from 'path';
import * as os from 'os';
import { findJsonFilesWithKeyword } from './your_module'; // Adjust the import as needed
import { jest } from '@jest/globals';

// Define a helper function for setting up temporary directories
const mkdtempSync = (): string => {
    const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'test-'));
    return tempDir;
};

describe('findJsonFilesWithKeyword', () => {
    let testDir: string;
    let testFilePath: string;

    beforeAll(() => {
        // Set up a temporary directory and file
        testDir = mkdtempSync();
        testFilePath = path.join(testDir, 'test.js.json');
        fs.writeFileSync(testFilePath, '{"key": "value with keyword"}');
    });

    afterAll(() => {
        // Remove the temporary directory and file after tests
        fs.rmSync(testDir, { recursive: true, force: true });
    });

    it('should find the keyword in a single file', () => {
        // Mock fs.readdirSync, fs.readFileSync, and JSON.parse
        jest.spyOn(fs, 'readdirSync').mockReturnValue(['test.js.json']);
        jest.spyOn(fs, 'readFileSync').mockReturnValue('{"key": "value with keyword"}');
        jest.spyOn(JSON, 'parse').mockReturnValue({ key: 'value with keyword' });

        const result = findJsonFilesWithKeyword(testDir, 'keyword');
        const expected = ['test.js.json'];

        expect(result).toEqual(expected);

        // Restore the mocked methods
        jest.restoreAllMocks();
    });

    it('should not find the keyword in the file', () => {
        // Mock fs.readdirSync, fs.readFileSync, and JSON.parse
        jest.spyOn(fs, 'readdirSync').mockReturnValue(['test.js.json']);
        jest.spyOn(fs, 'readFileSync').mockReturnValue('{"key": "no keyword here"}');
        jest.spyOn(JSON, 'parse').mockReturnValue({ key: 'no keyword here' });

        const result = findJsonFilesWithKeyword(testDir, 'wc');
        const expected: string[] = [];

        expect(result).toEqual(expected);

        // Restore the mocked methods
        jest.restoreAllMocks();
    });

    it('should handle directories with no JSON files', () => {
        // Mock fs.readdirSync to return an empty directory
        jest.spyOn(fs, 'readdirSync').mockReturnValue([]);

        const result = findJsonFilesWithKeyword(testDir, 'keyword');
        const expected: string[] = [];

        expect(result).toEqual(expected);

        // Restore the mocked methods
        jest.restoreAllMocks();
    });

    it('should find the keyword in multiple JSON files', () => {
        // Create multiple files in the temporary directory
        const file1Path = path.join(testDir, 'file1.json');
        const file2Path = path.join(testDir, 'file2.json');
        fs.writeFileSync(file1Path, '{"key": "keyword present here"}');
        fs.writeFileSync(file2Path, '{"key": "keyword present here"}');

        // Mock fs.readdirSync, fs.readFileSync, and JSON.parse
        jest.spyOn(fs, 'readdirSync').mockReturnValue(['file1.json', 'file2.json']);
        jest.spyOn(fs, 'readFileSync').mockReturnValue(
            '{"key": "keyword present here"}'
        );
        jest.spyOn(JSON, 'parse').mockReturnValue({ key: 'keyword present here' });

        const result = findJsonFilesWithKeyword(testDir, 'keyword');
        const expected = ['file1.json', 'file2.json'];

        expect(result).toEqual(expected);

        // Restore the mocked methods
        jest.restoreAllMocks();
    });
});