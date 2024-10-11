function convertFileSize(sizeBytes: number): string {
    /**
     * Converts a file size in bytes to a human-readable format.
     * For example:
     *      input: 2120
     *      output: 2KB
     * Args:
     *      sizeBytes (number): The size in bytes to be converted.
     *
     * Returns:
     *      string: The converted size in a human-readable format (e.g., "2KB", "1MB").
     */

    const units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB'];
    let i = Math.floor(Math.log2(sizeBytes) / 10);
    return `${(sizeBytes / Math.pow(1024, i)).toFixed(2)}${units[i]}`;
}