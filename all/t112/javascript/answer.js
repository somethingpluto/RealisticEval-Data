/**
 * Converts HTML heading tags (h1-h6) to corresponding Markdown headings.
 *
 * @param {string} html - The HTML string containing headings.
 * @returns {string} - The converted Markdown string.
 */
function convertHtmlHeadingsToMarkdown(html) {
    // Replace h1 to h6 tags with corresponding Markdown headings
    return html
        .replace(/<h1>(.*?)<\/h1>/g, '# \$1')         // Converts <h1> to #
        .replace(/<h2>(.*?)<\/h2>/g, '## \$1')        // Converts <h2> to ##
        .replace(/<h3>(.*?)<\/h3>/g, '### \$1')       // Converts <h3> to ###
        .replace(/<h4>(.*?)<\/h4>/g, '#### \$1')      // Converts <h4> to ####
        .replace(/<h5>(.*?)<\/h5>/g, '##### \$1')     // Converts <h5> to #####
        .replace(/<h6>(.*?)<\/h6>/g, '###### \$1');   // Converts <h6> to ######
}