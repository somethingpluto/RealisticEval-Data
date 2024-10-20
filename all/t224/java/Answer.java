package org.real.temp;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class Answer {

    /**
     * Empties all files and subdirectories in the specified directory, but keeps the directory itself.
     *
     * @param directoryPath Path to the directory whose contents are to be emptied.
     * @throws IllegalArgumentException If the specified path does not exist or is not a directory.
     */
    public static void emptyDirectory(String directoryPath) throws Exception {
        // Check if the path exists and is a directory
        Path path = Paths.get(directoryPath);
        if (!Files.exists(path)) {
            throw new IllegalArgumentException("The specified directory does not exist.");
        }
        if (!Files.isDirectory(path)) {
            throw new IllegalArgumentException("The specified path is not a directory.");
        }

        // Iterate over all items in the directory
        File dir = new File(directoryPath);
        File[] items = dir.listFiles();
        if (items != null) {
            for (File item : items) {
                // Check if the item is a file or directory and delete accordingly
                if (item.isFile() || item.isDirectory()) {
                    if (item.isFile() || item.isSymbolicLink()) {
                        Files.delete(item.toPath());  // Remove the file or link
                    } else if (item.isDirectory()) {
                        deleteDirectoryRecursively(item);  // Remove the directory and all its contents
                    }
                }
            }
        }
    }

    private static void deleteDirectoryRecursively(File directory) throws Exception {
        File[] files = directory.listFiles();
        if (files != null) {
            for (File file : files) {
                if (file.isDirectory()) {
                    deleteDirectoryRecursively(file);
                } else {
                    Files.delete(file.toPath());
                }
            }
        }
        Files.delete(directory.toPath());
    }

    public static void main(String[] args) {
        try {
            emptyDirectory("/path/to/directory");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}