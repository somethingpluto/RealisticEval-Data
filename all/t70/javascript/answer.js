/**
 * Extracts all code block contents from a markdown string.
 *
 * @param {string} markdownString - The input markdown string.
 * @returns {Array<string>} An array of strings, each representing the content of a code block.
 *                           Returns an empty array if no code blocks are found.
 */
function codeBlockRemover(markdownString) {
    const pattern = /```[a-zA-Z]*\n([\s\S]*?)```/g;
    const codeBlocks = markdownString.match(pattern);
    if (codeBlocks) {
        return codeBlocks.map(block => block.replace(/```[a-zA-Z]*\n|```/g, '').trim());
    }
    return [];
}