function readSequencesFromFile(filename) {
    // Read sequences from a file and return them as an array of arrays.
    const sequences = [];
    const fileContent = require('fs').readFileSync(filename, 'utf8');
    const lines = fileContent.split('\n');

    for (let line of lines) {
        // Assuming sequences are comma-separated in the file
        const seq = line.trim().split(',').map(num => parseInt(num, 10));  // Convert to an array of integers
        sequences.push(seq);
    }
    return sequences;
}

function isMunodiSequence(sequence) {
    // Check if the given sequence is a Munodi sequence.
    if (sequence.length < 2) {
        return false;  // A sequence with less than 2 elements cannot be a Munodi sequence
    }

    const commonDifference = sequence[1] - sequence[0];
    for (let i = 2; i < sequence.length; i++) {
        if (sequence[i] - sequence[i - 1] !== commonDifference) {
            return false;  // Found a different difference, not a Munodi sequence
        }
    }
    return true;  // All differences are the same
}

function checkSequences(filename) {
    // Read sequences from a file and determine if each is a Munodi sequence.
    const sequences = readSequencesFromFile(filename);
    const results = {};
    for (let seq of sequences) {
        results[JSON.stringify(seq)] = isMunodiSequence(seq);
    }
    return results;
}
