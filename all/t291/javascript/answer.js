function prependToEachLine(filePath, prefix) {
    /**
     * Prepends the specified string to the beginning of each line of the file.
     *
     * @param {string} filePath - Path to the file whose lines will be modified.
     * @param {string} prefix - String to prepend to the beginning of each line.
     */

    // Read the file content
    const fs = require('fs');
    let data = fs.readFileSync(filePath, 'utf8');

    // Split the data into lines
    let lines = data.split('\n');

    // Prepend the prefix to each line
    lines = lines.map(line => prefix + line);

    // Join the lines back together
    data = lines.join('\n');

    // Write the modified content back to the file
    fs.writeFileSync(filePath, data, 'utf8');
}