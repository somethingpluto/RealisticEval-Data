package org.real.temp;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

public class Answer {

    /**
     * This method converts the encoding of a file from one encoding to another.
     *
     * @param inputFilePath      The path to the input file.
     * @param outputFilePath     The path to the output file where the converted content is saved.
     * @param originalEncoding   The original encoding of the file (default is "cp932").
     * @param targetEncoding     The target encoding to convert to (default is "UTF-16").
     * @return                   True if the conversion was successful, or if no conversion was needed; False otherwise.
     */
    public static boolean convertEncoding(String inputFilePath, String outputFilePath, String originalEncoding, String targetEncoding) {
        try (BufferedReader reader = new BufferedReader(new FileReader(inputFilePath, StandardCharsets.ISO_8859_1))) {
            StringBuilder contentBuilder = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                contentBuilder.append(line).append(System.lineSeparator());
            }
            String content = contentBuilder.toString();

            try (BufferedWriter writer = new BufferedWriter(new FileWriter(outputFilePath, StandardCharsets.UTF_16))) {
                writer.write(content);
                return true;
            }

        } catch (IOException e) {
            // Handle encoding errors if the file was already in the target encoding
            try (BufferedReader reader = new BufferedReader(new FileReader(inputFilePath, StandardCharsets.UTF_16))) {
                reader.readLine();  // Try reading to check if it's already in target encoding
                java.io.FileUtils.copyFile(new java.io.File(inputFilePath), new java.io.File(outputFilePath));  // Copy if no error occurs
                System.out.println("File already in target encoding: " + inputFilePath);
                return true;
            } catch (IOException ex) {
                System.out.println("Conversion failed due to encoding error: " + e.getMessage());
                return false;
            }
        }
    }

}