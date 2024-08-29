/**
 * Truncates a string to a specified length and appends an ellipsis if necessary.
 * Removes any paragraph tags from the truncated string.
 * 
 * @param {string} str - The string to be truncated.
 * @param {number} num - The maximum number of characters allowed.
 * @returns {string} - The truncated string with an ellipsis, or the original string if it's shorter than the limit.
 */
function sliceString(str, num) {
    // Check if the string length exceeds the specified limit
    if (str.length > num) {
        // Truncate the string and remove any paragraph tags
        return `${str.slice(0, num)}...`.replace(/<p>/g, "").replace(/<\/p>/g, "");
    }
    // Return the original string if it does not exceed the limit
    return str;
}
