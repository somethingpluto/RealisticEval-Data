import * as re from 'xregexp';
import { Counter } from 'collections';

function wordFilterCounter(text: string, filterWords: string[]): Record<string, number> {
    /**
     * Counts the occurrences of specified words in the given text.
     *
     * This function filters the words from the text based on the provided list,
     * counts their occurrences, and returns a dictionary with the words in the
     * order they were provided.
     *
     * @param text - The input text from which to count words.
     * @param filterWords - A list of words to filter and count.
     * @returns A dictionary with the count of each filter word in the text,
     *          maintaining the order from filterWords.
     */

    // Convert filter words to lowercase for case-insensitive comparison
    const filterWordsSet = new Set(filterWords.map(word => word.toLowerCase()));

    // Find all words in the text using a regex pattern
    const words = re.match(text.toLowerCase(), /\b\w+(?:'\w+)?\b/g);

    // Count occurrences of filtered words
    const wordCounts = new Counter(words.filter(word => filterWordsSet.has(word)));

    // Create an ordered output based on the original order of filterWords
    const orderedOutput: Record<string, number> = {};
    for (const word of filterWords) {
        orderedOutput[word] = wordCounts.get(word.toLowerCase()) || 0;
    }

    return orderedOutput;
}