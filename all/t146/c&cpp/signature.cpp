/**
 * Formats a given number of bytes into a human-readable string representation,
 * using either the SI (decimal) or binary (accurate) size notation.
 *
 * @param bytes - The number of bytes to format.
 * @param decimals - Optional number of decimal places to include in the output.
 * @param sizeType - Optional specification of whether to use binary ("accurate") 
 *                   or decimal ("normal") units.
 *                   "accurate" uses units like KiB, MiB (base 1024).
 *                   "normal" uses units like KB, MB (base 1000).
 * @returns A string representation of the byte size in a human-readable format.
 */
std::string formatBytes()