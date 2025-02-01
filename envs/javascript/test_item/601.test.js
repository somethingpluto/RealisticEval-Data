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
describe('Count words in various strings', () => {
    test('Empty string', () => {
        expect(countWords("")).toBe(0);
    });

    test('String with only spaces', () => {
        expect(countWords("     ")).toBe(0);
    });

    test('Single word', () => {
        expect(countWords("Hello")).toBe(1);
    });

    test('Multiple words with single spaces', () => {
        expect(countWords("This is a test string")).toBe(5);
    });

    test('Multiple spaces between words', () => {
        expect(countWords("This    is   a   test   string")).toBe(5);
    });

    test('Leading and trailing spaces', () => {
        expect(countWords("   Hello world!   ")).toBe(2);
    });
});
