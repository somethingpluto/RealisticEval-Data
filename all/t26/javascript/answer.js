/**
 * Converts an input string with multiple separators to a comma-separated string.
 * Now handles additional separators: hyphens (-) and colons (:).
 *
 * @param {string} inputString - The input string containing various separators like *, ;, /, -, :
 * @returns {string} A comma-separated string where all specified separators have been replaced with commas.
 */
function convertToCommaSeparated(inputString) {
    const pattern = /[\*;\/\-:]/g;
    const commaSeparatedString = inputString.replace(pattern, ',');
    return commaSeparatedString;
}