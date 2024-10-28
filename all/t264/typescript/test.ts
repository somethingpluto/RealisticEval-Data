describe('TestExtractLogEntries', () => {
    beforeEach(() => {
        // Setup a temporary log file with sample content for testing
        const logFileContents = [
            "INFO: This is an informational message.\n",
            "WARNING: This is a warning message.\n",
            "ERROR: This is an error message.\n",
            "CRITICAL: This is a critical message.\n",
            "ALERT: This is an alert message.\n"
        ];
        const logFilePath = 'test_log.log';
        fs.writeFileSync(logFilePath, logFileContents.join(''));
    });

    afterEach(() => {
        // Clean up after each test
        ['warning_logs.txt', 'error_logs.txt', 'critical_logs.txt', 'alert_logs.txt'].forEach(file => {
            if (fs.existsSync(file)) {
                fs.unlinkSync(file);
            }
        });
        if (fs.existsSync('test_log.log')) {
            fs.unlinkSync('test_log.log');
        }
    });

    it('should handle no logs of certain levels', () => {
        const logFilePath = 'test_log.log';
        fs.writeFileSync(logFilePath, "INFO: This is another informational message.\n");
        extractLogEntries(logFilePath);

        ['WARNING', 'ERROR', 'CRITICAL', 'ALERT'].forEach(level => {
            const filePath = `${level.toLowerCase()}_logs.txt`;
            expect(fs.existsSync(filePath)).toBe(true);
            const content = fs.readFileSync(filePath, 'utf-8').trim();
            expect(content).toBe('');
        });
    });

    it('should throw an error when the log file does not exist', () => {
        expect(() => {
            extractLogEntries('nonexistent.log');
        }).toThrow(/No log file found at the specified path: nonexistent\.log/);
    });

    it('should handle an empty log file', () => {
        const logFilePath = 'test_log.log';
        fs.writeFileSync(logFilePath, "");
        extractLogEntries(logFilePath);

        ['WARNING', 'ERROR', 'CRITICAL', 'ALERT'].forEach(level => {
            const filePath = `${level.toLowerCase()}_logs.txt`;
            expect(fs.existsSync(filePath)).toBe(true);
            const content = fs.readFileSync(filePath, 'utf-8').trim();
            expect(content).toBe('');
        });
    });

    it('should extract logs from a file with mixed content', () => {
        const logFilePath = 'test_log.log';
        fs.writeFileSync(logFilePath, [
            "INFO: Some info.\n",
            "WARNING: Watch out!\n",
            "DEBUG: Debugging.\n",
            "ERROR: Oops!\n",
            "CRITICAL: Failed badly.\n",
            "ALERT: High alert!\n",
            "INFO: More info.\n"
        ].join(''));

        extractLogEntries(logFilePath);

        ['WARNING', 'ERROR', 'CRITICAL', 'ALERT'].forEach(level => {
            const filePath = `${level.toLowerCase()}_logs.txt`;
            expect(fs.existsSync(filePath)).toBe(true);
            const content = fs.readFileSync(filePath, 'utf-8').trim();
            expect(content).toContain(level);
        });
    });
});