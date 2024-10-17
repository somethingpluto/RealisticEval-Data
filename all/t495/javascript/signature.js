/**
 * Filters website content to include lines containing any of the specified keywords as whole words,
 * along with a specified number of lines before and after for context. This version uses regular expressions
 * to ensure exact, whole word matching and respects case sensitivity.
 *
 * @param {string} content - The full text content of the website.
 * @param {Array<string>} keywords - A list of strings to search for within the content.
 * @param {number} [linesBefore=1] - Number of lines to include before a matching line.
 * @param {number} [linesAfter=1] - Number of lines to include after a matching line.
 * @returns {string} - A string containing the filtered content with additional context.
 */
function filterContentWithContext(content, keywords, linesBefore = 1, linesAfter = 1) {

}