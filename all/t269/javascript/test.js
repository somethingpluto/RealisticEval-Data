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