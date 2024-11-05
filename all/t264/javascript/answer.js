import fs from 'fs'
function extractLogEntries(logFilePath) {
    /**
     * Extract log entries from a log file for WARNING, ERROR, CRITICAL, and ALERT levels
     * and save each type of log entry to a different file.
     *
     * @param {string} logFilePath - Path to the log file.
     */
    if (!fs.existsSync(logFilePath)) {
        throw new Error(`No log file found at the specified path: ${logFilePath}`);
    }

    // Prepare objects to hold log entries for each level
    const logs = {
        'WARNING': [],
        'ERROR': [],
        'CRITICAL': [],
        'ALERT': []
    };

    // Define output file paths
    const outputFiles = {
        'WARNING': 'warning_logs.txt',
        'ERROR': 'error_logs.txt',
        'CRITICAL': 'critical_logs.txt',
        'ALERT': 'alert_logs.txt'
    };

    // Read the log file and filter entries by level
    const fileContent = fs.readFileSync(logFilePath, 'utf8');
    const lines = fileContent.split('\n');

    lines.forEach(line => {
        for (const level of Object.keys(logs)) {
            if (line.includes(level)) {
                logs[level].push(line);
                break;
            }
        }
    });

    // Write the filtered logs to separate files
    for (const [level, entries] of Object.entries(logs)) {
        fs.writeFileSync(outputFiles[level], entries.join('\n'));
        console.log(`Saved ${entries.length} '${level}' entries to ${outputFiles[level]}.`);
    }
}