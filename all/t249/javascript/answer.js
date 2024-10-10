const fs = require('fs');
const pdf = require('pdf-parse');

async function extractTextFromPDF(filePath) {
    /**
     * Extracts text from a given PDF file.
     *
     * @param {string} filePath - The path to the PDF file from which to extract text.
     * @returns {Promise<string>} - The extracted text from the PDF.
     */

    const dataBuffer = fs.readFileSync(filePath);

    try {
        const data = await pdf(dataBuffer);
        return data.text;
    } catch (error) {
        throw new Error(`Failed to extract text from PDF: ${error.message}`);
    }
}