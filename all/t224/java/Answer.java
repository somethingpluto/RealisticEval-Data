package org.real.temp;

import java.io.File;
import java.io.IOException;

public class Answer {

    /**
     * Empty all files and subdirectories in the specified directory.
     *
     * @param directoryPath Path to the directory whose contents are to be emptied.
     * @throws IOException If an I/O error occurs while deleting files or directories.
     */
    public static void emptyDirectory(String directoryPath) throws IOException {
        File directory = new File(directoryPath);

        if (!directory.exists() || !directory.isDirectory()) {
            throw new IllegalArgumentException("The specified path does not exist or is not a directory.");
        }

        File[] files = directory.listFiles();
        if (files != null) {
            for (File file : files) {
                if (file.isDirectory()) {
                    emptyDirectory(file.getAbsolutePath()); // Recursively delete subdirectories
                } else {
                    if (!file.delete()) {
                        throw new IOException("Failed to delete file: " + file.getAbsolutePath());
                    }
                }
            }
        }
    }

    public static void main(String[] args) {
        try {
            emptyDirectory("/path/to/directory"); // Replace with your directory path
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}