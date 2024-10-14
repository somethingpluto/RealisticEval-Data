const fs = require('fs');
const path = require('path');
const Papa = require('papaparse');

/**
 * Reads a CSV file and converts it to an array of objects.
 *
 * @param {string} filePath - The path to the CSV file.
 * @returns {Promise<Array<Object>>} A promise that resolves to an array of objects containing the data from the CSV file.
 */
async function readCsvToDataArray(filePath) {
    try {
        // Check if the file exists
        const fileStats = await fs.promises.stat(filePath);
        if (!fileStats.isFile()) {
            throw new Error(`Error: The file '${filePath}' was not found.`);
        }

        // Read the CSV file content
        const fileContent = await fs.promises.readFile(filePath, 'utf8');

        // Parse the CSV content
        const results = Papa.parse(fileContent, { header: true });
        if (results.errors.length > 0) {
            throw new Error("Error: Could not parse the file.");
        }
        if (results.data.length === 0) {
            throw new Error("Error: The file is empty.");
        }

        return results.data;
    } catch (error) {
        console.error(error.message);
        throw error;
    }
}

describe('CSV Reader', () => {
    it('reads a valid CSV file', async () => {
        const validFilePath = path.join(__dirname, 'valid_data.csv');
        const dataArray = await readCsvToDataArray(validFilePath);
        expect(Array.isArray(dataArray)).toBe(true);
        expect(dataArray.length).toBe(10); // Assuming valid_data.csv has 10 rows
    });

    it('throws an error for a non-existent file', async () => {
        const invalidFilePath = path.join(__dirname, 'nonexistent_data.csv');
        await expect(readCsvToDataArray(invalidFilePath)).rejects.toThrow(/Error: The file.*was not found/);
    });

    it('throws an error for an empty CSV file', async () => {
        const emptyFilePath = path.join(__dirname, 'empty_data.csv');
        await expect(readCsvToDataArray(emptyFilePath)).rejects.toThrow(/Error: The file is empty/);
    });

    it('throws an error for a malformed CSV file', async () => {
        const malformedFilePath = path.join(__dirname, 'malformed_data.csv');
        await expect(readCsvToDataArray(malformedFilePath)).rejects.toThrow(/Error: Could not parse the file/);
    });
});