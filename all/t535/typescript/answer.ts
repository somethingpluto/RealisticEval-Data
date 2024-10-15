/**
 * Compresses an HTML string by removing unnecessary whitespace, 
 * including newlines, tabs, and extra spaces, 
 * while preserving the structure of the HTML.
 * 
 * @param {string} html - The input HTML string to be compressed.
 * @returns {string} - The compressed HTML string with reduced whitespace.
 */
function compressHtml(html: string): string {
    return html
        .replace(/[\r\n\t]+/g, '')  // Removes newlines and tabs
        .replace(/ {2,}/g, ' ')      // Replaces multiple spaces with a single space
        .replace(/> <+/g, '><')      // Removes spaces between HTML tags
        .trim();                     // Trims whitespace from the start and end of the string
}