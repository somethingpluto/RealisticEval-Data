/**
 * Splits a comma-separated string into individual tokens.
 *
 * This function takes a string containing comma-separated values, trims
 * leading and trailing whitespace from each token, and stores the non-empty
 * tokens in the provided array.
 *
 * @param {string} str - The input string to be split, which may contain leading and
 *            trailing whitespace around the tokens.
 * @param {Array<string>} vect - An array where the resulting tokens will be stored. 
 *             The array will be cleared before storing the new tokens.
 */
function splitComma(str, vect) {
    // Clear the output array to avoid residual data
    vect.length = 0;

    // Process each comma-separated token
    const tokens = str.split(','); // Split the string by commas
    tokens.forEach(token => {
        // Trim leading and trailing whitespace
        token = token.trim();

        // Only add non-empty tokens to the array
        if (token) {
            vect.push(token);
        }
    });
}