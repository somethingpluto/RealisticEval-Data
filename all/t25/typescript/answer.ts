import * as fs from 'fs';

interface JsonObject {
    pid?: string; // Adjust type based on your expected pid structure
    [key: string]: any; // Allows for other properties in the object
}

function classifyJsonObjectsByPid(
    sourceFile: string,
    pidList: string[],
    matchFile: string,
    mismatchFile: string
): void {
    try {
        // Load JSON from the source file
        const data: JsonObject[] = JSON.parse(fs.readFileSync(sourceFile, 'utf-8'));
        
        // Initialize arrays for matches and mismatches
        const matches: JsonObject[] = [];
        const mismatches: JsonObject[] = [];

        // Classify each object based on 'pid' presence in 'pidList'
        for (const obj of data) {
            if (pidList.includes(obj.pid)) {
                matches.push(obj);
            } else {
                mismatches.push(obj);
            }
        }

        // Save matches to a new JSON file
        fs.writeFileSync(matchFile, JSON.stringify(matches, null, 4));

        // Save mismatches to another JSON file
        fs.writeFileSync(mismatchFile, JSON.stringify(mismatches, null, 4));

        console.log("Classification complete. Data saved to respective files.");
    } catch (error) {
        console.error(`An error occurred: ${error.message}`);
    }
}
