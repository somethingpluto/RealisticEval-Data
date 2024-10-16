/**
 * Counts the number of words in a given string.
 *
 * A word is defined as a sequence of characters separated by whitespace.
 * This function handles leading and trailing whitespace, as well as
 * multiple spaces between words.
 *
 * @param {string} str The input string in which words are to be counted.
 * @return {number} The count of words in the input string.
 */
function countWords(str) {
    // Initialize a word count variable
    let wordCount = 0; // Use let for block scoping
    const words = str.trim().split(/\s+/); // Split the string by whitespace

    // Count the words
    for (const word of words) {
        if (word) { // Check if the word is not empty
            wordCount++; // Increment the count for each word found
        }
    }

    return wordCount; // Return the total word count
}