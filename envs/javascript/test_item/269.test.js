/**
 * Check whether the IP address is a legal IP address.
 *
 * @param {string} ip - The IP address in string format.
 * @returns {boolean} - True if the IP is compliant, False otherwise.
 */
function isCompliantIP(ip) {
    // Regular expression to match a valid IPv4 address
    const ipv4Pattern = /^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;
    
    // Check if the IP address matches the pattern
    return ipv4Pattern.test(ip);
}
describe('TestIsCompliantIP', () => {
  test('test_private_ip', () => {
      expect(isCompliantIP('192.168.1.1')).toBe(true);
  });

  test('test_public_ip', () => {
      expect(isCompliantIP('8.8.8.8')).toBe(true);
  });

  test('test_invalid_ip', () => {
      expect(isCompliantIP('999.999.999.999')).toBe(false);
  });
});
