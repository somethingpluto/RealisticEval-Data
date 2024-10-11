describe('extractLogEntries', () => {
    it('should extract WARNING logs to a separate file', async () => {
        const mockFilePath = 'mock.log';
        const mockWarningLogs = [
            'WARNING: This is a warning message',
            'WARNING: Another warning message'
        ];

        // Mock the file reading and writing operations
        jest.spyOn(fs, 'readFileSync').mockImplementation(() => mockWarningLogs.join('\n'));
        jest.spyOn(fs, 'writeFileSync');

        await extractLogEntries(mockFilePath);

        expect(fs.writeFileSync).toHaveBeenCalledWith('WARNING_mock.log', mockWarningLogs[0] + '\n' + mockWarningLogs[1]);
    });

    it('should extract ERROR logs to a separate file', async () => {
        const mockFilePath = 'mock.log';
        const mockErrorLogs = [
            'ERROR: This is an error message',
            'ERROR: Another error message'
        ];

        // Mock the file reading and writing operations
        jest.spyOn(fs, 'readFileSync').mockImplementation(() => mockErrorLogs.join('\n'));
        jest.spyOn(fs, 'writeFileSync');

        await extractLogEntries(mockFilePath);

        expect(fs.writeFileSync).toHaveBeenCalledWith('ERROR_mock.log', mockErrorLogs[0] + '\n' + mockErrorLogs[1]);
    });

    it('should extract CRITICAL logs to a separate file', async () => {
        const mockFilePath = 'mock.log';
        const mockCriticalLogs = [
            'CRITICAL: This is a critical message',
            'CRITICAL: Another critical message'
        ];

        // Mock the file reading and writing operations
        jest.spyOn(fs, 'readFileSync').mockImplementation(() => mockCriticalLogs.join('\n'));
        jest.spyOn(fs, 'writeFileSync');

        await extractLogEntries(mockFilePath);

        expect(fs.writeFileSync).toHaveBeenCalledWith('CRITICAL_mock.log', mockCriticalLogs[0] + '\n' + mockCriticalLogs[1]);
    });

    it('should extract ALERT logs to a separate file', async () => {
        const mockFilePath = 'mock.log';
        const mockAlertLogs = [
            'ALERT: This is an alert message',
            'ALERT: Another alert message'
        ];

        // Mock the file reading and writing operations
        jest.spyOn(fs, 'readFileSync').mockImplementation(() => mockAlertLogs.join('\n'));
        jest.spyOn(fs, 'writeFileSync');

        await extractLogEntries(mockFilePath);

        expect(fs.writeFileSync).toHaveBeenCalledWith('ALERT_mock.log', mockAlertLogs[0] + '\n' + mockAlertLogs[1]);
    });
});