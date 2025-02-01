const { exec } = require('child_process');

/**
 * Retrieve the local IP address of the specified network interface on Windows.
 *
 * @param {string} [interface='Wi-Fi'] - The name of the network interface to check (default is 'Wi-Fi').
 * @returns {Promise<string | null>} - A promise that resolves to the local IP address if found, otherwise null.
 */
async function getLocalIP(interface = 'Wi-Fi') {
  return new Promise((resolve, reject) => {
    // Construct the command to get the IP address of the specified network interface
    const command = `ipconfig | findstr /C:"${interface}" /C:"IPv4 Address"`;

    // Execute the command
    exec(command, (error, stdout, stderr) => {
      if (error) {
        reject(error);
        return;
      }

      // Parse the output to find the IP address
      const lines = stdout.split('\n');
      const ipAddressLine = lines.find(line => line.includes('IPv4 Address'));
      if (ipAddressLine) {
        // Extract the IP address from the line
        const ipAddress = ipAddressLine.split(': ')[1].trim();
        resolve(ipAddress);
      } else {
        resolve(null);
      }
    });
  });
}

// Example usage:
// getLocalIP('Wi-Fi').then(ip => console.log(ip)).catch(err => console.error(err));
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
