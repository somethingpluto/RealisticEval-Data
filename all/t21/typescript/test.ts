import * as fs from 'fs';
import * as path from 'path';
import { compareFiles } from './compareFiles'; // Ensure this path matches where you have the compareFiles function

// Create temporary file paths for testing
const file1Path = path.resolve('file1.txt');
const file2Path = path.resolve('file2.txt');

describe('TestCompareFiles', () => {

    afterEach(() => {
        // Clean up created files
        if (fs.existsSync(file1Path)) {
            fs.unlinkSync(file1Path);
        }
        if (fs.existsSync(file2Path)) {
            fs.unlinkSync(file2Path);
        }
    });

    test('test_identical_files', () => {
        // Content for two identical files
        const file1Content = "Line1\nLine2\nLine3\n";
        const file2Content = "Line1\nLine2\nLine3\n";

        fs.writeFileSync(file1Path, file1Content, 'utf-8');
        fs.writeFileSync(file2Path, file2Content, 'utf-8');

        const result = compareFiles(file1Path, file2Path);
        expect(result.length).toBe(0); // There should be no differences detected
    });

    test('test_files_with_differences', () => {
        // Content for two different files
        const file1Content = "Line1\nLine2\nLine3\n";
        const file2Content = "Line1\nLineChanged\nLine3\n";

        fs.writeFileSync(file1Path, file1Content, 'utf-8');
        fs.writeFileSync(file2Path, file2Content, 'utf-8');

        const result = compareFiles(file1Path, file2Path);
        expect(result.length).not.toBe(0); // There should be differences detected
    });

    test('test_nonexistent_file', () => {
        // Mock FileNotFoundError for nonexistent file
        jest.spyOn(fs, 'readFileSync').mockImplementation((fileName: string) => {
            if (fileName === 'nonexistent.txt') {
                throw new Error('File not found');
            }
            return '';
        });

        expect(() => {
            compareFiles('nonexistent.txt', file2Path);
        }).toThrow('Error reading files: File not found');

        jest.restoreAllMocks();
    });

    test('test_file_reading_error', () => {
        // Mock IOError when reading files
        jest.spyOn(fs, 'readFileSync').mockImplementation(() => {
            throw new Error('Error reading file');
        });

        expect(() => {
            compareFiles(file1Path, file2Path);
        }).toThrow('Error reading files: Error reading file');

        jest.restoreAllMocks();
    });
});