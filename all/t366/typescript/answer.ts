import * as mammoth from 'mammoth';

async function extractTextFromWord(docxFilePath: string): Promise<string> {
    /**
     * Extracts text content from a given Word file (.docx).
     *
     * @param {string} docxFilePath - The path to the Word file.
     * @returns {Promise<string>} - The extracted text content.
     */

    try {
        const result = await mammoth.convertToHtml({ path: docxFilePath });
        const html = result.value; // The generated HTML
        const text = extractTextFromHtml(html); // Convert HTML to plain text
        return text;
    } catch (error) {
        throw new Error(`Failed to extract text from ${docxFilePath}: ${error.message}`);
    }
}

function extractTextFromHtml(html: string): string {
    const tempDiv = document.createElement('div');
    tempDiv.innerHTML = html;
    return tempDiv.textContent || tempDiv.innerText || '';
}