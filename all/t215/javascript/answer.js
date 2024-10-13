const fs = require('fs').promises; // Import the fs.promises API for asynchronous file operations

/**
 * Read a text file, replace words according to a dictionary map, and return the modified text.
 *
 * @param {string} file_path - The path to the text file.
 * @param {Object} replacement_dict - An object where the keys are words to be replaced, and the values are the replacement words.
 * @returns {Promise<string>} A promise that resolves to the text with the words replaced or an error message.
 */
async function replaceWordsInFile(file_path, replacement_dict) {
    try {
        // Read the content of the file
        const text = await fs.readFile(file_path, 'utf-8');

        // Replace words according to the replacement dictionary
        for (const [oldWord, newWord] of Object.entries(replacement_dict)) {
            text = text.replace(new RegExp(oldWord, 'g'), newWord);
        }

        return text;

    } catch (error) {
        if (error.code === 'ENOENT') {
            return "Error: The file was not found.";
        }
        return `Error: ${error.message}`;
    }
}