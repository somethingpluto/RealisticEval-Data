/**
 * Decodes HTML entities in a given HTML string.
 * @param {string} htmlString - The HTML string containing entities to decode.
 * @returns {string} The decoded string with HTML entities converted back to their original characters.
 */
function replaceHtmlEntities(htmlString) {
    if (typeof htmlString !== 'string') {
        throw new TypeError('Input must be a string.');
    }

    // Use a DOMParser to parse the string as HTML
    const parser = new DOMParser();
    const doc = parser.parseFromString(htmlString, 'text/html');

    // Return the text content, effectively decoding HTML entities
    return doc.documentElement.textContent || "";
}