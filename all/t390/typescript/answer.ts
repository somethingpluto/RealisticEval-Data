import { compile } from 'path-to-regexp';

function splitIntoSentences(text: string): string[] {
    if (typeof text !== 'string') {
        throw new Error('Input must be a string.');
    }
    const sentenceDelimiters = /(?<=[.!?])\s+(?=[A-Z])|(?<=[.!?]["”’])\s+(?=[A-Z])/g;
    const sentences = text.split(sentenceDelimiters);
    const cleanedSentences = sentences.filter(sentence => sentence.trim().length > 0).map(sentence => sentence.trim());
    return cleanedSentences;
}