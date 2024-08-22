const fs = require('fs');

/**
 * Use ESM syntax to import the file system module and define the file read and write operation functions
 */

/**
 * Reads the content of a file synchronously and returns it as a string.
 *
 * @param {string} filePath - The path to the file to be read.
 * @returns {string} - The content of the file as a UTF-8 encoded string.
 * @throws {Error} - Throws an error if the file cannot be read.
 */
function readFile(filePath) {
    try {
        return fs.readFileSync(filePath, 'utf8');
    } catch (error) {
        throw new Error(`Failed to read file at ${filePath}: ${error.message}`);
    }
}

/**
 * Writes data to a file synchronously.
 *
 * @param {string} filePath - The path to the file where data will be written.
 * @param {string} data - The data to be written to the file.
 * @throws {Error} - Throws an error if the file cannot be written.
 */
function writeFile(filePath, data) {
    try {
        fs.writeFileSync(filePath, data);
    } catch (error) {
        throw new Error(`Failed to write file at ${filePath}: ${error.message}`);
    }
}