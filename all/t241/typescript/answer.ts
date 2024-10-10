import fs from 'fs';
import { promisify } from 'util';

const readFile = promisify(fs.readFile);

async function getMinSeqNumAndDistance(filePath: string, word1: string, word2: string): Promise<[number | null, number]> {
    try {
        const data = await readFile(filePath, 'utf8');
        const lines = data.split('\n');

        let minLine: number | null = null;
        let minDist: number = Infinity;

        for (let i = 0; i < lines.length; i++) {
            const words = lines[i].split(/\s+/);
            const idx1 = words.indexOf(word1);
            const idx2 = words.indexOf(word2);

            if (idx1 !== -1 && idx2 !== -1) {
                const dist = Math.abs(idx1 - idx2);
                if (dist < minDist) {
                    minDist = dist;
                    minLine = i + 1;
                }
            }
        }

        return [minLine, minDist];
    } catch (error) {
        console.error(`Error reading file ${filePath}:`, error);
        return [null, Infinity];
    }
}