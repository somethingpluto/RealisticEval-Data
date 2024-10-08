package org.real.temp;

import org.junit.jupiter.api.Test;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class Tester {

    private void createTestFile(String fileName, String content) throws IOException {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName))) {
            writer.write(content);
        }
    }

    @Test
    void testReadValidIntegers() throws IOException {
        String filePath = "valid_integers.txt";
        createTestFile(filePath, "42\n-7\n0\n100\n");

        Answer answer = new Answer();
        List<Object> result = answer.readDataFromFile(filePath);

        assertEquals(4, result.size());
        assertEquals(42, result.get(0));
        assertEquals(-7, result.get(1));
        assertEquals(0, result.get(2));
        assertEquals(100, result.get(3));
    }

    @Test
    void testReadValidFloats() throws IOException {
        String filePath = "valid_floats.txt";
        createTestFile(filePath, "3.14\n-0.001\n2.71828\n0.0\n");

        Answer answer = new Answer();
        List<Object> result = answer.readDataFromFile(filePath);

        assertEquals(4, result.size());
        assertEquals(3.14f, result.get(0));
        assertEquals(-0.001f, result.get(1));
        assertEquals(2.71828f, result.get(2));
        assertEquals(0.0f, result.get(3));
    }

    @Test
    void testReadMixedData() throws IOException {
        String filePath = "mixed_data.txt";
        createTestFile(filePath, "Hello\n42\n3.14\nWorld\n-19.99\n");

        Answer answer = new Answer();
        List<Object> result = answer.readDataFromFile(filePath);

        assertEquals(5, result.size());
        assertEquals("Hello", result.get(0));
        assertEquals(42, result.get(1));
        assertEquals(3.14f, result.get(2));
        assertEquals("World", result.get(3));
        assertEquals(-19.99f, result.get(4));
    }

    @Test
    void testReadEmptyFile() throws IOException {
        String filePath = "empty_file.txt";
        createTestFile(filePath, "");

        Answer answer = new Answer();
        List<Object> result = answer.readDataFromFile(filePath);

        assertEquals(0, result.size());
    }

    @Test
    void testReadInvalidData() throws IOException {
        String filePath = "invalid_data.txt";
        createTestFile(filePath, "Hello\n42a\n3.14.15\nWorld!\n");

        Answer answer = new Answer();
        List<Object> result = answer.readDataFromFile(filePath);

        assertEquals(4, result.size());
        assertEquals("Hello", result.get(0));
        assertEquals("42a", result.get(1));
        assertEquals("3.14.15", result.get(2));
        assertEquals("World!", result.get(3));
    }
}
