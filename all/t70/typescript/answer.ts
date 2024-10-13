import { match } from "assert";

function codeBlockRemover(markdownString: string): string[] {
    /**
     * Extracts all code block contents from a markdown string.
     *
     * @param markdownString - The input markdown string.
     * @returns An array of strings, each representing the content of a code block.
     *          Returns an empty array if no code blocks are found.
     */
    // Define a pattern that captures content within triple backticks, with optional language specifier
    const pattern = /```[a-zA-Z]*\n([\s\S]*?)```/g;

    // Use String.match() to find all occurrences of the pattern
    const matches = markdownString.match(pattern);

    // Extract the content of each code block
    const codeBlocks = matches ? matches.map(match => match.replace(/```[a-zA-Z]*\n|```/g, '')) : [];

    return codeBlocks;
}