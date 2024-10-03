package org.real.temp;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

public class Answer {
    /**
     * Reads the content of the file specified by the file path and returns it as a byte array.
     *
     * @param filePath The path to the file that needs to be read.
     * @return A byte array containing the content of the file.
     * @throws IOException If an I/O error occurs while reading the file.
     */
    public static byte[] readFileToByteArray(String filePath) throws IOException {
        File file = new File(filePath);
        if (!file.exists()) {
            throw new IllegalArgumentException("File does not exist: " + filePath);
        }

        try (FileInputStream fis = new FileInputStream(file)) {
            byte[] data = new byte[(int) file.length()];
            int bytesRead = fis.read(data);
            if (bytesRead != data.length) {
                throw new IOException("Could not completely read the file: " + filePath);
            }
            return data;
        }
    }

    /**
     * Main method for testing the readFileToByteArray function.
     */
    public static void main(String[] args) {
        try {
            String filePath = "example.txt";
            byte[] content = readFileToByteArray(filePath);
            System.out.println("File content as byte array: " + content.length + " bytes.");
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
