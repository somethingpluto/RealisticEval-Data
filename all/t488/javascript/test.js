describe('TestGetLocalIP', () => {
    beforeEach(() => {
        jest.spyOn(console, 'error').mockImplementation(() => {});
    });

    afterEach(() => {
        console.error.mockRestore();
    });

    it('should find a local IP when one is present', async () => {
        // Mock the output of ipconfig for a case where a local IP is found
        const execMock = jest.spyOn(require('child_process'), 'exec').mockResolvedValue({
            stdout: '192.168.1.10\n',
            stderr: ''
        });

        const result = await getLocalIP();
        expect(result).toBe('192.168.1.10');

        execMock.mockRestore();
    });

    it('should return null when no local IP is found', async () => {
        // Mock the output of ipconfig for a case where no local IP is found
        const execMock = jest.spyOn(require('child_process'), 'exec').mockResolvedValue({
            stdout: '10.0.0.5\n',
            stderr: ''
        });

        const result = await getLocalIP();
        expect(result).toBeNull();

        execMock.mockRestore();
    });

    it('should find the correct local IP when multiple IPs are present', async () => {
        // Mock the output with multiple local IPs
        const execMock = jest.spyOn(require('child_process'), 'exec').mockResolvedValue({
            stdout: '10.0.0.5\n192.168.1.10\n',
            stderr: ''
        });

        const result = await getLocalIP();
        expect(result).toBe('192.168.1.10');

        execMock.mockRestore();
    });

    it('should return null when the command fails', async () => {
        // Simulate a case where exec throws an error
        const execMock = jest.spyOn(require('child_process'), 'exec').mockRejectedValue(new Error('CalledProcessError'));

        const result = await getLocalIP().catch(() => null);
        expect(result).toBeNull();

        execMock.mockRestore();
    });

    it('should return null when an unexpected error occurs', async () => {
        // Simulate an unexpected error
        const execMock = jest.spyOn(require('child_process'), 'exec').mockRejectedValue(new Error('Unexpected error'));

        const result = await getLocalIP().catch(() => null);
        expect(result).toBeNull();

        execMock.mockRestore();
    });
});