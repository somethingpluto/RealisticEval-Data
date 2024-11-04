import fs from 'fs'

/**
 * Reads numerical columns from a file starting from the line after the last line containing '/'.
 *
 * @param {string} fileName - The name of the file to read.
 * @returns {Array<Array<number>>} - A 2D array containing the numerical data.
 * @throws {Error} - If the file does not contain any '/' character.
 */
function readColumns(fileName) {
    let lastSlashIndex = null;
    const lines = fs.readFileSync(fileName, 'utf8').split('\n');
    for (let i = 0; i < lines.length; i++) {
        if (lines[i].includes('/')) {
            lastSlashIndex = i;
        }
    }
    if (lastSlashIndex === null) {
        throw new Error("File does not contain '/' character");
    }
    const dataLines = lines.slice(lastSlashIndex + 1);
    const filteredDataLines = dataLines.filter(line => line.trim() && !line.trim().startsWith('!'));
    if (filteredDataLines.length === 0) {
        return [];
    }
    const colCount = filteredDataLines[0].split(' ').length;
    const arr = new Array(filteredDataLines.length).fill(null).map(() => new Array(colCount).fill(0));
    for (let i = 0; i < filteredDataLines.length; i++) {
        const nums = filteredDataLines[i].split(' ').map(Number);
        arr[i] = nums;
    }
    return arr;
}