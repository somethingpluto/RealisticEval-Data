const { exec } = require('child_process');
const { expect } = require('@jest/globals');

// Mock the `exec` function to simulate subprocess behavior
jest.mock('child_process', () => ({
  exec: jest.fn(),
}));
describe('TestGetLocalIp', () => {
  beforeEach(() => {
    // Sample IP command output for a wlan0 interface
    const sampleOutput = `3: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    inet 192.168.1.100/24 brd 192.168.1.255 scope global dynamic wlan0
       valid_lft 86394sec preferred_lft 86394sec`;

    // Mock the exec function to return a successful output
    exec.mockImplementationOnce((command, callback) => {
      callback(null, sampleOutput, '');
    });

    // Mock the exec function for a different interface
    exec.mockImplementationOnce((command, callback) => {
      callback(null, `3: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500
      inet 10.0.0.1/24`, '');
    });

    // Mock the exec function to simulate a subprocess failure
    exec.mockImplementationOnce((command, callback) => {
      callback(new Error('Failed to execute command'), '', '');
    });
  });

  it('should successfully retrieve the IP address', async () => {
    const ip = await getLocalIP('wlan0');
    expect(ip).toBe('192.168.1.100');
  });

  it('should handle command failure', async () => {
    try {
      await getLocalIP('wlan0');
    } catch (error) {
      expect(error.message).toContain('Failed to retrieve IP address');
    }
  });

  it('should retrieve the IP address for a different interface', async () => {
    const ip = await getLocalIP('eth0');
    expect(ip).toBe('10.0.0.1');
  });
});