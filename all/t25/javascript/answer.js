import {fs} from 'fs'
/**
 * Classifies JSON objects by pid and writes matches and mismatches to separate files.
 * 
 * @param {string} sourceFile - Path to the source JSON file.
 * @param {Array} pidList - List of pids to match.
 * @param {string} matchFile - Path to save matching objects JSON.
 * @param {string} mismatchFile - Path to save mismatching objects JSON.
 */
function classifyJsonObjectsByPid(sourceFile, pidList, matchFile, mismatchFile) {
    try {
        // Load data from the source JSON file
        const data = JSON.parse(fs.readFileSync(sourceFile, 'utf-8'));
        
        // Initialize arrays for matches and mismatches
        const matches = [];
        const mismatches = [];

        // Classify each object based on 'pid' presence in 'pidList'
        data.forEach(obj => {
            if (pidList.includes(obj.pid)) {
                matches.push(obj);
            } else {
                mismatches.push(obj);
            }
        });

        // Save the matches to a new JSON file
        fs.writeFileSync(matchFile, JSON.stringify(matches, null, 4));

        // Save the mismatches to another JSON file
        fs.writeFileSync(mismatchFile, JSON.stringify(mismatches, null, 4));

        console.log("Classification complete. Data saved to respective files.");
    } catch (e) {
        console.error(`An error occurred: ${e.message}`);
    }
}