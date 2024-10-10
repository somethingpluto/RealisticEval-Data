const fs = require('fs');
const readline = require('readline');

function readColumns(fileName) {
    return new Promise((resolve, reject) => {
        const stream = fs.createReadStream(fileName);
        let lines = [];
        let index = -1;

        const rl = readline.createInterface({
            input: stream,
            crlfDelay: Infinity
        });

        rl.on('line', (line) => {
            if (index === -1 && line.includes('/')) {
                index = lines.length;
            }
            lines.push(line.trim());
        });

        rl.on('close', () => {
            if (index === -1) {
                reject(new Error("File does not contain any '/' character"));
            } else {
                resolve(lines.slice(index + 1).map(line => line.split(/\s+/).map(Number)));
            }
        });
    });
}

module.exports = readColumns;