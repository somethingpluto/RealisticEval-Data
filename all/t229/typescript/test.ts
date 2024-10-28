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