import fs from 'fs'

/**
 * Modifies a specific line in the given file.
 *
 * @param {string} filePath - The path of the file to be modified.
 * @param {number} lineNumber - The line number to be modified (1-based index).
 * @param {string} newValue - The new value to update the line with.
 * @returns {Promise<void>} - A promise that resolves when the file is updated.
 * @throws {Error} - If an invalid line number is specified or an I/O error occurs.
 */
async function modifyLineInFile(filePath, lineNumber, newValue) {
    try {
        // Read the current lines of the file
        const data = await fs.promises.readFile(filePath, 'utf-8');
        const lines = data.split('\n');

        // Check if the line number is valid
        if (lineNumber < 1 || lineNumber > lines.length) {
            throw new Error(`Invalid line number: ${lineNumber}`);
        }

        // Update the specific line with the new value
        lines[lineNumber - 1] = newValue; // No need to add a newline character

        // Write the updated lines back to the file
        await fs.promises.writeFile(filePath, lines.join('\n'));
    } catch (error) {
        throw new Error(`An error occurred: ${error.message}`);
    }
}