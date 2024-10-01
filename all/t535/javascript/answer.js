/**
 * Compresses an HTML string by removing unnecessary whitespace, 
 * including newlines, tabs, and extra spaces, 
 * while preserving the structure of the HTML.
 * 
 * @param {string} html - The input HTML string to be compressed.
 * @returns {string} - The compressed HTML string with reduced whitespace.
 */
function compressHtml(html) {
    return html
        // Remove all newline and tab characters from the string
        .replace(/[\r\n\t]+/g, '')  // Removes newlines and tabs
        
        // Replace multiple consecutive spaces with a single space
        .replace(/ {2,}/g, ' ')      // Replaces multiple spaces with a single space
        
        // Remove spaces between HTML tags (e.g., transforming "> <" into "><")
        .replace(/> <+/g, '><')      // Removes spaces between HTML tags
        
        // Trim any leading and trailing whitespace from the final string
        .trim();                     // Trims whitespace from the start and end of the string
}
