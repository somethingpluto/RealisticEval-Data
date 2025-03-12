const { exec } = require('child_process');

/**
 * Retrieve the local IP address of the specified network interface on Windows.
 *
 * @param {string} [interface='Wi-Fi'] - The name of the network interface to check (default is 'Wi-Fi').
 * @returns {Promise<string | null>} - A promise that resolves to the local IP address if found, otherwise null.
 */
async function getLocalIP(interface = 'Wi-Fi') {
    return new Promise((resolve, reject) => {
        exec(`ipconfig | findstr /R /C:"${interface}"`, (error, stdout, stderr) => {
            if (error) {
                reject(error);
                return;
            }

            if (stderr) {
                reject(new Error(stderr));
                return;
            }

            const lines = stdout.split('\n');
            for (const line of lines) {
                const match = line.match(/IPv4 Address[^:]*:\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/);
                if (match) {
                    resolve(match[1]);
                    return;
                }
            }

            resolve(null);
        });
    });
}
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
