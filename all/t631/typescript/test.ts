import * as fs from 'fs';

describe('writeCsvToFile', () => {
    const testFilePath = 'test_output.csv'; // Path for test output file

    afterEach(() => {
        // Delete the test file after each test
        if (fs.existsSync(testFilePath)) {
            fs.unlinkSync(testFilePath);
        }
    });

    const readFile = (filePath: string): string => {
        /** Helper method to read file content as a string. */
        return fs.readFileSync(filePath, 'utf-8');
    };

    test('should write CSV to file with multiple strings', () => {
        const data = ['Apple', 'Banana', 'Cherry'];
        writeCsvToFile(data, testFilePath);
        // Assert the content of the file
        const content = readFile(testFilePath);
        expect(content).toBe('Apple,Banana,Cherry');
    });

    test('should write CSV to file with a single string', () => {
        const data = ['Apple'];
        writeCsvToFile(data, testFilePath);
        // Assert the content of the file
        const content = readFile(testFilePath);
        expect(content).toBe('Apple');
    });

    test('should write CSV to file with an empty list', () => {
        const data: string[] = [];
        writeCsvToFile(data, testFilePath);
        // Assert the content of the file is empty
        const content = readFile(testFilePath);
        expect(content).toBe('');
    });

    test('should write CSV to file with special characters', () => {
        const data = ['Apple', 'Banana, Cherry', 'Date'];
        writeCsvToFile(data, testFilePath);
        // Assert the content of the file
        const content = readFile(testFilePath);
        expect(content).toBe('Apple,Banana, Cherry,Date');
    });

    test('should write CSV to file with spaces', () => {
        const data = ['Apple ', ' Banana', ' Cherry '];
        writeCsvToFile(data, testFilePath);
        // Assert the content of the file with spaces
        const content = readFile(testFilePath);
        expect(content).toBe('Apple , Banana, Cherry ');
    });

    test('should overwrite the file with new data', () => {
        // First write to the file
        const firstData = ['Apple', 'Banana'];
        writeCsvToFile(firstData, testFilePath);

        // Now overwrite with new data
        const secondData = ['Cherry', 'Date'];
        writeCsvToFile(secondData, testFilePath);

        // Assert that the file now contains the new data
        const content = readFile(testFilePath);
        expect(content).toBe('Cherry,Date');
    });
});