/**
 * Count the number of letters in a string.
 *
 * @param {string} str - The input string from which to count letters.
 * @returns {number} - The count of letters in the string.
 */
function countLetters(str) {
    // Use a regular expression to match all letter characters (both uppercase and lowercase)
    const letters = str.match(/[a-zA-Z]/g);

    // Return the number of letters found, or 0 if none are found
    return letters ? letters.length : 0;
}