/**
 * Compresses multiple consecutive whitespace characters in a string into a single space.
 *
 * @param inputString The string to be processed.
 * @returns The processed string with compressed whitespace.
 */
function compressWhitespace(inputString: string): string {
    return inputString.replace(/\s+/g, ' ').trim();
}