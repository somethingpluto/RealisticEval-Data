describe('convertFileSize', () => {
    it('should convert 2120 bytes to 2KB', () => {
      expect(convertFileSize(2120)).toBe('2KB');
    });
  
    it('should convert 1048576 bytes to 1MB', () => {
      expect(convertFileSize(1048576)).toBe('1MB');
    });
  
    it('should convert 1073741824 bytes to 1GB', () => {
      expect(convertFileSize(1073741824)).toBe('1GB');
    });
  
    it('should convert 1 byte to 1B', () => {
      expect(convertFileSize(1)).toBe('1B');
    });
  });