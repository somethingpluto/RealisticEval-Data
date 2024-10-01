/**
 * Counts the occurrences of consecutive identical letters in a given string.
 *
 * @param {string} inputString - The string to analyze for letter changes.
 * @returns {Array<number>} An array of counts representing the number of consecutive
 *                          identical letters before a different letter is found.
 */
function countLetterChanges(inputString) {
    // Array to hold counts of consecutive letters
    const counts = [];
    let currentCount = 1; // Initialize the count of the current letter

    // Iterate through the string starting from the second character
    for (let i = 1; i < inputString.length; i++) {
        // If the current character is different from the previous one
        if (inputString[i] !== inputString[i - 1]) {
            counts.push(currentCount); // Store the count of the previous letter
            currentCount = 1; // Reset count for the new letter
        } else {
            currentCount++; // Increment count for the current letter
        }
    }

    counts.push(currentCount); // Push the count of the last letter
    return counts;
}
