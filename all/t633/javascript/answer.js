import fs from 'fs'
/**
 * Formats a list of strings into a single-line CSV string and writes it to a specified file.
 *
 * @param {Array<string>} strings - List of strings to be formatted into CSV.
 * @param {string} filePath - The file path where the CSV string should be written.
 * @throws {Error} Throws an error if writing to the file fails.
 */
function writeCsvToFile(strings, filePath) {
    // Join the list of strings into a single line CSV formatted string
    const csvString = strings.join(',');

    // Write the CSV string to the specified file
    fs.promises.writeFile(filePath, csvString)
        .then(() => {
            console.log(`CSV written to file: ${filePath}`);
        })
        .catch(error => {
            console.error(`Error writing to file: ${error.message}`);
        });
}