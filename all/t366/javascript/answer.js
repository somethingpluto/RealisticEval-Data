const mammoth = require("mammoth");

async function extractTextFromWord(docxFilePath) {
    /**
     * Extracts text content from a given Word file (.docx).
     *
     * @param {string} docxFilePath - The path to the Word file.
     * @returns {Promise<string>} The extracted text content.
     */

    try {
        const result = await mammoth.convertToHtml({ path: docxFilePath });
        return result.value; // The generated HTML
    } catch (error) {
        console.error("Error extracting text from .docx file:", error);
        throw error;
    }
}
