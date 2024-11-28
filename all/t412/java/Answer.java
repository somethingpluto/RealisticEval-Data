package org.real.temp;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Answer {

    public static void formatText(String inputFilePath, String outputFilePath) {
        try (BufferedReader reader = new BufferedReader(new FileReader(inputFilePath));
             BufferedWriter writer = new BufferedWriter(new FileWriter(outputFilePath))) {
            
            String line;
            StringBuilder processedContent = new StringBuilder();
            
            while ((line = reader.readLine()) != null) {
                // Remove newline characters and append the line with a space
                processedContent.append(line).append(" ");
            }
            
            // Remove the last extra space
            if (processedContent.length() > 0) {
                processedContent.setLength(processedContent.length() - 1);
            }
            
            // Write the processed content to the output file
            writer.write(processedContent.toString());
            
            System.out.println("Line breaks removed and spaces added. Output written to " + outputFilePath);

        } catch (IOException e) {
            System.out.println("Input file not found.");
        }
    }

    public static void main(String[] args) {
        formatText("input.txt", "output.txt");
    }
}