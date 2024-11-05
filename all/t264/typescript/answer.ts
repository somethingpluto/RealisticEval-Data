import * as fs from 'fs';

function extractLogEntries(logFilePath: string): void {
    /**
     * Extract log entries from a log file for WARNING, ERROR, CRITICAL, and ALERT levels
     * and save each type of log entry to a different file.
     *
     * @param logFilePath - Path to the log file.
     */
    if (!fs.existsSync(logFilePath)) {
        throw new Error(`No log file found at the specified path: ${logFilePath}`);
    }

    // Prepare objects to hold log entries for each level
    const logs: { [key: string]: string[] } = {
        'WARNING': [],
        'ERROR': [],
        'CRITICAL': [],
        'ALERT': []
    };

    // Define output file paths
    const outputFiles: { [key: string]: string } = {
        'WARNING': 'warning_logs.txt',
        'ERROR': 'error_logs.txt',
        'CRITICAL': 'critical_logs.txt',
        'ALERT': 'alert_logs.txt'
    };

    // Read the log file and filter entries by level
    const fileContent = fs.readFileSync(logFilePath, 'utf-8');
    const lines = fileContent.split('\n');

    for (const line of lines) {
        for (const level of Object.keys(logs)) {
            if (line.includes(level)) {
                logs[level as keyof typeof logs].push(line);
                break;
            }
        }
    }

    // Write the filtered logs to separate files
    for (const level of Object.keys(logs)) {
        const entries = logs[level as keyof typeof logs];
        fs.writeFileSync(outputFiles[level as keyof typeof outputFiles], entries.join('\n'));
        console.log(`Saved ${entries.length} '${level}' entries to ${outputFiles[level as keyof typeof outputFiles]}.`);
    }
}