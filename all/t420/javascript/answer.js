function readFileAsSequences(filePath) {
    // Read the file and convert each line into an array of words.
    const fs = require('fs');
    const fileContent = fs.readFileSync(filePath, 'utf8');
    const lines = fileContent.split('\n');
    return lines.map(line => line.trim().split(/\s+/));
}

function findClosestWordIndices(sequence, word1, word2) {
    // Find the indices of two words in a sequence and calculate their closest distances.
    let word1Indices = [];
    let word2Indices = [];
    let minDistance = Infinity;

    // Gather indices for both words
    sequence.forEach((word, index) => {
        if (word === word1) {
            word1Indices.push(index);
        } else if (word === word2) {
            word2Indices.push(index);
        }
    });

    // Calculate the minimum distance between all pairs of indices
    word1Indices.forEach(index1 => {
        word2Indices.forEach(index2 => {
            let distance = Math.abs(index1 - index2);
            if (distance < minDistance) {
                minDistance = distance;
            }
        });
    });

    return minDistance;
}

function getMinDistance(filePath, word1, word2) {
    // Determine the minimum distance between two words in any line of a file.
    const sequences = readFileAsSequences(filePath);
    let minDistance = Infinity;
    let minSeqNum = null;

    sequences.forEach((seq, i) => {
        let distance = findClosestWordIndices(seq, word1, word2);
        if (distance < minDistance) {
            minDistance = distance;
            minSeqNum = i;
        }
    });

    return minDistance !== Infinity ? [minSeqNum, minDistance] : [null, null];
}