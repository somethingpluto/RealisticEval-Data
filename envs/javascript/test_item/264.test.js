const fs = require('fs');
const path = require('path');

/**
 * Extract log entries from a log file for WARNING, ERROR, CRITICAL, and ALERT levels
 * and save each type of log entry to a different file.
 *
 * @param {string} logFilePath - Path to the log file.
 */
function extractLogEntries(logFilePath) {
    // Define the log levels and corresponding output file paths
    const logLevels = {
        WARNING: 'warning_logs.txt',
        ERROR: 'error_logs.txt',
        CRITICAL: 'critical_logs.txt',
        ALERT: 'alert_logs.txt'
    };

    // Initialize an object to hold the log entries for each level
    const logEntries = {
        WARNING: [],
        ERROR: [],
        CRITICAL: [],
        ALERT: []
    };

    // Read the log file
    fs.readFile(logFilePath, 'utf8', (err, data) => {
        if (err) {
            console.error(`Error reading log file: ${err.message}`);
            return;
        }

        // Split the log file content by lines
        const lines = data.split('\n');

        // Iterate through each line to extract log entries
        lines.forEach(line => {
            for (const level in logLevels) {
                if (line.includes(level)) {
                    logEntries[level].push(line);
                    break;
                }
            }
        });

        // Write each type of log entry to a different file
        for (const level in logLevels) {
            const outputFilePath = path.join(path.dirname(logFilePath), logLevels[level]);
            fs.writeFile(outputFilePath, logEntries[level].join('\n'), 'utf8', err => {
                if (err) {
                    console.error(`Error writing ${level} log file: ${err.message}`);
                }
            });
        }
    });
}
const fs = require('fs');

describe('TestExtractLogEntries', () => {
    let logFile;

    beforeAll(() => {
        logFile = 'test_log.log';
    });

    beforeEach(() => {
        // Setup a temporary log file with sample content for testing
        const logContents = [
            "INFO: This is an informational message.\n",
            "WARNING: This is a warning message.\n",
            "ERROR: This is an error message.\n",
            "CRITICAL: This is a critical message.\n",
            "ALERT: This is an alert message.\n"
        ];
        fs.writeFileSync(logFile, logContents.join(''));
    });

    afterEach(() => {
        // Clean up after each test
        fs.unlinkSync(logFile);
        ['warning_logs.txt', 'error_logs.txt', 'critical_logs.txt', 'alert_logs.txt'].forEach(file => {
            if (fs.existsSync(file)) {
                fs.unlinkSync(file);
            }
        });
    });

    it('should handle no logs of certain levels', () => {
        fs.writeFileSync(logFile, "INFO: This is another informational message.\n");
        extractLogEntries(logFile);
        ['WARNING', 'ERROR', 'CRITICAL', 'ALERT'].forEach(level => {
            const filePath = `${level.toLowerCase()}_logs.txt`;
            expect(fs.readFileSync(filePath, 'utf8')).toBe('');
        });
    });

    it('should throw an error when the log file does not exist', () => {
        expect(() => {
            extractLogEntries('nonexistent.log');
        }).toThrow(/No log file found at the specified path/);
    });

    it('should handle an empty log file', () => {
        fs.writeFileSync(logFile, '');
        extractLogEntries(logFile);
        ['WARNING', 'ERROR', 'CRITICAL', 'ALERT'].forEach(level => {
            const filePath = `${level.toLowerCase()}_logs.txt`;
            expect(fs.readFileSync(filePath, 'utf8')).toBe('');
        });
    });

    it('should extract logs from a file with mixed content', () => {
        fs.writeFileSync(logFile, [
            "INFO: Some info.\n",
            "WARNING: Watch out!\n",
            "DEBUG: Debugging.\n",
            "ERROR: Oops!\n",
            "CRITICAL: Failed badly.\n",
            "ALERT: High alert!\n",
            "INFO: More info.\n"
        ].join(''));
        extractLogEntries(logFile);
        ['WARNING', 'ERROR', 'CRITICAL', 'ALERT'].forEach(level => {
            const filePath = `${level.toLowerCase()}_logs.txt`;
            const content = fs.readFileSync(filePath, 'utf8').trim();
            expect(content).toContain(level);
        });
    });
});
