/**
 * Converts a file size in bytes to a human-readable format.
 * 
 * @param {number} sizeBytes - The size in bytes to be converted.
 * @returns {string} The converted size in a human-readable format (e.g., "2KB", "1MB").
 */
function convertFileSize(sizeBytes) {
    const units = ["B", "KB", "MB", "GB", "TB"];
    let size = sizeBytes;
    let unitIndex = 0;

    while (size >= 1024 && unitIndex < units.length - 1) {
        size /= 1024;
        unitIndex++;
    }

    return `${Math.round(size)}${units[unitIndex]}`;
}
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
