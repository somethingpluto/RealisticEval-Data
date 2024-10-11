describe('IP Address Validation', () => {
  test('should return true for a valid IPv4 address', () => {
    expect(isCompliantIp('192.168.1.1')).toBe(true);
  });

  test('should return false for an invalid IPv4 address', () => {
    expect(isCompliantIp('256.256.256.256')).toBe(false);
  });

  test('should return false for an IPv4 address with non-numeric characters', () => {
    expect(isCompliantIp('192.168.1.a')).toBe(false);
  });

  test('should return false for an IPv4 address with too many octets', () => {
    expect(isCompliantIp('192.168.1.1.1')).toBe(false);
  });

  test('should return false for an IPv4 address with an empty octet', () => {
    expect(isCompliantIp('192.168..1')).toBe(false);
  });

  // Add more tests as needed
});