const fs = require('fs');

function classifyJsonObjectsByPid(sourceFile, pidList, matchFile, mismatchFile) {
    /**
     * Reads JSON questions from a file, filters objects based on 'pid' field inclusion in 'pidList'.
     * Writes matches and mismatches to separate JSON files.
     *
     * Args:
     * sourceFile (string): Path to the source JSON file.
     * pidList (array): List of pids to match.
     * matchFile (string): Path to save matching objects JSON.
     * mismatchFile (string): Path to save mismatching objects JSON.
     */
    try {
        // Load question from the source JSON file
        const data = JSON.parse(fs.readFileSync(sourceFile, 'utf8'));
        // Initialize arrays for matches and mismatches
        const matches = [];
        const mismatches = [];

        // Classify each object based on 'pid' presence in 'pidList'
        data.forEach((obj) => {
            if (pidList.includes(obj.pid)) {
                matches.push(obj);
            } else {
                mismatches.push(obj);
            }
        });

        // Save the matches to a new JSON file
        fs.writeFileSync(matchFile, JSON.stringify(matches, null, 4), 'utf8');

        // Save the mismatches to another JSON file
        fs.writeFileSync(mismatchFile, JSON.stringify(mismatches, null, 4), 'utf8');

        console.log("Classification complete. Data saved to respective files.");
    } catch (e) {
        console.error(`An error occurred: ${e.message}`);
    }
}