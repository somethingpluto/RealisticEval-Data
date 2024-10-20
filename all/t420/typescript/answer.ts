function readFileAsSequences(filePath: string): string[][] {
    const fs = require('fs');
    const fileContent = fs.readFileSync(filePath, 'utf-8');
    return fileContent.split('\n').map(line => line.trim().split(' '));
}

function findClosestWordIndices(sequence: string[], word1: string, word2: string): number {
    let word1Indices: number[] = [];
    let word2Indices: number[] = [];
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
            const distance = Math.abs(index1 - index2);
            if (distance < minDistance) {
                minDistance = distance;
            }
        });
    });

    return minDistance;
}

function getMinDistance(filePath: string, word1: string, word2: string): [number | null, number | null] {
    const sequences = readFileAsSequences(filePath);
    let minDistance = Infinity;
    let minSeqNum: number | null = null;

    sequences.forEach((seq, i) => {
        const distance = findClosestWordIndices(seq, word1, word2);
        if (distance < minDistance) {
            minDistance = distance;
            minSeqNum = i;
        }
    });

    if (minDistance === Infinity) {
        return [null, null];
    }

    return [minSeqNum, minDistance];
}
