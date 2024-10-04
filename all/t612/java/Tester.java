package org.real.temp;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.*;

public class Tester {

    private Path testFilePath;

    @BeforeEach
    public void setUp() throws IOException {
        // Create a temporary file for testing
        testFilePath = Paths.get("testFile.txt");
        Files.write(testFilePath, "This is a test file with oldText.".getBytes());
    }

    @Test
    public void testFindAndReplace_SingleOccurrence() throws IOException {
        // Arrange
        String searchString = "oldText";
        String replaceString = "newText";

        // Act
        Answer.findAndReplaceInFile(testFilePath, searchString, replaceString);

        // Assert
        String content = new String(Files.readAllBytes(testFilePath));
        assertEquals("This is a test file with newText.", content);
    }

    @Test
    public void testFindAndReplace_MultipleOccurrences() throws IOException {
        // Arrange
        Files.write(testFilePath, "oldText oldText oldText".getBytes()); // Setting up multiple occurrences
        String searchString = "oldText";
        String replaceString = "newText";

        // Act
        Answer.findAndReplaceInFile(testFilePath, searchString, replaceString);

        // Assert
        String content = new String(Files.readAllBytes(testFilePath));
        assertEquals("newText newText newText", content);
    }

    @Test
    public void testFindAndReplace_NoOccurrences() throws IOException {
        // Arrange
        String searchString = "nonExistentText";
        String replaceString = "newText";

        // Act
        Answer.findAndReplaceInFile(testFilePath, searchString, replaceString);

        // Assert
        String content = new String(Files.readAllBytes(testFilePath));
        assertEquals("This is a test file with oldText.", content); // Content should remain unchanged
    }


    @Test
    public void testFindAndReplace_EmptyReplaceString() throws IOException {
        // Arrange
        String searchString = "oldText";
        String replaceString = "";

        // Act
        Answer.findAndReplaceInFile(testFilePath, searchString, replaceString);

        // Assert
        String content = new String(Files.readAllBytes(testFilePath));
        assertEquals("This is a test file with .", content); // Should remove "oldText"
    }

    @Test
    public void testFindAndReplace_FileNotFound() {
        // Arrange
        Path nonExistentPath = Paths.get("nonExistentFile.txt");
        String searchString = "oldText";
        String replaceString = "newText";

        // Act & Assert
        assertThrows(IOException.class, () -> {
            Answer.findAndReplaceInFile(nonExistentPath, searchString, replaceString);
        });
    }
}
