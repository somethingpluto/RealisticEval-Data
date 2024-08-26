package com.real.t182;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class Adapted {

    /**
     * Copies the contents of the source file to the destination file using a buffered stream
     * and measures the time it takes to complete the operation.
     *
     * @param sourceFilePath      The path to the source file.
     * @param destinationFilePath The path to the destination file.
     * @return The time taken to copy the file in milliseconds.
     * @throws IOException If an I/O error occurs during the copy operation.
     */
    public static long copyFileWithBufferedStream(String sourceFilePath, String destinationFilePath) throws IOException {
        long startTime = System.currentTimeMillis();

        try (BufferedInputStream bis = new BufferedInputStream(new FileInputStream(sourceFilePath));
             BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream(destinationFilePath))) {

            byte[] buffer = new byte[8192];
            int bytesRead;

            while ((bytesRead = bis.read(buffer)) != -1) {
                bos.write(buffer, 0, bytesRead);
            }
        }

        long endTime = System.currentTimeMillis();
        return endTime - startTime;
    }

    /**
     * Main method for testing the copyFileWithBufferedStream function.
     */
    public static void main(String[] args) {
        try {
            String sourceFilePath = "source.txt";
            String destinationFilePath = "destination.txt";
            long timeTaken = copyFileWithBufferedStream(sourceFilePath, destinationFilePath);
            System.out.println("Time taken to copy file: " + timeTaken + " ms.");
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
