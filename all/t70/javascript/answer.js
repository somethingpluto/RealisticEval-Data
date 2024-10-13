function codeBlockRemover(markdownString) {
    /**
     * Extracts all code block contents from a markdown string.
     *
     * @param {string} markdownString - The input markdown string.
     * @returns {Array<string>} An array of strings, each representing the content of a code block.
     *                           Returns an empty array if no code blocks are found.
     */
    
    // Define a pattern that captures content within triple backticks, with optional language specifier
    const pattern = /```[a-zA-Z]*\n([\s\S]*?)```/g;

    // Use match() to find all occurrences of the pattern
    const codeBlocks = markdownString.match(pattern);

    // Extract the content of each code block by removing the surrounding ``` and trimming newlines
    if (codeBlocks) {
        return codeBlocks.map(block => block.replace(/```[a-zA-Z]*\n|```/g, '').trim());
    }

    return [];
}