function extractParagraphsAndLines(text: string): { paragraphs: string[], lines: string[] } {
    /**
     * Extracts paragraphs and lines from the given text.
     *
     * @param text - The input text from which paragraphs and lines will be extracted.
     * @returns An object containing:
     *          - 'paragraphs': An array of paragraphs extracted from the text.
     *          - 'lines': An array of lines extracted from the text.
     */

    // Split the text into paragraphs
    const paragraphs = text.split('\n\n');

    // Split each paragraph into lines
    const lines = paragraphs.flatMap(paragraph => paragraph.split('\n'));

    // Remove empty paragraphs and lines
    const filteredParagraphs = paragraphs.filter(p => p.trim()).map(p => p.trim());
    const filteredLines = lines.filter(l => l.trim()).map(l => l.trim());

    // Return the extracted paragraphs and lines in an object
    return {
        paragraphs: filteredParagraphs,
        lines: filteredLines
    };
}