const fs = require('fs').promises;
const readline = require('readline');
const { Readable } = require('stream');

/**
 * Reads a CSV file and parses each line into a list of strings.
 *
 * @param {string} filePath - The path to the CSV file.
 * @returns {Promise<Array<Array<string>>>} A list of string lists, where each list represents a line from the CSV.
 */
async function readCsv(filePath) {
    const fileContent = await fs.readFile(filePath, 'utf-8');
    const lines = fileContent.split('\n');

    return lines.map(line => {
        return line.split(',').map(value => value.trim());
    });
}

module.exports = readCsv;
const fs = require('fs');

describe('TestAnswer', () => {
    const testFilePath = 'test.csv';

    beforeAll(() => {
        // Create a temporary CSV file for testing
        const sampleCsvContent = "Name,Age,Location\n" +
                                  "Alice,30,New York\n" +
                                  "Bob,25,Los Angeles\n" +
                                  "Charlie,35,Chicago\n";
        fs.writeFileSync(testFilePath, sampleCsvContent);
    });

    test('read valid CSV', async () => {
        const result = await readCsv(testFilePath);
        expect(result.length).toBe(4);  // 4 lines including the header
        expect(result[0]).toEqual(["Name", "Age", "Location"]);  // Check header
        expect(result[1]).toEqual(["Alice", "30", "New York"]);
        expect(result[2]).toEqual(["Bob", "25", "Los Angeles"]);
        expect(result[3]).toEqual(["Charlie", "35", "Chicago"]);
    });

    test('read empty CSV', async () => {
        // Create an empty CSV file
        fs.writeFileSync(testFilePath, "");
        const result = await readCsv(testFilePath);
        expect(result.length).toBe(0);  // Expecting an empty list
    });

    test('read CSV with quotes', async () => {
        // Write CSV content with quoted fields
        const contentWithQuotes = '"Name","Age","Location"\n' +
                                   '"Alice","30","New York"\n' +
                                   '"Bob","25","Los Angeles"\n';
        fs.writeFileSync(testFilePath, contentWithQuotes);
        const result = await readCsv(testFilePath);
        expect(result.length).toBe(3);  // 3 lines including the header
        expect(result[0]).toEqual(['Name', 'Age', 'Location']);
    });

    test('read invalid CSV file', async () => {
        await expect(readCsv('non_existent_file.csv')).rejects.toThrow(Error);
    });

    test('read CSV with different delimiters', async () => {
        // Write CSV content with semicolons instead of commas
        const contentWithSemicolons = "Name;Age;Location\n" +
                                       "Alice;30;New York\n" +
                                       "Bob;25;Los Angeles\n";
        fs.writeFileSync(testFilePath, contentWithSemicolons);
        const result = await readCsv(testFilePath);
        expect(result.length).toBe(3);  // Expecting 3 lines
        expect(result[0]).toEqual(["Name;Age;Location"]);
    });

    afterAll(() => {
        // Clean up: remove test file after tests
        try {
            fs.unlinkSync(testFilePath);
        } catch (err) {
            // Handle error if necessary
        }
    });
});
