package org.real.temp;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Answer {

    /**
     * Prepends the specified string to the beginning of each line of the file.
     *
     * @param filePath path to the file whose lines will be modified.
     * @param prefix   string to prepend to the beginning of each line.
     */
    public static void prependToEachLine(String filePath, String prefix) throws IOException {
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath));
             BufferedWriter writer = new BufferedWriter(new FileWriter("temp.txt"))) {

            String line;
            while ((line = reader.readLine()) != null) {
                writer.write(prefix + line);
                writer.newLine();
            }

            // Replace original file with temp file
            new File(filePath).delete();
            new File("temp.txt").renameTo(new File(filePath));
        }
    }
}