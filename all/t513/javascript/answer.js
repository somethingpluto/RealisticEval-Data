function isPhraseInStringIgnoreCase(phrase, string) {
    /**
     * Check if the given phrase exists in the target string, ignoring case and allowing for variations in whitespace.
     *
     * @param {string} phrase - The phrase to search for in the string.
     * @param {string} string - The target string in which to search for the phrase.
     * @returns {boolean} - True if the phrase is found as a whole word in the string, False otherwise.
     */

    // Convert both phrase and string to lower case
    phrase = phrase.toLowerCase();
    string = string.toLowerCase();

    // Escape special characters in the phrase
    const escapeRegExp = (str) => str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    let escapedPhrase = escapeRegExp(phrase);

    // Replace spaces in the phrase with \s+ to allow for any whitespace variations
    escapedPhrase = escapedPhrase.replace(/\\ /g, '\\s+');

    // Construct the regex pattern with word boundaries
    const pattern = new RegExp(`\\b${escapedPhrase}\\b`, 'g');

    // Search for the pattern in the target string
    return pattern.test(string);
}