function saveContentToFile(content, path) {
    /**
     * Saves the provided content to a specified file after cleaning up
     * redundant whitespace.
     *
     * @param {string} content - The text content to be saved to the file.
     * @param {string} path - The file path where the content will be saved.
     */

    // Remove redundant whitespace from the content.
    // Split the content into lines, strip leading/trailing whitespace,
    // and filter out empty lines.
    content = content.split('\n')
                    .map(line => line.trim())
                    .filter(line => line.length > 0)
                    .join('\n');

    // Replace multiple spaces with a single space.
    content = content.replace(/\s+/g, ' ');

    // Write the cleaned content to the specified file.
    const fs = require('fs');
    fs.writeFile(path, content, { encoding: 'utf-8' }, (err) => {
        if (err) throw err;
    });
}