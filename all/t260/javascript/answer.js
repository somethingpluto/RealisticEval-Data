const csvParser = require('csv-parser');
const createObjectCsvWriter = require('csv-writer').createObjectCsvWriter;
const fs = require('fs');
const path = require('path');

async function processCSV(filePath, outputPath) {
    /**
     * Processes a CSV file and removes rows with two or more empty columns.
     *
     * Parameters:
     * filePath (string): The path to the input CSV file.
     * outputPath (string): The path where the processed CSV file will be saved.
     *
     * Returns:
     * None
     */
    try {
        // Read the CSV file into an array of objects
        const records = [];
        await new Promise((resolve, reject) => {
            fs.createReadStream(filePath)
                .pipe(csvParser())
                .on('data', (row) => {
                    records.push(row);
                })
                .on('end', resolve)
                .on('error', reject);
        });

        // Filter the records based on the number of empty columns
        const filteredRecords = records.filter((row) => {
            const emptyCount = Object.values(row).filter(value => value === '').length;
            return emptyCount < 2;
        });

        // Define the CSV writer configuration
        const csvWriter = createObjectCsvWriter({
            path: outputPath,
            header: Object.keys(filteredRecords[0]).map(key => ({ id: key, title: key })),
        });

        // Write the filtered records to a new CSV file
        await csvWriter.writeRecords(filteredRecords);

    } catch (error) {
        if (error.code === 'ENOENT') {
            // Handle the case of an empty CSV
            fs.writeFileSync(outputPath, '');
        } else if (error.code === 'PARSE_ERR') {
            // Handle parsing errors (e.g., inconsistent columns in rows)
            console.error("Error: The input CSV has inconsistent row lengths. Please check the input data.");
        } else {
            throw error;
        }
    }
}