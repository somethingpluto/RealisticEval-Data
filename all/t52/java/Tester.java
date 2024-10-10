package org.real.temp;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class Tester {

    @Test
    public void testRenameFilePath() {
        // Test data
        String inputPath = "C:\\Users\\Username\\Documents\\file:name.txt";
        String expectedOutput = "C:\\Users\\Username\\Documents\\file_name.txt";

        // Call the method under test
        String actualOutput = renameFilePath(inputPath);

        // Assert the result
        assertEquals(expectedOutput, actualOutput);
    }

    /**
     * Renames a Windows file path by replacing colons in the filename with underscores.
     *
     * @param path The original file path.
     * @return The modified file path with colons in the filename replaced by underscores.
     */
    public static String renameFilePath(String path) {
        return path.replace(":", "_");
    }
}