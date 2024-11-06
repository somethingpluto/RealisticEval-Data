const fs = require('fs');
const path = require('path');
const util = require('util');

// Promisify the fs methods for better async handling
const readFileAsync = util.promisify(fs.readFile);
const writeFileAsync = util.promisify(fs.writeFile);

/**
 * This function converts the encoding of a file from one encoding to another
 *
 * @param {string} inputFilePath - The path to the input file.
 * @param {string} outputFilePath - The path to the output file where the converted content is saved.
 * @param {string} [originalEncoding='cp932'] - The original encoding of the file (default is 'cp932').
 * @param {string} [targetEncoding='utf16le'] - The target encoding to convert to (default is 'utf16le').
 * @returns {Promise<boolean>} A promise that resolves to true if the conversion was successful, or if no conversion was needed; false otherwise.
 */
async function convertEncoding(inputFilePath, outputFilePath, originalEncoding = 'cp932', targetEncoding = 'utf16le') {
    try {
        // Read the file with the original encoding
        const content = await readFileAsync(inputFilePath, { encoding: originalEncoding });

        // Write the content in the new encoding
        await writeFileAsync(outputFilePath, content, { encoding: targetEncoding });

        return true;
    } catch (error) {
        if (error.code === 'UNICODE_ERROR') {
            // Handle encoding errors if the file was already in the target encoding
            try {
                // Try reading to check if it's already in target encoding
                await readFileAsync(inputFilePath, { encoding: targetEncoding });

                // Copy if no error occurs
                fs.copyFileSync(inputFilePath, outputFilePath);
                console.log(`File already in target encoding: ${inputFilePath}`);
                return true;
            } catch (innerError) {
                console.error(`Conversion failed due to encoding error: ${error.message}`);
                return false;
            }
        } else {
            console.error(`An unexpected error occurred: ${error.message}`);
            return false;
        }
    }
}