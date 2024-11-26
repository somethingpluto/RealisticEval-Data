package org.real.temp;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.assertEquals;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import static org.real.temp.Answer.*;
public class Tester {

    private static final String TEST_FILE = "test_sequences.dat";

    @Before
    public void setUp() throws IOException {
        // Create a temporary file with test cases
        try (FileWriter writer = new FileWriter(TEST_FILE)) {
            writer.write("2,4,6,8\n");    // Munodi sequence (d = 2)
            writer.write("1,3,5,7\n");    // Munodi sequence (d = 2)
            writer.write("10,20,30\n");   // Munodi sequence (d = 10)
            writer.write("1,2,4,8\n");    // Not a Munodi sequence (d changes)
            writer.write("5,10,15,20\n"); // Munodi sequence (d = 5)
        }
    }

    @Test
    public void testSequences() {
        // Expected results
        Map<List<Integer>, Boolean> expectedResults = Map.of(
            List.of(2, 4, 6, 8), true,
            List.of(1, 3, 5, 7), true,
            List.of(10, 20, 30), true,
            List.of(1, 2, 4, 8), false,
            List.of(5, 10, 15, 20), true
        );

        Map<List<Integer>, Boolean> results = checkSequences(TEST_FILE);

        for (Map.Entry<List<Integer>, Boolean> entry : expectedResults.entrySet()) {
            assertEquals(entry.getValue(), results.get(entry.getKey()));
        }
    }

    @After
    public void tearDown() {
        // Clean up the test file after tests
        try {
            Files.delete(Paths.get(TEST_FILE));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // Utility method to check sequences
    private static Map<List<Integer>, Boolean> checkSequences(String filename) {
        List<List<Integer>> sequences = readSequencesFromFile(filename);
        Map<List<Integer>, Boolean> results = new HashMap<>();
        for (List<Integer> seq : sequences) {
            results.put(seq, isMunodiSequence(seq));
        }
        return results;
    }
}