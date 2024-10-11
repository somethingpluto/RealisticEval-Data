const fs = require('fs');
const path = require('path');

function findCommonColumns(directory) {
    /**
     * Find the common columns of all CSV files in a directory and return these column names as an array.
     * @param {string} directory - Directory path
     * @returns {Array} - Array of common column names
     */

    // Read all files in the directory
    const files = fs.readdirSync(directory);

    // Filter out non-CSV files
    const csvFiles = files.filter(file => path.extname(file).toLowerCase() === '.csv');

    if (csvFiles.length === 0) {
        throw new Error('No CSV files found in the directory.');
    }

    // Function to read and parse a CSV file
    function readAndParseCsv(filePath) {
        const content = fs.readFileSync(filePath, 'utf8');
        const rows = content.split('\n').map(row => row.trim().split(','));
        return rows[0]; // Return the header row
    }

    // Get headers from the first CSV file
    let commonHeaders = readAndParseCsv(path.join(directory, csvFiles[0]));

    // Compare with other CSV files
    for (let i = 1; i < csvFiles.length; i++) {
        const currentHeaders = readAndParseCsv(path.join(directory, csvFiles[i]));
        commonHeaders = commonHeaders.filter(header => currentHeaders.includes(header));
    }

    return commonHeaders;
}