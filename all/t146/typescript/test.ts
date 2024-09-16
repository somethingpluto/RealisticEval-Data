describe('formatBytes', () => {
    test('should return "0 Byte" for 0 bytes', () => {
        const result = formatBytes(0);
        expect(result).toBe('0 Byte');
    });

    test('should return "2.0 KB" for 2048 bytes', () => {
        const result = formatBytes(2048);
        expect(result).toBe('2.0 KB');
    });

    test('should return "2.0 KiB" for 2048 bytes with sizeType "accurate"', () => {
        const result = formatBytes(2048, { sizeType: "accurate" });
        expect(result).toBe('2.0 KiB');
    });

    test('should return "5.0 MB" for 5242880 bytes', () => {
        const result = formatBytes(5242880);
        expect(result).toBe('5.0 MB');
    });

    test('should return "5.00 MiB" for 5242880 bytes with 2 decimal places and sizeType "accurate"', () => {
        const result = formatBytes(5242880, { decimals: 2, sizeType: "accurate" });
        expect(result).toBe('5.00 MiB');
    });
});