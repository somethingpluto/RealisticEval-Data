/**
 * Converts a file size in bytes to a human-readable format.
 * For example:
 *     input: 2120
 *     output: 2KB
 * 
 * @param {number} sizeBytes - The size in bytes to be converted.
 * @returns {string} The converted size in a human-readable format (e.g., "2KB", "1MB").
 */
function convertFileSize(sizeBytes) {
    const units = ['B', 'KB', 'MB', 'GB', 'TB'];
    let unitIndex = 0;

    while (sizeBytes >= 1024 && unitIndex < units.length - 1) {
        sizeBytes /= 1024;
        unitIndex++;
    }

    return `${sizeBytes.toFixed(2)}${units[unitIndex]}`;
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
