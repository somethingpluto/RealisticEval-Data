const fs = require('fs');
const path = require('path');

/**
 * Recursively searches for Markdown files in the specified directory.
 *
 * @param {string} dir - The directory path to search in.
 * @returns {string[]} - An array of paths to Markdown files.
 */
function findMarkdownFiles(dir) {
    let markdownFiles = [];

    // Read the contents of the directory
    const files = fs.readdirSync(dir);

    files.forEach(file => {
        const filePath = path.join(dir, file);
        const stat = fs.statSync(filePath);

        // If it's a directory, recurse into it
        if (stat.isDirectory()) {
            markdownFiles = markdownFiles.concat(findMarkdownFiles(filePath));
        }
        // If it's a Markdown file, add it to the list
        else if (filePath.endsWith('.md')) {
            markdownFiles.push(filePath);
        }
    });

    return markdownFiles;
}