/**
 * Compresses an HTML string by removing unnecessary whitespace without disrupting
 * the integrity of content within <pre>, <textarea>, <script>, and <style> tags.
 *
 * @param {string} htmlString - The HTML content to compress.
 * @returns {string} The compressed HTML content.
 */
function compressHTML(htmlString) {
    // Temporary replacements for safe elements where whitespace matters
    const blocks = {};
    let i = 0; // Unique key generator for replacements

    // Protect content of specific tags by replacing them with placeholders
    htmlString = htmlString.replace(/<(pre|textarea|script|style)([\s\S]*?)<\/\1>/gi, (match) => {
        const key = `@@${i++}@@`; // Generate a unique key
        blocks[key] = match; // Store original content in blocks object
        return key; // Replace original content with unique key
    });

    // Remove spaces around tags and compress all spaces and new lines
    htmlString = htmlString
        .replace(/>\s+|\s+</g, (m) => m.trim()) // Remove spaces around tags
        .replace(/(\r\n|\n|\r)\s*/gm, '') // Remove all newlines and spaces starting a newline
        .trim();

    // Restore protected tags' content from blocks
    htmlString = htmlString.replace(/@@\d+@@/g, (key) => blocks[key]);

    return htmlString;
}