import * as pdfjsLib from 'pdfjs-dist';

export async function extractTextFromPdf(filePath: string): Promise<string> {
    /**
     * Extracts text from a given PDF file.
     *
     * @param filePath - The path to the PDF file from which to extract text.
     * @returns A promise that resolves with the extracted text from the PDF.
     */

    const loadingTask = pdfjsLib.getDocument({ url: filePath });
    const pdfDocument = await loadingTask.promise;

    let textContent = '';

    for (let i = 1; i <= pdfDocument.numPages; i++) {
        const page = await pdfDocument.getPage(i);
        const textPage = await page.getTextContent();

        textContent += textPage.items.map(item => item.str).join(' ');
    }

    return textContent;
}