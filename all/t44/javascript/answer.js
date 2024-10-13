/**
 * Align two lines of string to the left, supplementing with spaces if the length is not enough.
 *
 * @param {string} str1 - The first string.
 * @param {string} str2 - The second string.
 * @returns {Array} An array containing the aligned str1 and aligned str2.
 */
function alignLinesLeft(str1, str2) {
    // Determine the maximum length of the two strings
    const maxLength = Math.max(str1.length, str2.length);

    // Align both strings to the left by padding with spaces
    const alignedStr1 = str1.padEnd(maxLength, ' ');
    const alignedStr2 = str2.padEnd(maxLength, ' ');

    return [alignedStr1, alignedStr2];
}