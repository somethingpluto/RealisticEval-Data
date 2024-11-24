function isPhraseInStringIgnoreCase(phrase, string) {
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