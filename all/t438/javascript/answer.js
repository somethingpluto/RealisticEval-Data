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

// Example usage
(async () => {
    try {
        const filePath = path.join(__dirname, 'example.csv');
        const dataArray = await readCsvToDataArray(filePath);
        console.log(dataArray);
    } catch (error) {
        console.error(error.message);
    }
})();