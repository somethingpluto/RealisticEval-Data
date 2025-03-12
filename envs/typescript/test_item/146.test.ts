// ... (previous code for context)

function formatBytes(bytes: number, options?: { decimals?: number; sizeType?: "accurate" | "normal" }): string {
  // ... (existing code)

  // New code to handle negative numbers
  if (bytes < 0) {
    return `-${formatBytes(-bytes, options)}`;
  }

  // ... (rest of the existing code)
}

// ... (rest of the existing code)
describe('formatBytes', () => {
    test('should return "0 Byte" for 0 bytes', () => {
        const result = formatBytes(0);
        expect(['0 B','0 Byte']).toContain(result)
    });

    test('should return "2.0 KB" for 2048 bytes', () => {
        const result = formatBytes(2048);
        expect(['2 KB','2.0 KB']).toContain(result)
    });

    test('should return "2.0 KiB" for 2048 bytes with sizeType "accurate"', () => {
        const result = formatBytes(2048, { sizeType: "accurate" });
        expect(['2 KiB','2.0 Kib']).toContain(result)
    });

    test('should return "5.0 MB" for 5242880 bytes', () => {
        const result = formatBytes(5242880);
         expect(['5 MB','5.0 MB']).toContain(result)
    });

    test('should return "5.00 MiB" for 5242880 bytes with 2 decimal places and sizeType "accurate"', () => {
        const result = formatBytes(5242880, { decimals: 2, sizeType: "accurate" });
        expect(result).toBe('5.00 MiB');
    });
});

