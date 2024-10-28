/**
 * Extracts paragraphs and lines from the given text. Paragraphs end with \n\n and lines end with \n.
 * 
 * Example:
 *   Input: "First paragraph.\nThis is the second line.\n\nSecond paragraph.\nAnother line."
 *   Output: 
 *   {
 *     paragraphs: ["First paragraph.\nThis is the second line.", "Second paragraph.\nAnother line."],
 *     lines: ["First paragraph.", "This is the second line.", "Second paragraph.", "Another line."]
 *   }
 * 
 * @param text The input text from which paragraphs and lines will be extracted.
 * @returns A dictionary containing:
 *   - 'paragraphs': A list of paragraphs extracted from the text.
 *   - 'lines': A list of lines extracted from the text.
 */
function extractParagraphsAndLines(text: string): { paragraphs: string[], lines: string[] } {}