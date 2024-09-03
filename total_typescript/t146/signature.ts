/**
 * Formats a given number of bytes into a human-readable string representation,
 * using either the SI (decimal) or binary (accurate) size notation.
 *
 * @param {number} bytes - The number of bytes to format.
 * @param {Object} options - Optional settings to customize the output.
 * @param {number} [options.decimals=0] - Number of decimal places to include in the result.
 * @param {"accurate" | "normal"} [options.sizeType="normal"] -
 *        Specifies whether to use binary ("accurate") or decimal ("normal") units.
 *        "accurate" uses units like KiB, MiB (base 1024).
 *        "normal" uses units like KB, MB (base 1000).
 * @returns {string} A string representation of the byte size in a human-readable format.
 */
function formatBytes(
    bytes: number,
    options?: {
      decimals?: number;
      sizeType?: "accurate" | "normal";
    }
): string;
