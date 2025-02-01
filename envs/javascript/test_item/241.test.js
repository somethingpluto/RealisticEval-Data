/**
 * Finds the minimum distance between two words in a text file, considering each line as a separate sequence.
 * @param {string} filePath - The path to the file to read.
 * @param {string} word1 - The first word to search for.
 * @param {string} word2 - The second word to search for.
 * @returns {Array} An array containing the line number with the minimum distance and the minimum distance itself.
 *                  Returns [null, Infinity] if one or both words are not found in any line.
 */
function getMinSeqNumAndDistance(filePath, word1, word2) {
    const fs = require('fs');
    let fileContent = fs.readFileSync(filePath, 'utf8');
    let lines = fileContent.split('\n');
    let minDistance = Infinity;
    let minSeqNum = null;

    for (let i = 0; i < lines.length; i++) {
        let line = lines[i].trim().toLowerCase();
        let index1 = line.indexOf(word1.toLowerCase());
        let index2 = line.indexOf(word2.toLowerCase());

        if (index1 !== -1 && index2 !== -1) {
            let distance = Math.abs(index1 - index2) - 1;
            if (distance < minDistance) {
                minDistance = distance;
                minSeqNum = i + 1;
            }
        }
    }

    return [minSeqNum, minDistance === Infinity ? null : minDistance];
}
const fs = require('fs');
describe('TestGetMinDistance', () => {
    it('test basic functionality with expected input', () => {
        const mockContent = "hello world\napple banana apple\norange apple banana";
        const mockFs = {
            readFileSync: jest.fn(() => mockContent),
        };

        global.fs = mockFs;

        const [lineNumber, distance] = getMinSeqNumAndDistance('dummy_file.txt', 'apple', 'banana');
        expect([lineNumber, distance]).toEqual([2, 1]);
    });

    it('test case where one or both words are not present', () => {
        const mockContent = "apple orange pear\norange pear apple";
        const mockFs = {
            readFileSync: jest.fn(() => mockContent),
        };

        global.fs = mockFs;

        const [lineNumber, distance] = getMinSeqNumAndDistance('dummy_file.txt', 'apple', 'banana');
        expect([lineNumber, distance]).toEqual([null, Infinity]);
    });

    it('test an empty file', () => {
        const mockContent = '';
        const mockFs = {
            readFileSync: jest.fn(() => mockContent),
        };

        global.fs = mockFs;

        const [lineNumber, distance] = getMinSeqNumAndDistance('dummy_file.txt', 'apple', 'banana');
        expect([lineNumber, distance]).toEqual([null, Infinity]);
    });

    it('test multiple lines with varying distances between words', () => {
        const mockContent = "apple banana\napple orange orange banana\napple orange orange orange banana";
        const mockFs = {
            readFileSync: jest.fn(() => mockContent),
        };

        global.fs = mockFs;

        const [lineNumber, distance] = getMinSeqNumAndDistance('dummy_file.txt', 'apple', 'banana');
        expect([lineNumber, distance]).toEqual([1, 1]);
    });
});
