package org.real.temp;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import org.json.JSONObject;

import static org.junit.Assert.assertEquals;

public class Tester {
    private File tempDir;
    private File sourceFile;
    private File matchFile;
    private File mismatchFile;

    @Before
    public void setUp() throws IOException {
        // Create a temporary directory
        tempDir = Files.createTempDirectory("test").toFile();

        // Create temporary files for testing
        sourceFile = new File(tempDir, "source.json");
        matchFile = new File(tempDir, "match.json");
        mismatchFile = new File(tempDir, "mismatch.json");

        // Example data
        String jsonData = "[{\"name\": \"Alice\", \"pid\": 1}, {\"name\": \"Bob\", \"pid\": 2}, {\"name\": \"Charlie\", \"pid\": 3}]";
        
        // Write example data to source file
        try (FileWriter writer = new FileWriter(sourceFile)) {
            writer.write(jsonData);
        }
    }

    @After
    public void tearDown() {
        // Delete temporary files and directory
        sourceFile.delete();
        matchFile.delete();
        mismatchFile.delete();
        tempDir.delete();
    }

    @Test
    public void testAllMatch() throws IOException {
        // Test where all items match
        classifyJsonObjectsByPid(sourceFile.getAbsolutePath(), new int[]{1, 2, 3}, matchFile.getAbsolutePath(), mismatchFile.getAbsolutePath());
        
        List<Object> matches = readJsonFile(matchFile);
        List<Object> mismatches = readJsonFile(mismatchFile);

        assertEquals(3, matches.size());
        assertEquals(0, mismatches.size());
    }

    @Test
    public void testNoMatch() throws IOException {
        // Test where no items match
        classifyJsonObjectsByPid(sourceFile.getAbsolutePath(), new int[]{4, 5}, matchFile.getAbsolutePath(), mismatchFile.getAbsolutePath());
        
        List<Object> matches = readJsonFile(matchFile);
        List<Object> mismatches = readJsonFile(mismatchFile);

        assertEquals(0, matches.size());
        assertEquals(3, mismatches.size());
    }

    @Test
    public void testPartialMatch() throws IOException {
        // Test where some items match
        classifyJsonObjectsByPid(sourceFile.getAbsolutePath(), new int[]{1, 3}, matchFile.getAbsolutePath(), mismatchFile.getAbsolutePath());

        List<Object> matches = readJsonFile(matchFile);
        List<Object> mismatches = readJsonFile(mismatchFile);

        assertEquals(2, matches.size());
        assertEquals(1, mismatches.size());
    }

    @Test
    public void testEmptyPidList() throws IOException {
        // Test with an empty PID list
        classifyJsonObjectsByPid(sourceFile.getAbsolutePath(), new int[]{}, matchFile.getAbsolutePath(), mismatchFile.getAbsolutePath());

        List<Object> matches = readJsonFile(matchFile);
        List<Object> mismatches = readJsonFile(mismatchFile);

        assertEquals(0, matches.size());
        assertEquals(3, mismatches.size());
    }
    private List<Object> readJsonFile(File file) throws IOException {
        // You can implement JSON reading logic here using a library like Jackson or Gson
        String jsonData = new String(Files.readAllBytes(file.toPath()));
        return parseJson(jsonData); // Replace with actual parsing method
    }
    public static JSONObject parseJson(String jsonString) {
        try {
            return new JSONObject(jsonString);
        } catch (Exception e) {
            System.err.println("Failed to parse JSON: " + e.getMessage());
            return null;
        }
    }
}
