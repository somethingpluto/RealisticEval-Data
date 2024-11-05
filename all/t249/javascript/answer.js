async function extractTextFromPdf(fileUrl) {
    /**
     * Extracts text from a given PDF file.
     *
     * @param {string} fileUrl - The URL/path to the PDF file from which to extract text.
     * @returns {Promise<string>} A promise that resolves to the extracted text from the PDF.
     */
    // Initialize a text container
    let extractedText = "";

    // Load the PDF document
    const loadingTask = pdfjsLib.getDocument(fileUrl);
    const pdfDocument = await loadingTask.promise;

    // Get the number of pages in the PDF
    const numPages = pdfDocument.numPages;

    // Loop through each page in the PDF
    for (let pageNum = 1; pageNum <= numPages; pageNum++) {
        const page = await pdfDocument.getPage(pageNum);

        // Extract text from each page and add it to the text container
        const content = await page.getTextContent();
        const text = content.items.map(item => item.str).join('');
        extractedText += text + '\n';
    }

    return extractedText;
}