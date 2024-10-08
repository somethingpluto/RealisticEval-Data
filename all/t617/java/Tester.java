package org.real.temp;

import static org.junit.jupiter.api.Assertions.*;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import org.junit.jupiter.api.Test;
import java.util.Map;

public class Tester {

    @Test
    public void testValidJson() throws IOException {
        String jsonContent = "{\"name\":\"John\", \"age\":30}";
        Path path = Files.createTempFile(null, ".json");
        Files.write(path, jsonContent.getBytes());

        Map<String, Object> result = Answer.parseJsonFile(path.toString());
        assertEquals("John", result.get("name"));
        assertEquals(30, result.get("age"));
    }

    @Test
    public void testEmptyJson() throws IOException {
        String jsonContent = "{}";
        Path path = Files.createTempFile(null, ".json");
        Files.write(path, jsonContent.getBytes());

        Map<String, Object> result = Answer.parseJsonFile(path.toString());
        assertTrue(result.isEmpty());
    }



    @Test
    public void testNullInput() {
        assertThrows(NullPointerException.class, () -> Answer.parseJsonFile(null));
    }

    @Test
    public void testNonJsonFile() throws IOException {
        String notJsonContent = "Hello, World!";
        Path path = Files.createTempFile(null, ".txt");
        Files.write(path, notJsonContent.getBytes());

        assertThrows(Exception.class, () -> Answer.parseJsonFile(path.toString()));
    }

    @Test
    public void testJsonWithArray() throws IOException {
        String jsonContent = "{\"names\":[\"John\", \"Doe\"]}";
        Path path = Files.createTempFile(null, ".json");
        Files.write(path, jsonContent.getBytes());

        Map<String, Object> result = Answer.parseJsonFile(path.toString());
        assertNotNull(result.get("names"));
    }
}
