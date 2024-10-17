const assert = require('assert'); // For testing purposes

function wordFilterCounter(text, filterWords) {
    /**
     * Counts the occurrences of specified words in the given text.
     *
     * This function filters the words from the text based on the provided list,
     * counts their occurrences, and returns an object with the words in the
     * order they were provided.
     *
     * @param {string} text - The input text from which to count words.
     * @param {Array<string>} filterWords - An array of words to filter and count.
     * @returns {Object} An object with the count of each filter word in the text,
     *                   maintaining the order from filterWords.
     */

    // Convert filter words to lowercase for case-insensitive comparison
    const filterWordsSet = new Set(filterWords.map(word => word.toLowerCase()));

    // Find all words in the text using a regex pattern
    const words = text.toLowerCase().match(/\b\w+(?:'\w+)?\b/g);

    // Count occurrences of filtered words
    const wordCounts = {};
    if (words) {
        words.forEach(word => {
            if (filterWordsSet.has(word)) {
                wordCounts[word] = (wordCounts[word] || 0) + 1;
            }
        });
    }

    // Create an ordered output based on the original order of filterWords
    const orderedOutput = {};
    filterWords.forEach(word => {
        orderedOutput[word] = wordCounts[word.toLowerCase()] || 0;
    });

    return orderedOutput;
}
