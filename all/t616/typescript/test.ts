describe('byteCountToDisplaySize', () => {
    test('should return "0 bytes" for 0 bytes', () => {
        const inputSize = 0;
        const expected = "0 bytes";
        expect(byteCountToDisplaySize(inputSize)).toBe(expected);
    });

    test('should return "500 bytes" for 500 bytes', () => {
        const inputSize = 500;
        const expected = "500 bytes";
        expect(byteCountToDisplaySize(inputSize)).toBe(expected);
    });

    test('should return "1 KB" for exactly 1KB', () => {
        const inputSize = 1024;
        const result = byteCountToDisplaySize(inputSize);
        expect(result).toBe("1 KB");
        expect(result).toBe("1.00 KB");
    });

    test('should return "4.88 KB" for 5000 bytes', () => {
        const inputSize = 5000;
        const expected = "4.88 KB";
        expect(byteCountToDisplaySize(inputSize)).toBe(expected);
    });

    test('should return "1 MB" for exactly 1MB', () => {
        const inputSize = 1048576; // 1024 * 1024
        const result = byteCountToDisplaySize(inputSize);
        expect(result).toBe("1 MB");
        expect(result).toBe("1.00 MB");
    });
});