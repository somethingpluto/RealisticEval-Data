import {fs} from 'fs';
import {diff} from 'diff'
/**
 * Compare the contents of two files and print the differences in unified diff format.
 *
 * @param {string} file1Path - Path to the first file.
 * @param {string} file2Path - Path to the second file.
 * @returns {Promise<Array<string>>} A promise that resolves to a list containing the lines of differences, if any.
 * @throws {Error} If either file does not exist or there is an error reading the files.
 */
async function compareFiles(file1Path, file2Path) {
    try {
        const file1Content = await fs.promises.readFile(file1Path, 'utf8');
        const file2Content = await fs.promises.readFile(file2Path, 'utf8');

        const lines1 = file1Content.split('\n');
        const lines2 = file2Content.split('\n');

        const diffResult = diff.diffLines(lines1.join('\n'), lines2.join('\n'));
        const diffLines = diffResult.map(part => part.value).join('\n').split('\n');

        diffLines.forEach(line => console.log(line));

        return diffLines;
    } catch (error) {
        if (error.code === 'ENOENT') {
            throw new Error('One of the files was not found.');
        }
        throw new Error(`Error reading files: ${error.message}`);
    }
}