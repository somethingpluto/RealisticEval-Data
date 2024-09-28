const fs = require('fs');
const { diffLines } = require('diff');

function compareFiles(file1Path, file2Path) {
    /**
     * Compare the contents of two files and return the differences in unified diff format.
     *
     * Args:
     * file1Path (string): Path to the first file.
     * file2Path (string): Path to the second file.
     *
     * Returns:
     * Array<string>: An array containing the lines of differences, if any.
     *
     * Throws:
     * Error: If either file does not exist or there is an error reading the files.
     */

    let lines1, lines2;
    try {
        lines1 = fs.readFileSync(file1Path, 'utf-8');
        lines2 = fs.readFileSync(file2Path, 'utf-8');
    } catch (error) {
        if (error.code === 'ENOENT') {
            throw new Error("One of the files was not found.");
        } else {
            throw new Error(`Error reading files: ${error.message}`);
        }
    }

    const diff = diffLines(lines1, lines2);
    const diffLinesArray = [];

    diff.forEach((part) => {
        const prefix = part.added ? '+' : part.removed ? '-' : ' ';
        part.value.split('\n').forEach((line) => {
            if (line) {
                const diffLine = `${prefix} ${line}`;
                console.log(diffLine);
                diffLinesArray.push(diffLine);
            }
        });
    });

    return diffLinesArray;
}

// Example usage:
// compareFiles('path/to/file1.txt', 'path/to/file2.txt');