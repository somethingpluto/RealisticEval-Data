package com.real.t179;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;

public class Adapted {
    /**
     * Copies all files and subdirectories from the source directory to the target directory.
     *
     * @param sourceDir The source directory from which files and subdirectories will be copied.
     * @param targetDir The target directory to which files and subdirectories will be copied.
     * @throws IOException If an I/O error occurs while copying files or directories.
     */
    public static void copyDirectory(File sourceDir, File targetDir) throws IOException {
        if (!sourceDir.exists()) {
            throw new IllegalArgumentException("Source directory does not exist: " + sourceDir.getAbsolutePath());
        }

        if (!sourceDir.isDirectory()) {
            throw new IllegalArgumentException("Source is not a directory: " + sourceDir.getAbsolutePath());
        }

        if (!targetDir.exists()) {
            targetDir.mkdirs();
        }

        File[] files = sourceDir.listFiles();
        if (files != null) {
            for (File file : files) {
                File targetFile = new File(targetDir, file.getName());
                if (file.isDirectory()) {
                    // Recursively copy the subdirectory
                    copyDirectory(file, targetFile);
                } else {
                    // Copy the file
                    copyFile(file.toPath(), targetFile.toPath());
                }
            }
        }
    }

    /**
     * Copies a single file from the source path to the target path.
     *
     * @param source The source file path.
     * @param target The target file path.
     * @throws IOException If an I/O error occurs during file copy.
     */
    private static void copyFile(Path source, Path target) throws IOException {
        Files.copy(source, target, StandardCopyOption.REPLACE_EXISTING);
    }

    /**
     * Main method for testing the copyDirectory function.
     */
    public static void main(String[] args) {
        try {
            File sourceDir = new File("path/to/source/directory");
            File targetDir = new File("path/to/target/directory");

            copyDirectory(sourceDir, targetDir);

            System.out.println("Directory copied successfully.");
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
