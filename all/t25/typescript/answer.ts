import * as fs from 'fs';
import { promisify } from 'util';

// Promisify the fs functions for better async/await usage
const readFile = promisify(fs.readFile);
const writeFile = promisify(fs.writeFile);

async function classifyJsonObjectsByPid(sourceFile: string, pidList: string[], matchFile: string, mismatchFile: string) {
    try {
        // Load questions from the source JSON file
        const dataBuffer = await readFile(sourceFile, 'utf8');
        const data = JSON.parse(dataBuffer);

        // Initialize arrays for matches and mismatches
        const matches = [];
        const mismatches = [];

        // Classify each object based on 'pid' presence in 'pidList'
        data.forEach((obj: any) => {
            if (pidList.includes(obj.pid)) {
                matches.push(obj);
            } else {
                mismatches.push(obj);
            }
        });

        // Save the matches to a new JSON file
        await writeFile(matchFile, JSON.stringify(matches, null, 4));

        // Save the mismatches to another JSON file
        await writeFile(mismatchFile, JSON.stringify(mismatches, null, 4));

        console.log("Classification complete. Data saved to respective files.");
    } catch (e) {
        console.error(`An error occurred: ${e}`);
    }
}

// Example usage
// classifyJsonObjectsByPid('source.json', ['123', '456'], 'matches.json', 'mismatches.json');