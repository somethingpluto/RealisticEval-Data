package org.real.temp;

import java.util.regex.Pattern;

public class Answer {

    /**
     * Remove illegal characters from Windows file path string.
     *
     * @param filename The original filename string to be sanitized.
     * @return A sanitized string that is safe to use as a Windows filename.
     */
    public static String sanitizeFilename(String filename) {
        // Define the illegal characters for Windows filenames
        String illegalCharsPattern = "[<>:\"/\\\\|?*\\x00-\\x1F]";

        // Replace illegal characters with an underscore
        String sanitized = filename.replaceAll(illegalCharsPattern, "_");

        // Optionally, you can also limit the length of the filename
        // Windows has a maximum path length of 260 characters
        int maxLength = 255;
        if (sanitized.length() > maxLength) {
            sanitized = sanitized.substring(0, maxLength);
        }

        return sanitized;
    }

    public static void main(String[] args) {
        // Example usage
        String originalFilename = "example<file>.txt";
        String sanitizedFilename = sanitizeFilename(originalFilename);
        System.out.println("Original: " + originalFilename);
        System.out.println("Sanitized: " + sanitizedFilename);
    }
}