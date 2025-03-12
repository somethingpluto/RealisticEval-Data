const fs = require('fs');

/**
 * Formats a list of strings into a single-line CSV string and writes it to a specified file.
 *
 * @param {string[]} strings - List of strings to be formatted into CSV.
 * @param {string} filePath - The file path where the CSV string should be written.
 */
function writeCsvToFile(strings, filePath) {
    // Join the strings with a comma separator to create a CSV string
    const csvString = strings.join(',');

    // Write the CSV string to the specified file
    fs.writeFileSync(filePath, csvString);
}
const fs = require('fs');
const path = require('path');

describe('TestAnswer', () => {
    const testFilePath = path.join(__dirname, 'test_output.csv'); // Path for test output file

    afterEach(() => {
        // Delete the test file after each test
        if (fs.existsSync(testFilePath)) {
            fs.unlinkSync(testFilePath);
        }
    });

    const readFile = (filePath) => {
        /** Helper method to read file content as a string. */
        try {
            return fs.readFileSync(filePath, 'utf8');
        } catch (e) {
            throw new Error(`Failed to read file: ${e.message}`);
        }
    };

    test('writeCsvToFile with multiple strings', () => {
        const data = ["Apple", "Banana", "Cherry"];
        writeCsvToFile(data, testFilePath);
        // Assert the content of the file
        const content = readFile(testFilePath);
        expect(content).toBe("Apple,Banana,Cherry");
    });

    test('writeCsvToFile with single string', () => {
        const data = ["Apple"];
        writeCsvToFile(data, testFilePath);
        // Assert the content of the file
        const content = readFile(testFilePath);
        expect(content).toBe("Apple");
    });

    test('writeCsvToFile with empty list', () => {
        const data = [];
        writeCsvToFile(data, testFilePath);
        // Assert the content of the file is empty
        const content = readFile(testFilePath);
        expect(content).toBe("");
    });

    test('writeCsvToFile with special characters', () => {
        const data = ["Apple", "Banana, Cherry", "Date"];
        writeCsvToFile(data, testFilePath);
        // Assert the content of the file
        const content = readFile(testFilePath);
        expect(content).toBe("Apple,Banana, Cherry,Date");
    });

    test('writeCsvToFile with spaces', () => {
        const data = ["Apple ", " Banana", " Cherry "];
        writeCsvToFile(data, testFilePath);
        // Assert the content of the file with spaces
        const content = readFile(testFilePath);
        expect(content).toBe("Apple , Banana, Cherry ");
    });

    test('writeCsvToFile with file overwrite', () => {
        // First write to the file
        const firstData = ["Apple", "Banana"];
        writeCsvToFile(firstData, testFilePath);

        // Now overwrite with new data
        const secondData = ["Cherry", "Date"];
        writeCsvToFile(secondData, testFilePath);

        // Assert that the file now contains the new data
        const content = readFile(testFilePath);
        expect(content).toBe("Cherry,Date");
    });
});
