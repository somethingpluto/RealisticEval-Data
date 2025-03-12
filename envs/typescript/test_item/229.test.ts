// ... (previous code for context)

export function convertFileSize(sizeBytes: number): string {
  const units = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
  let index = 0;

  while (sizeBytes >= 1024 && index < units.length - 1) {
    sizeBytes /= 1024;
    index++;
  }

  return `${sizeBytes.toFixed(2)} ${units[index]}`;
}

// ... (rest of the code)
describe('TestFileSizeConverter', () => {
    it('should handle zero bytes', () => {
      expect(convertFileSize(0)).toBe("0B");
    });
  
    it('should handle bytes less than 1KB', () => {
      expect(convertFileSize(512)).toBe("512B");
    });
  
    it('should handle exactly 1KB', () => {
      expect(convertFileSize(1024)).toBe("1KB");
    });
  
    it('should handle 2KB', () => {
      expect(convertFileSize(2048)).toBe("2KB");
    });
  
    it('should handle exactly 1MB', () => {
      expect(convertFileSize(1048576)).toBe("1MB");
    });
  
    it('should handle 5MB', () => {
      expect(convertFileSize(5242880)).toBe("5MB");
    });
  
    it('should handle exactly 1GB', () => {
      expect(convertFileSize(1073741824)).toBe("1GB");
    });
  });
