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

    test('readFile should throw an error if file cannot be read', () => {
        fs.readFileSync.mockImplementation(() => {
            throw new Error('File not found');
        });

        expect(() => readFile('/invalid/path.txt')).toThrow('Failed to read file at /invalid/path.txt: File not found');
    });

    test('writeFile should write data to the specified file', () => {
        const dataToWrite = 'Some data to write';

        writeFile('/path/to/file.txt', dataToWrite);

        expect(fs.writeFileSync).toHaveBeenCalledWith('/path/to/file.txt', dataToWrite);
    });

    test('writeFile should throw an error if file cannot be written', () => {
        fs.writeFileSync.mockImplementation(() => {
            throw new Error('Permission denied');
        });

        expect(() => writeFile('/invalid/path.txt', 'data')).toThrow('Failed to write file at /invalid/path.txt: Permission denied');
    });

    test('writeFile should be called with correct arguments', () => {
        const dataToWrite = 'Test data';
        const filePath = '/path/to/file.txt';

        writeFile(filePath, dataToWrite);

        expect(fs.writeFileSync).toHaveBeenCalledWith(filePath, dataToWrite);
    });
});