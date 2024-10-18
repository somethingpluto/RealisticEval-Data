package org.real.temp;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Answer {

    /**
     * Writes a line to a text file only if the line with the same content does not already exist.
     *
     * @param filename    The name of the file to write to.
     * @param lineContent The content of the line to write.
     */
    public static void writeUniqueLineToFile(String filename, String lineContent) {
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String currentLine;
            while ((currentLine = reader.readLine()) != null) {
                if (currentLine.equals(lineContent)) {
                    System.out.println("Line '" + lineContent + "' already exists in '" + filename + "'. Not writing again.");
                    return;
                }
            }
        } catch (IOException e) {
            System.err.println("Error reading the file: " + e.getMessage());
        }

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filename, true))) {
            writer.write(lineContent);
            writer.newLine();
            System.out.println("Line '" + lineContent + "' successfully written to '" + filename + "'.");
        } catch (IOException e) {
            System.err.println("Error writing to the file: " + e.getMessage());
        }
    }

}