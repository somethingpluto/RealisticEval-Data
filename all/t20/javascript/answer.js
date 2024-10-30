/**
 * Transforms the input text by finding and modifying patterns that match the format '(*...*)'.
 * Specifically, it removes any asterisks inside the parentheses while preserving the outer format.
 * For example:
 *     input: *he*l*lo*
 *     output: *hello*
 *
 * @param {string} text - The input text containing patterns to be transformed.
 * @returns {string} - The transformed text with asterisks inside '(*...*)' patterns removed.
 */
function removeInnerAsterisks(text) {
    const pattern = /\(\*(.*?)\*\)/g;
    const removeInnerAsterisks = (match, content) => {
        content = content.replace(/\*/g, ''); // Remove inner asterisks
        return `(*${content}*)`; // Return the modified format
    };
    return text.replace(pattern, removeInnerAsterisks);
}