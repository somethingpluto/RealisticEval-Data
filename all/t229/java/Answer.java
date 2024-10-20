package org.real.temp;

public class Answer {

    /**
     * Converts the file size from bytes to a human-readable format.
     * 
     * @param sizeBytes The size in bytes.
     * @return A string representing the formatted size with the appropriate unit.
     */
    public static String convertFileSize(long sizeBytes) {
        // Define the size units
        String[] units = {"B", "KB", "MB", "GB", "TB"};

        // Handle the case when size is 0 bytes
        if (sizeBytes == 0) {
            return "0B";
        }

        // Calculate the appropriate unit
        int index = 0;
        while (sizeBytes >= 1024 && index < units.length - 1) {
            sizeBytes /= 1024;
            index++;
        }

        // Return the formatted size with the appropriate unit
        return String.format("%d%s", sizeBytes, units[index]);
    }

    public static void main(String[] args) {
        // Example usage
        System.out.println(convertFileSize(1550)); // Output: 1KB
        System.out.println(convertFileSize(1049026)); // Output: 1MB
    }
}