describe('TestGetLocalIp', () => {
  beforeEach(() => {
      // Sample IP command output for a wlan0 interface
      this.sampleOutput = `
          3: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
          inet 192.168.1.100/24 brd 192.168.1.255 scope global dynamic wlan0
          valid_lft 86394sec preferred_lft 86394sec
      `;
  });

  describe('testSuccessfulIpRetrieval', () => {
      it('should retrieve the correct IP address', async () => {
          // Mock the child_process.exec function
          jest.spyOn(child_process, 'exec').mockImplementation((command, callback) => {
              callback(null, this.sampleOutput, '');
          });

          const ip = await getLocalIP('wlan0');
          expect(ip).toBe('192.168.1.100');
      });
  });

  describe('testCommandFailure', () => {
      it('should throw an error when the command fails', async () => {
          // Mock the child_process.exec function to simulate a failure
          jest.spyOn(child_process, 'exec').mockImplementation((command, callback) => {
              callback(new Error('Command failed'), '', '');
          });

          await expect(getLocalIP('wlan0')).rejects.toThrow('Failed to retrieve IP address: Command failed');
      });
  });

  describe('testDifferentInterface', () => {
      it('should retrieve the correct IP address for a different interface', async () => {
          // Sample IP command output for a different interface
          const sampleOutputEth0 = `
              3: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500
              inet 10.0.0.1/24
          `;

          // Mock the child_process.exec function
          jest.spyOn(child_process, 'exec').mockImplementation((command, callback) => {
              callback(null, sampleOutputEth0, '');
          });

          const ip = await getLocalIP('eth0');
          expect(ip).toBe('10.0.0.1');
      });
  });
});