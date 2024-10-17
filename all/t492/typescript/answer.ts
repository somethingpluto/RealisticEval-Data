function saveContentToFile(content: string, path: string): void {
    /**
     * Saves the provided content to a specified file after cleaning up redundant whitespace.
     *
     * @param content - The text content to be saved to the file.
     * @param path - The file path where the content will be saved.
     */

    // Remove redundant whitespace from the content.
    // Split the content into lines, strip leading/trailing whitespace,
    // and filter out empty lines.
    const lines = content.split('\n').filter(line => line.trim().length > 0).map(line => line.trim());
    content = lines.join('\n');

    // Replace multiple spaces with a single space.
    content = content.replace(/\s+/g, ' ');

    // Write the cleaned content to the specified file.
    const fs = require('fs');
    fs.writeFileSync(path, content, { encoding: 'utf-8' });
}