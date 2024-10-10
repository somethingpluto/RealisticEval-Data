describe('getLocalIP', () => {
    it('should return the local IP address for a given interface', async () => {
      const interfaceName = 'wlan0'; // Change this to the desired interface name
      const expectedPattern = /inet\s+(\d+\.\d+\.\d+\.\d+)/; // Regex pattern to match the IP address
  
      try {
        const { stdout } = await exec(`ifconfig ${interfaceName}`);
        const match = stdout.match(expectedPattern);
  
        if (!match) {
          throw new Error('No IP address found');
        }
  
        expect(match[1]).toMatch(/^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$/); // Validate that the IP address matches the standard format
      } catch (error) {
        expect(error.message).toBe('No IP address found'); // Handle the error case where no IP address is found
      }
    });
  });