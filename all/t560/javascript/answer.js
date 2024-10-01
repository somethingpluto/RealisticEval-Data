/**
 * Gets the line number in the content at the specified index.
 *
 * @param {string} content - The string content to check.
 * @param {number} index - The character index to find the line number for.
 * @returns {number} - The line number corresponding to the given index.
 */
function getLineNumber(content, index) {
    // Use a regular expression to count the number of newline characters before the index
    return (content.slice(0, index).match(/\n/g) || []).length + 1;
}