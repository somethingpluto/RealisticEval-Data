import { compile } from 'path-to-regexp';

function splitIntoSentences(text: string): string[] {
    /**
     * Split the input text string into sentences.
     *
     * @param text - The input text to be split into sentences.
     * @returns An array of sentences extracted from the input text, cleaned and stripped of leading/trailing whitespace.
     */

    // Check if the input is a string
    if (typeof text !== 'string') {
        throw new Error('Input must be a string.');
    }

    // Regular expression to split the text where there is a punctuation followed by space or end of string
    // This handles situations where punctuation might be followed by a quotation mark or other punctuation
    const sentenceDelimiters = /(?<=[.!?])\s+(?=[A-Z])|(?<=[.!?]["”’])\s+(?=[A-Z])/g;

    // Split the text using the defined regular expression
    const sentences = text.split(sentenceDelimiters);

    // Remove any leading or trailing whitespace from each sentence
    const cleanedSentences = sentences.filter(sentence => sentence.trim().length > 0).map(sentence => sentence.trim());

    // Return the cleaned list of sentences
    return cleanedSentences;
}
