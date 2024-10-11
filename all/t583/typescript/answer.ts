/**
 * Removes the specified parameter from the URL query string.
 *
 * @param {string} url - The URL from which to remove the parameter.
 * @param {string} key - The key of the parameter to remove.
 * @returns {string} - The modified URL with the specified parameter removed.
 */
function removeQueryParam(url: string, key: string): string {
    // Create a URL object to easily manipulate the URL
    const urlObj = new URL(url);

    // Get the current search parameters
    const params = new URLSearchParams(urlObj.search);

    // Delete the specified key
    params.delete(key);

    // Set the new search parameters back to the URL object
    urlObj.search = params.toString();

    // Return the modified URL
    return urlObj.toString();
}