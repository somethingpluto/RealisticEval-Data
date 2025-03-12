/**
 * Formats a given number of bytes into a human-readable string representation,
 * using either the SI (decimal) or binary (accurate) size notation.
 *
 * @param {number} bytes - The number of bytes to format.
 * @param {Object} options - Optional settings to customize the output.
 * @param {number} [options.decimals=0] - Number of decimal places to include in the output.
 * @param {"accurate" | "normal"} [options.sizeType="normal"] -
 *        Specifies whether to use binary ("accurate") or decimal ("normal") units.
 *        "accurate" uses units like KiB, MiB (base 1024).
 *        "normal" uses units like KB, MB (base 1000).
 * @returns {string} A string representation of the byte size in a human-readable format.
 */
function formatBytes(bytes, options = {}) {
    const { decimals = 0, sizeType = "normal" } = options;
    const base = sizeType === "accurate" ? 1024 : 1000;
    const units = sizeType === "accurate" ? ["B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB"] : ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"];

    if (bytes === 0) return `0 ${units[0]}`;

    const exponent = Math.floor(Math.log(bytes) / Math.log(base));
    const value = bytes / Math.pow(base, exponent);
    const unit = units[exponent];

    return `${value.toFixed(decimals)} ${unit}`;
}
describe('formatBytes', () => {
    test('should return "0 Byte" for 0 bytes', () => {
        const result = formatBytes(0);
        expect(['0 B', '0 Byte']).toContain(result);
    });

    test('should return "2.0 KB" for 2048 bytes', () => {
        const result = formatBytes(2048);
        expect(['2 KB', '2.0 KB']).toContain(result);
    });

    test('should return "2.0 KiB" for 2048 bytes with sizeType "accurate"', () => {
        const result = formatBytes(2048, { sizeType: "accurate" });
        expect(['2 KiB', '2.0 KiB']).toContain(result);
    });

    test('should return "5.0 MB" for 5242880 bytes', () => {
        const result = formatBytes(5242880);
        expect(['5 MB', '5.0 MB']).toContain(result);
    });

    test('should return "5.00 MiB" for 5242880 bytes with 2 decimal places and sizeType "accurate"', () => {
        const result = formatBytes(5242880, { decimals: 2, sizeType: "accurate" });
        expect(result).toBe('5.00 MiB');
    });
});
