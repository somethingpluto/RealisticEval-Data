import { escape as escapeRegex } from 'lodash';

function isPhraseInStringIgnoreCase(phrase: string, string: string): boolean {
    /**
     * Check if the given phrase exists in the target string, ignoring case and allowing for variations in whitespace.
     *
     * @param phrase - The phrase to search for in the string.
     * @param string - The target string in which to search for the phrase.
     * @returns True if the phrase is found as a whole word in the string, False otherwise.
     */
    // Convert both phrase and string to lower case
    const lowerCasePhrase = phrase.toLowerCase();
    const lowerCaseString = string.toLowerCase();

    // Escape special characters in the phrase
    const escapedPhrase = escapeRegex(lowerCasePhrase);

    // Replace spaces in the phrase with \s+ to allow for any whitespace variations
    const escapedPhraseWithWhitespace = escapedPhrase.replace(/\\ /g, '\\s+');

    // Construct the regex pattern with word boundaries
    const pattern = new RegExp(`\\b${escapedPhraseWithWhitespace}\\b`, 'i');

    // Search for the pattern in the target string
    return pattern.test(lowerCaseString);
}
