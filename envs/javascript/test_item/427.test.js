const fs = require('fs');

/**
 * Reads sequences from a file and determines if each sequence is a "Munodi sequence".
 * The definition of the Munodi sequence is based on a specific recursive relationship,
 * that is, for even numbers, the next term is half of it, for odd numbers, the next term is 3*n + 1,
 * and the sequence terminates when it encounters 1.
 * For example: (2, 4, 6, 8) is a Munodi sequence.
 *
 * @param {string} filename - The file path containing the sequences.
 * @returns {Object} An object mapping each sequence to a boolean indicating whether it is a Munodi sequence.
 */
function checkSequences(filename) {
    const munodiSequences = {};

    fs.readFile(filename, 'utf8', (err, data) => {
        if (err) {
            console.error(`Error reading file from disk: ${err}`);
        } else {
            const lines = data.split('\n');
            lines.forEach(line => {
                const sequence = line.split(',').map(Number);
                munodiSequences[line] = isMunodiSequence(sequence);
            });
        }
    });

    return munodiSequences;
}

function isMunodiSequence(sequence) {
    if (sequence.length === 0) return false;
    const [first, ...rest] = sequence;
    if (first === 1) return true;
    if (first % 2 === 0) {
        return isMunodiSequence([...rest, first / 2]);
    } else {
        return isMunodiSequence([...rest, 3 * first + 1]);
    }
}

module.exports = { checkSequences };
const fs = require('fs');
const os = require('os');
const path = require('path');

describe('TestCheckSequences', () => {
    let testFile;

    beforeAll(() => {
        // Set up the test cases with sequences
        testFile = 'test_sequences.dat';
        fs.writeFileSync(testFile, [
            "2,4,6,8",    // Munodi sequence (d = 2)
            "1,3,5,7",    // Munodi sequence (d = 2)
            "10,20,30",   // Munodi sequence (d = 10)
            "1,2,4,8",    // Not a Munodi sequence (d changes)
            "5,10,15,20"  // Munodi sequence (d = 5)
        ].join('\n'));
    });

    afterAll(() => {
        // Clean up the test file after tests
        fs.unlinkSync(testFile);
    });

    it('should correctly identify Munodi sequences', () => {
        const expectedResults = {
            "[2,4,6,8]": true,
            "[1,3,5,7]": true,
            "[10,20,30]": true,
            "[1,2,4,8]": false,
            "[5,10,15,20]": true,
        };

        const results = checkSequences(testFile);

        Object.keys(expectedResults).forEach(seqStr => {
            const seq = JSON.parse(seqStr);
            expect(results[seqStr]).toEqual(expectedResults[seqStr]);
        });
    });
});
