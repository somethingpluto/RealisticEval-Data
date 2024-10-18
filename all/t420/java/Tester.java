package org.real.temp;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.mockito.stubbing.Answer;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.when;

@ExtendWith(MockitoExtension.class)
public class Tester {

    @Mock
    private BufferedReader mockReader;

    private List<List<String>> sequences;

    @BeforeEach
    public void setUp() throws IOException {
        sequences = new ArrayList<>();
    }

    @Test
    public void testSimpleCase() throws IOException {
        // Mock the file read operation
        when(mockReader.readLine()).thenReturn("hello world", "hello hello world", "world hello", null);

        List<List<String>> sequences = readFileAsSequences(mockReader);
        Pair<Integer, Integer> result = getMinDistance(sequences, "hello", "world");

        assertEquals(new Pair<>(0, 1), result);
    }

    @Test
    public void testMultipleLines() throws IOException {
        // Mock the file read operation
        when(mockReader.readLine()).thenReturn("hello planet", "world hello planet", "hello world planet", null);

        List<List<String>> sequences = readFileAsSequences(mockReader);
        Pair<Integer, Integer> result = getMinDistance(sequences, "hello", "world");

        assertEquals(new Pair<>(1, 1), result);
    }

    @Test
    public void testLargeDistance() throws IOException {
        // Mock the file read operation
        when(mockReader.readLine()).thenReturn(
            "hello a b c d e f g h i j k l m n o p q r s t u v w x y z world", null
        );

        List<List<String>> sequences = readFileAsSequences(mockReader);
        Pair<Integer, Integer> result = getMinDistance(sequences, "hello", "world");

        assertEquals(new Pair<>(0, 27), result);
    }

    @Test
    public void testAdjacentWords() throws IOException {
        // Mock the file read operation
        when(mockReader.readLine()).thenReturn("hello world", "hello hello world world", "world hello", null);

        List<List<String>> sequences = readFileAsSequences(mockReader);
        Pair<Integer, Integer> result = getMinDistance(sequences, "hello", "world");

        assertEquals(new Pair<>(0, 1), result);
    }
}