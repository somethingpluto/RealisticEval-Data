describe('getLocalIP', () => {
    it('should return the local IP address when the specified interface exists', async () => {
      // Mocking the subprocess module
      const mockExec = jest.fn().mockResolvedValue({ stdout: '192.168.1.1\n' });
      jest.mock('child_process', () => ({
        exec: mockExec,
      }));
  
      const { getLocalIP } = await import('./yourModulePath'); // Replace with actual path
  
      const result = await getLocalIP('wlan0');
      expect(result).toBe('192.168.1.1');
  
      expect(mockExec).toHaveBeenCalledWith(
        `ip addr show ${interface} | grep -oP '(?<=inet\s)\d+(\.\d+){3}'`,
        expect.any(Function)
      );
    });
  
    it('should return a message indicating no IP was found if the specified interface does not exist', async () => {
      // Mocking the subprocess module
      const mockExec = jest.fn().mockRejectedValue(new Error('No such device'));
      jest.mock('child_process', () => ({
        exec: mockExec,
      }));
  
      const { getLocalIP } = await import('./yourModulePath'); // Replace with actual path
  
      try {
        await getLocalIP('nonexistent_interface');
      } catch (error) {
        expect(error.message).toBe('No such device');
      }
  
      expect(mockExec).toHaveBeenCalledWith(
        `ip addr show nonexistent_interface | grep -oP '(?<=inet\s)\d+(\.\d+){3}'`,
        expect.any(Function)
      );
    });
  });