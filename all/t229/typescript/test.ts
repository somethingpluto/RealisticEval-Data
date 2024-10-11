describe('convertFileSize', () => {
    it('should convert 2120 bytes to 2KB', () => {
        expect(convertFileSize(2120)).toBe('2.05KB');
    });

    it('should convert 1024 bytes to 1KB', () => {
        expect(convertFileSize(1024)).toBe('1.00KB');
    });

    it('should convert 1048576 bytes to 1MB', () => {
        expect(convertFileSize(1048576)).toBe('1.00MB');
    });

    it('should convert 1073741824 bytes to 1GB', () => {
        expect(convertFileSize(1073741824)).toBe('1.00GB');
    });

    it('should convert 1099511627776 bytes to 1TB', () => {
        expect(convertFileSize(1099511627776)).toBe('1.00TB');
    });

    it('should handle 0 bytes correctly', () => {
        expect(convertFileSize(0)).toBe('0B');
    });
});