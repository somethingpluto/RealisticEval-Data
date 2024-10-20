function readSequencesFromFile(filename: string): number[][] {
    const sequences: number[][] = [];
    const fileContent = require('fs').readFileSync(filename, 'utf8');
    const lines = fileContent.split('\n');

    for (const line of lines) {
        // Assuming sequences are comma-separated in the file
        const seq = line.trim().split(',').map((num) => parseInt(num, 10));
        sequences.push(seq);
    }

    return sequences;
}

function isMunodiSequence(sequence: number[]): boolean {
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

function checkSequences(filename: string): {[key: string]: boolean} {
    const sequences = readSequencesFromFile(filename);
    const results: {[key: string]: boolean} = {};
    for (const seq of sequences) {
        results[seq.toString()] = isMunodiSequence(seq);
    }

    return results;
}