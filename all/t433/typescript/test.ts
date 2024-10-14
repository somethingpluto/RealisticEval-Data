/**
 * Extracts paragraphs and lines from the given text. The paragraphs end with \n\n The line end with \n
 *
 * Example:
 *     Input: "First paragraph.\nThis is the second line.\n\nSecond paragraph.\nAnother line."
 *     Output: {
 *         paragraphs: ["First paragraph.\nThis is the second line.", "Second paragraph.\nAnother line."],
 *         lines: ["First paragraph.", "This is the second line.", "Second paragraph.", "Another line."]
 *     }
 *
 * @param text The input text from which paragraphs and lines will be extracted.
 * @returns A dictionary containing:
 *          - 'paragraphs': A list of paragraphs extracted from the text.
 *          - 'lines': A list of lines extracted from the text.
 */
function extract_paragraphs_and_lines(text: string): { paragraphs: string[], lines: string[] } {
    const paragraphs = text.split('\n\n').map(paragraph => paragraph.trim());
    const lines = text.split('\n').map(line => line.trim()).filter(line => line.length > 0);

    return { paragraphs, lines };
}

// Test cases
describe('extract_paragraphs_and_lines', () => {
    it('should correctly extract paragraphs and lines', () => {
        const input = "First paragraph.\nThis is the second line.\n\nSecond paragraph.\nAnother line.";
        const expectedOutput = {
            paragraphs: ["First paragraph.\nThis is the second line.", "Second paragraph.\nAnother line."],
            lines: ["First paragraph.", "This is the second line.", "Second paragraph.", "Another line."]
        };
        const result = extract_paragraphs_and_lines(input);
        expect(result).toEqual(expectedOutput);
    });

    it('should handle empty input correctly', () => {
        const input = "";
        const expectedOutput = { paragraphs: [], lines: [] };
        const result = extract_paragraphs_and_lines(input);
        expect(result).toEqual(expectedOutput);
    });
});

export { extract_paragraphs_and_lines };