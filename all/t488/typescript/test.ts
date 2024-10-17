describe('TestGetLocalIP', () => {
    beforeEach(() => {
        jest.resetAllMocks();
    });

    it('should find a local IP', async () => {
        // Mock the output of ipconfig for a case where a local IP is found
        mockExec.mockResolvedValueOnce({ stdout: '192.168.1.10\n' });
        const result = await getLocalIp();
        expect(result).toBe('192.168.1.10');
    });

    it('should return null when no local IP is found', async () => {
        // Mock the output of ipconfig for a case where no local IP is found
        mockExec.mockResolvedValueOnce({ stdout: '10.0.0.5\n' });
        const result = await getLocalIp();
        expect(result).toBeNull();
    });

    it('should return the first local IP when multiple IPs are found', async () => {
        // Mock the output with multiple local IPs
        mockExec.mockResolvedValueOnce({ stdout: '10.0.0.5\n192.168.1.10\n' });
        const result = await getLocalIp();
        expect(result).toBe('192.168.1.10');
    });

    it('should return null when the command fails', async () => {
        // Simulate a case where subprocess.run raises a CalledProcessError
        mockExec.mockRejectedValueOnce(new Error('Command failed'));
        const result = await getLocalIp();
        expect(result).toBeNull();
    });

    it('should return null when an unexpected error occurs', async () => {
        // Simulate an unexpected error
        mockExec.mockRejectedValueOnce(new Error('Unexpected error'));
        const result = await getLocalIp();
        expect(result).toBeNull();
    });
});