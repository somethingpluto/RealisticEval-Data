const fs = require('fs');

/**
 * Converts the data object to JSON format and saves it to the specified file path.
 * @param {Object} data - The data object to be converted to JSON.
 * @param {string} outputFilePath - The file path where the JSON will be saved.
 */
function saveAsJSON(data, outputFilePath) {
    try {
        // Convert data to JSON string with 2-space indentation
        const jsonData = JSON.stringify(data, null, 2);

        // Write the JSON string to the specified file path
        fs.writeFileSync(outputFilePath, jsonData, 'utf8');

        console.log(`Data successfully saved to ${outputFilePath}`);
    } catch (error) {
        console.error(`Error saving data to file: ${error.message}`);
    }
}