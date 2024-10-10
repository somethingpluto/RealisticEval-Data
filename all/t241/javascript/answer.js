const fs = require('fs');

function getMinSeqNumAndDistance(filePath, word1, word2) {
    let minLine = null;
    let minDistance = Infinity;

    const lines = fs.readFileSync(filePath, 'utf8').split('\n');
    for(let i = 0; i < lines.length; i++) {
        const words = lines[i].split(/\s+/);
        let index1 = -1;
        let index2 = -1;
        words.forEach((word, j) => {
            if(word === word1) index1 = j;
            if(word === word2) index2 = j;
        });
        if(index1 !== -1 && index2 !== -1) {
            const distance = Math.abs(index1 - index2);
            if(distance < minDistance) {
                minDistance = distance;
                minLine = i + 1;
            }
        }
    }

    return [minLine, minDistance];
}