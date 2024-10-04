package org.real.temp;

import java.text.DecimalFormat;

public class Answer {

    // Define constants for byte sizes
    private static final long ONE_KB = 1024;
    private static final long ONE_MB = ONE_KB * 1024;
    private static final long ONE_GB = ONE_MB * 1024;
    private static final long ONE_TB = ONE_GB * 1024;

    // Create a DecimalFormat instance for formatting
    private static final DecimalFormat df = new DecimalFormat("#.##");

    /**
     * Converts a size in bytes to a human-readable string representation.
     *
     * @param sizeInBytes The size in bytes to convert.
     * @return A string representation of the size in an appropriate unit (bytes, KB, MB, GB, TB).
     */
    public static String byteCountToDisplaySize(final long sizeInBytes) {
        // Check the size and format accordingly
        if (sizeInBytes < ONE_KB) {
            return df.format(sizeInBytes) + " bytes";  // Return size in bytes
        } else if (sizeInBytes < ONE_MB) {
            return df.format((double) sizeInBytes / ONE_KB) + " KB";  // Return size in KB
        } else if (sizeInBytes < ONE_GB) {
            return df.format((double) sizeInBytes / ONE_MB) + " MB";  // Return size in MB
        } else if (sizeInBytes < ONE_TB) {
            return df.format((double) sizeInBytes / ONE_GB) + " GB";  // Return size in GB
        } else {
            return df.format((double) sizeInBytes / ONE_TB) + " TB";  // Return size in TB
        }
    }
}