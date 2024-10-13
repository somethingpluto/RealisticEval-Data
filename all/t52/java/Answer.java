package org.real.temp;

import java.io.File;
import java.nio.file.Path;
import java.nio.file.Paths;

public class Answer {

    /**
     * Renames a Windows file path by replacing colons in the filename with underscores.
     *
     * @param path The original file path as a String.
     * @return The modified file path with colons in the filename replaced by underscores as a String.
     */
    public static String renameFilePath(String path) {
        // Convert the string path to a Path object
        Path filePath = Paths.get(path);

        // Get the parent directory and the filename
        Path parentDirectory = filePath.getParent();
        String filename = filePath.getFileName().toString();

        // Replace colons in the filename with underscores
        String sanitizedFilename = filename.replace(":", "_");

        // Reconstruct the full path with the sanitized filename
        Path newPath = parentDirectory.resolve(sanitizedFilename);

        // Convert the Path object back to a string
        return newPath.toString();
    }

    // Example usage
    public static void main(String[] args) {
        String originalPath = "C:\\Users\\Example\\Documents\\file:name.txt";
        String newPath = renameFilePath(originalPath);
        System.out.println("Original Path: " + originalPath);
        System.out.println("New Path: " + newPath);
    }
}