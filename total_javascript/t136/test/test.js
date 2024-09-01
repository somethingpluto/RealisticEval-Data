const fs = require('fs');
const path = require('path');
// Mock the file system module
jest.mock('fs');

describe('loadCachedData', () => {
    const cacheFilePath = path.join(__dirname, 'cache.json');

    afterEach(() => {
        jest.clearAllMocks(); // Clear any mocks after each test
    });

    test('should return parsed JSON data when the file exists and contains valid JSON', () => {
        const mockData = { key: 'value' };
        fs.existsSync.mockReturnValue(true);
        fs.readFileSync.mockReturnValue(JSON.stringify(mockData));

        const result = loadCachedData();
        expect(result).toEqual(mockData);
    });

    test('should return null when the file does not exist', () => {
        fs.existsSync.mockReturnValue(false);

        const result = loadCachedData();
        expect(result).toBeNull();
    });

    test('should return null and log error when the file contains invalid JSON', () => {
        fs.existsSync.mockReturnValue(true);
        fs.readFileSync.mockReturnValue('invalid JSON');

        console.error = jest.fn(); // Mock console.error
        const result = loadCachedData();

        expect(result).toBeNull();
        expect(console.error).toHaveBeenCalledWith(
            'Error reading or parsing cache.json:',
            expect.any(SyntaxError)
        );
    });

    test('should return null and log error when there is an error reading the file', () => {
        fs.existsSync.mockReturnValue(true);
        fs.readFileSync.mockImplementation(() => {
            throw new Error('Read error');
        });

        console.error = jest.fn(); // Mock console.error
        const result = loadCachedData();

        expect(result).toBeNull();
        expect(console.error).toHaveBeenCalledWith(
            'Error reading or parsing cache.json:',
            expect.any(Error)
        );
    });

    test('should return null when the file is empty', () => {
        fs.existsSync.mockReturnValue(true);
        fs.readFileSync.mockReturnValue('');

        const result = loadCachedData();
        expect(result).toBeNull();
    });
});