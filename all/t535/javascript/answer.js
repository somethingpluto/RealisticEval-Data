/**
 * Converts an HTML string to a plain text string, removing excess line breaks and spaces.
 *
 * @param {string} html - The input HTML string.
 * @returns {string} The converted plain text string.
 */
function htmlToPlainText(html) {
    // Create a temporary DOM element to leverage the browser's HTML parsing
    const tempElement = document.createElement('div');

    // Set the innerHTML to the provided HTML string
    tempElement.innerHTML = html;

    // Get the text content of the temporary element
    let text = tempElement.innerText || tempElement.textContent || '';

    // Remove excess line breaks and spaces
    // Replace multiple line breaks with a single line break
    text = text.replace(/\n+/g, '\n'); // Replace multiple newlines with a single newline
    text = text.replace(/\s+/g, ' ').trim(); // Replace multiple spaces with a single space and trim leading/trailing spaces

    return text;
}
