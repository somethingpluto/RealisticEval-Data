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
    // Regular expression to find patterns like (*...*)
    const pattern = /\(\*(.*?)\*\)/g;

    // Function to replace matched patterns
    const removeInnerAsterisks = (match, content) => {
        content = content.replace(/\*/g, ''); // Remove inner asterisks
        return `(*${content}*)`; // Return the modified format
    };

    // Substitute the pattern in text with the processed content
    return text.replace(pattern, removeInnerAsterisks);
}