/**
 * Converts a string to Base64 encoding.
 *
 * @param {string} input - The string to be converted to Base64.
 * @returns {string} The Base64 encoded string.
 */
function convertToBase64(input) {
    // Create a Buffer from the input string
    const buffer = Buffer.from(input, 'utf-8');
    // Convert the Buffer to a Base64 encoded string
    return buffer.toString('base64');
}
