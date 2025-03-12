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
function wordFilterCounter(text, filterWords) {
    // Initialize an object to store the counts
    const wordCounts = {};

    // Convert the text to lowercase and split it into words
    const words = text.toLowerCase().split(/\W+/);

    // Initialize the wordCounts object with the filterWords
    filterWords.forEach(word => {
        wordCounts[word] = 0;
    });

    // Count the occurrences of each filter word in the text
    words.forEach(word => {
        if (wordCounts.hasOwnProperty(word)) {
            wordCounts[word]++;
        }
    });

    return wordCounts;
}
describe('TestWordFilterCounter', () => {
    it('test_case1', () => {
        const text = "go to the school.go to the park.";
        const filterWords = ["go", "to", "the", "school", "park", "play"];
        const expectedOutput = {
            go: 2,
            to: 2,
            the: 2,
            school: 1,
            park: 1,
            play: 0
        };
        expect(wordFilterCounter(text, filterWords)).toEqual(expectedOutput);
    });

    it('test_case2', () => {
        const text = "This is a completely different sentence.";
        const filterWords = ["I'll", "go", "to", "the", "school", "park", "play"];
        const expectedOutput = {
            "I'll": 0,
            go: 0,
            to: 0,
            the: 0,
            school: 0,
            park: 0,
            play: 0
        };
        expect(wordFilterCounter(text, filterWords)).toEqual(expectedOutput);
    });

    it('test_case3', () => {
        const text = "I will not go to the school's park.";
        const filterWords = ["I", "will", "not", "go", "to", "the", "school's", "park"];
        const expectedOutput = {
            I: 1,
            will: 1,
            not: 1,
            go: 1,
            to: 1,
            the: 1,
            "school's": 1,
            park: 1
        };
        expect(wordFilterCounter(text, filterWords)).toEqual(expectedOutput);
    });
});
