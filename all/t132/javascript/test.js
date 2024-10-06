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
