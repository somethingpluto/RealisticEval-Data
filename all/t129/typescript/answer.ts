/**
 * Validates a URL string using a simplified and more comprehensive regular expression.
 *
 * @param {string} str - The URL string to validate.
 * @returns {boolean} True if the URL is valid, false otherwise.
 */
function validURL(str: string): boolean {
    // Simplified and robust regex for URL validation
    const pattern = new RegExp('^(http|https?:\\/\\/)?' + // protocol
        '((([a-zA-Z\\d]([a-zA-Z\\d-]*[a-zA-Z\\d])*)\\.)+[a-zA-Z]{2,}|' + // domain name and extension
        '((\\d{1,3}\\.){3}\\d{1,3}))' + // OR ip (v4) address
        '(\\:\\d+)?' + // port
        '(\\/[-a-zA-Z\\d%_.~+]*)*' + // path
        '(\\?[;&amp;a-zA-Z\\d%_.~+=-]*)?' + // query string
        '(\\#[-a-zA-Z\\d_]*)?$', 'i'); // fragment locator
    return !!pattern.test(str);
}