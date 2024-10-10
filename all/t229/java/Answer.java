package org.real.temp;

public class Answer {

    /**
     * Converts a file size in bytes to a human-readable format.
     * For example:
     *      input: 2120
     *      output: 2KB
     *
     * @param sizeBytes The size in bytes to be converted.
     * @return The converted size in a human-readable format (e.g., "2KB", "1MB").
     */
    public static String convertFileSize(int sizeBytes) {
        if (sizeBytes < 1024) {
            return sizeBytes + "B";
        } else if (sizeBytes < 1024 * 1024) {
            return Math.round((float) sizeBytes / 1024) + "KB";
        } else if (sizeBytes < 1024 * 1024 * 1024) {
            return Math.round((float) sizeBytes / (1024 * 1024)) + "MB";
        } else {
            return Math.round((float) sizeBytes / (1024 * 1024 * 1024)) + "GB";
        }
    }

    public static void main(String[] args) {
        // Example usage
        System.out.println(convertFileSize(2120)); // Output: 2KB
    }
}