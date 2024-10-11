package org.real.temp;

import static org.junit.Assert.*;
import org.junit.Test;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Tester extends junit.framework.TestCase {

    @Test
    public void testPrependToFile() throws IOException {
        // Temporary file path
        File tempFile = File.createTempFile("test", ".txt");

        // Content to write to the file
        String content = "Hello\nWorld";

        // Write initial content to the file
        try (FileWriter writer = new FileWriter(tempFile)) {
            writer.write(content);
        }

        // Prefix to prepend
        String prefix = "Prefix_";

        // Call the method under test
        prependToEachLine(tempFile.getAbsolutePath(), prefix);

        // Read the updated content from the file
        String updatedContent = new String(Files.readAllBytes(Paths.get(tempFile.getAbsolutePath())));

        // Expected result
        String expectedResult = "Prefix_Hello\nPrefix_World";

        // Assert that the updated content matches the expected result
        assertEquals(expectedResult, updatedContent);

        // Clean up the temporary file
        tempFile.delete();
    }

    private void prependToEachLine(String filePath, String prefix) {
        try {
            // Read all lines from the file
            List<String> lines = Files.readAllLines(Paths.get(filePath));

            // Prepend the prefix to each line
            for (int i = 0; i < lines.size(); i++) {
                lines.set(i, prefix + lines.get(i));
            }

            // Write the updated lines back to the file
            Files.write(Paths.get(filePath), lines);
        } catch (IOException e) {
            throw new RuntimeException("Error while prepending to file: " + filePath, e);
        }
    }
}