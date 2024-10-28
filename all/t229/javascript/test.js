describe('TestFileSizeConverter', () => {
  test('test_zero_bytes', () => {
      expect(convertFileSize(0)).toBe("0B");
  });

  test('test_bytes_less_than_1KB', () => {
      expect(convertFileSize(512)).toBe("512B");
  });

  test('test_exactly_1KB', () => {
      expect(convertFileSize(1024)).toBe("1KB");
  });

  test('test_2KB', () => {
      expect(convertFileSize(2048)).toBe("2KB");
  });

  test('test_exactly_1MB', () => {
      expect(convertFileSize(1048576)).toBe("1MB");
  });

  test('test_5MB', () => {
      expect(convertFileSize(5242880)).toBe("5MB");
  });

  test('test_exactly_1GB', () => {
      expect(convertFileSize(1073741824)).toBe("1GB");
  });
});