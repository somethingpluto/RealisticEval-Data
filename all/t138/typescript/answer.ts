/**
 * Removes all punctuation from a given string, converts the string to lowercase,
 * and trims whitespace from both ends.
 *
 * @param {string} str - The string from which to remove punctuation.
 * @returns {string} The cleaned and formatted string.
 */
function removePunctuation(str: string): string {
    // Define a regex pattern that matches common punctuation characters.
    // This includes Unicode punctuation and ASCII punctuation.
    const punctuationRegex = /[\u2000-\u206F\u2E00-\u2E7F!"#$%&'()*+,\-./:;<=>?@\[\]^_`{|}~]/g;
    return str.replace(punctuationRegex, '').toLowerCase().trim();
}