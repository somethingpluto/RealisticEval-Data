package org.real.temp;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.io.TempDir;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class Tester {

    private Path testDir;

    @BeforeEach
    public void setUp(@TempDir Path tempDir) {
        this.testDir = tempDir;
    }

    @AfterEach
    public void tearDown() {
        // The @TempDir annotation automatically cleans up the directory after each test
    }

    private void createPngFiles(List<String> filenames) throws IOException {
        for (String filename : filenames) {
            Path filePath = testDir.resolve(filename);
            Files.createFile(filePath);  // Create an empty file
        }
    }

    @Test
    public void testBasicRenaming() throws IOException {
        // Test renaming in a basic scenario with simple filenames
        List<String> filenames = Arrays.asList("image1.png", "image2.png", "image3.png");
        createPngFiles(filenames);

        renameFiles(testDir.toString());

        List<String> expectedFiles = Arrays.asList("image1001.png", "image2001.png", "image3001.png");
        List<String> resultFiles = Files.list(testDir)
                                        .map(Path::getFileName)
                                        .map(Path::toString)
                                        .sorted()
                                        .collect(Collectors.toList());
        assertEquals(expectedFiles, resultFiles);
    }

    @Test
    public void testResetCounterForDifferentBaseNames() throws IOException {
        // Test that the counter resets for different base names
        List<String> filenames = Arrays.asList("image1.png", "picture1.png", "image2.png", "picture2.png");
        createPngFiles(filenames);

        renameFiles(testDir.toString());

        List<String> expectedFiles = Arrays.asList("image1001.png", "image2001.png", "picture1001.png", "picture2001.png");
        List<String> resultFiles = Files.list(testDir)
                                        .map(Path::getFileName)
                                        .map(Path::toString)
                                        .sorted()
                                        .collect(Collectors.toList());
        assertEquals(expectedFiles, resultFiles);
    }

    @Test
    public void testNoPngFiles() throws IOException {
        // Test handling of directories with no PNG files
        List<String> filenames = Arrays.asList("file1.txt", "file2.jpg");
        createPngFiles(filenames);

        renameFiles(testDir.toString());

        List<String> expectedFiles = filenames;  // No changes expected
        List<String> resultFiles = Files.list(testDir)
                                        .map(Path::getFileName)
                                        .map(Path::toString)
                                        .sorted()
                                        .collect(Collectors.toList());
        assertEquals(expectedFiles, resultFiles);
    }

    @Test
    public void testEmptyDirectory() throws IOException {
        // Test handling of an empty directory
        renameFiles(testDir.toString());

        List<String> expectedFiles = Arrays.asList();  // No files to rename
        List<String> resultFiles = Files.list(testDir)
                                        .map(Path::getFileName)
                                        .map(Path::toString)
                                        .collect(Collectors.toList());
        assertEquals(expectedFiles, resultFiles);
    }

    @Test
    public void testFilesWithExistingNumbers() throws IOException {
        // Test renaming files that already have numbers in their names
        List<String> filenames = Arrays.asList("file001.png", "file002.png", "file003.png");
        createPngFiles(filenames);

        renameFiles(testDir.toString());

        List<String> expectedFiles = Arrays.asList("file001001.png", "file002001.png", "file003001.png");
        List<String> resultFiles = Files.list(testDir)
                                        .map(Path::getFileName)
                                        .map(Path::toString)
                                        .sorted()
                                        .collect(Collectors.toList());
        assertEquals(expectedFiles, resultFiles);
    }
}