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
    // Read the file content
    const fileContent = fs.readFileSync(filename, 'utf-8');
    
    // Split the file content by lines
    const lines = fileContent.split('\n');
    
    // Initialize the result object
    const result = {};

    // Iterate over each line
    lines.forEach(line => {
        // Trim any leading/trailing whitespace and split by commas
        const sequence = line.trim().split(',').map(Number);
        
        // Check if the sequence is a Munodi sequence
        const isMunodiSequence = isMunodi(sequence);
        
        // Add the result to the result object
        result[sequence.join(',')] = isMunodiSequence;
    });

    return result;
}

/**
 * Helper function to determine if a given sequence is a Munodi sequence.
 * @param {Array<number>} sequence - The sequence to check.
 * @returns {boolean} True if the sequence is a Munodi sequence, false otherwise.
 */
function isMunodi(sequence) {
    // Iterate over the sequence
    for (let i = 0; i < sequence.length; i++) {
        const current = sequence[i];
        const next = sequence[i + 1];

        // If the current number is even, the next should be half of it
        if (current % 2 === 0) {
            if (next !== current / 2) {
                return false;
            }
        } 
        // If the current number is odd, the next should be 3*n + 1
        else {
            if (next !== 3 * current + 1) {
                return false;
            }
        }
    }

    // If we reach the end of the sequence without issues, it's a Munodi sequence
    return true;
}
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
