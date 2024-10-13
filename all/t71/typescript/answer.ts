import * as fs from 'fs';

/**
 * Reads numerical columns from a file starting from the line after the last line containing '/'.
 *
 * @param {string} fileName - The name of the file to read.
 * @returns {number[][]} - A 2D array containing the numerical data.
 * @throws {Error} - If the file does not contain any '/' character.
 */
function readColumns(fileName: string): number[][] {
    // Initialize a variable to track the last slash line index
    let lastSlashIndex: number | null = null;

    const lines = fs.readFileSync(fileName, 'utf8').split('\n');

    // Find the index of the last line that contains the "/" character
    for (let i = 0; i < lines.length; i++) {
        if (lines[i].includes('/')) {
            lastSlashIndex = i;
        }
    }

    // If no "/" character was found, throw an error
    if (lastSlashIndex === null) {
        throw new Error('File does not contain \'/\' character');
    }

    // Read the remaining lines in the file, starting from the line after the last "/"
    const dataLines = lines.slice(lastSlashIndex + 1);

    // Remove any empty lines or lines that start with a comment character
    const filteredDataLines = dataLines.filter(line => line.trim() && !line.trim().startsWith('!'));

    // If no valid lines remain, return an empty array
    if (filteredDataLines.length === 0) {
        return [];
    }

    // Get the row and column count by counting the number of columns in the first line
    const colCount = filteredDataLines[0].split(' ').length;

    // Create an empty array of the required size
    const arr: number[][] = [];

    // Loop through the lines in the file
    for (let i = 0; i < filteredDataLines.length; i++) {
        // Split the line into numbers and convert them to floats
        const nums = filteredDataLines[i].split(' ').map(x => parseFloat(x));

        // Store the numbers in the array
        arr.push(nums);
    }

    // Return the array
    return arr;
}