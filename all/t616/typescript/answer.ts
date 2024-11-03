/**
 * Converts a size in bytes to a human-readable string representation.
 *
 * @param sizeInBytes - The size in bytes to convert.
 * @returns A string representation of the size in an appropriate unit (bytes, KB, MB, GB, TB).
 */
function byteCountToDisplaySize(sizeInBytes: number): string {
    // Define constants for byte conversions
    const ONE_KB = 1024;
    const ONE_MB = ONE_KB * 1024;
    const ONE_GB = ONE_MB * 1024;
    const ONE_TB = ONE_GB * 1024;

    if (sizeInBytes < ONE_KB) {
        return `${sizeInBytes} bytes`;  // Return size in bytes without decimal
    } else if (sizeInBytes < ONE_MB) {
        return `${(sizeInBytes / ONE_KB).toFixed(2)} KB`;  // Return size in KB
    } else if (sizeInBytes < ONE_GB) {
        return `${(sizeInBytes / ONE_MB).toFixed(2)} MB`;  // Return size in MB
    } else if (sizeInBytes < ONE_TB) {
        return `${(sizeInBytes / ONE_GB).toFixed(2)} GB`;  // Return size in GB
    } else {
        return `${(sizeInBytes / ONE_TB).toFixed(2)} TB`;  // Return size in TB
    }
}