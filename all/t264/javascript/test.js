describe('extractLogEntries', () => {
    const logFilePath = 'path/to/logfile.log';
    const expectedWarningLogs = ['WARNING: This is a warning message'];
    const expectedErrorLogs = ['ERROR: This is an error message'];
    const expectedCriticalLogs = ['CRITICAL: This is a critical message'];
    const expectedAlertLogs = ['ALERT: This is an alert message'];

    beforeEach(() => {
        // Reset mocks before each test
        fs.readFileSync.mockReset();
        fs.writeFileSync.mockReset();

        // Simulate reading the log file
        fs.readFileSync.mockReturnValue(`
            WARNING: This is a warning message
            INFO: This is an info message
            ERROR: This is an error message
            CRITICAL: This is a critical message
            DEBUG: This is a debug message
            ALERT: This is an alert message
        `.trim());
    });

    it('should extract WARNING logs and save them to a separate file', () => {
        extractLogEntries(logFilePath);

        expect(fs.writeFileSync).toHaveBeenCalledWith(
            path.join(__dirname, 'warnings.log'),
            expectedWarningLogs.join('\n')
        );
    });

    it('should extract ERROR logs and save them to a separate file', () => {
        extractLogEntries(logFilePath);

        expect(fs.writeFileSync).toHaveBeenCalledWith(
            path.join(__dirname, 'errors.log'),
            expectedErrorLogs.join('\n')
        );
    });

    it('should extract CRITICAL logs and save them to a separate file', () => {
        extractLogEntries(logFilePath);

        expect(fs.writeFileSync).toHaveBeenCalledWith(
            path.join(__dirname, 'criticals.log'),
            expectedCriticalLogs.join('\n')
        );
    });

    it('should extract ALERT logs and save them to a separate file', () => {
        extractLogEntries(logFilePath);

        expect(fs.writeFileSync).toHaveBeenCalledWith(
            path.join(__dirname, 'alerts.log'),
            expectedAlertLogs.join('\n')
        );
    });
});