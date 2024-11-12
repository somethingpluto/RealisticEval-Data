package org.real.temp;

import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Path;
import java.util.List;
import org.junit.Test;
import org.mockito.Mockito;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThrows;

public class Tester {

    private static final String FILE1_CONTENT = "Line1\nLine2\nLine3\n";
    private static final String FILE2_CONTENT = "Line1\nLineChanged\nLine3\n";

    private Path file1Path;
    private Path file2Path;

    @BeforeEach
    public void setUp(@TempDir Path tempDir) {
        file1Path = tempDir.resolve("file1.txt");
        file2Path = tempDir.resolve("file2.txt");
    }

    @AfterEach
    public void tearDown() {
        if (file1Path.toFile().exists()) {
            file1Path.toFile().delete();
        }
        if (file2Path.toFile().exists()) {
            file2Path.toFile().delete();
        }
    }

    @Test
    public void testIdenticalFiles() throws IOException {
        writeToFile(file1Path, FILE1_CONTENT);
        writeToFile(file2Path, FILE1_CONTENT);

        List<String> result = compareFiles(file1Path.toString(), file2Path.toString());
        assertEquals(0, result.size(), "There should be no differences detected");
    }

    @Test
    public void testFilesWithDifferences() throws IOException {
        writeToFile(file1Path, FILE1_CONTENT);
        writeToFile(file2Path, FILE2_CONTENT);

        List<String> result = compareFiles(file1Path.toString(), file2Path.toString());
        assertNotEquals(0, result.size(), "There should be differences detected");
    }

    @Test
    public void testNonexistentFile() {
        try (MockedStatic<Answer> mockedStatic = Mockito.mockStatic(Answer.class)) {
            mockedStatic.when(() -> Answer.readFile("nonexistent.txt"))
                    .thenThrow(new java.io.FileNotFoundException("File not found"));

            Exception exception = assertThrows(java.io.FileNotFoundException.class,
                    () -> compareFiles("nonexistent.txt", file2Path.toString()));
            assertEquals("File not found", exception.getMessage());
        }
    }

    @Test
    public void testFileReadingError() {
        try (MockedStatic<Answer> mockedStatic = Mockito.mockStatic(Answer.class)) {
            mockedStatic.when(() -> Answer.readFile(file1Path.toString()))
                    .thenThrow(new java.io.IOException("Error reading file"));

            Exception exception = assertThrows(java.io.IOException.class,
                    () -> compareFiles(file1Path.toString(), file2Path.toString()));
            assertEquals("Error reading file", exception.getMessage());
        }
    }

    private void writeToFile(Path filePath, String content) throws IOException {
        try (FileWriter writer = new FileWriter(filePath.toFile())) {
            writer.write(content);
        }
    }
}