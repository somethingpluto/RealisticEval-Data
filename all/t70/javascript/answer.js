function codeBlockRemover(markdownString) {
    // Regular expression to match code blocks in Markdown
    const regex = /(```[\s\S]*?```)/g;
    let matches;
    let codeBlocks = [];

    // Find all matches of code blocks
    while ((matches = regex.exec(markdownString)) !== null) {
        // Extract the content inside the code block
        const codeContent = matches[1].replace(/^[`~]{3}/, '').replace(/[`~]{3}$/, '');
        codeBlocks.push(codeContent);
    }

    return codeBlocks;
}