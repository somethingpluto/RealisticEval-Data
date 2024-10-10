package org.real.temp;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class Tester {

    private TextFileProcessor processor;

    @BeforeEach
    public void setUp() {
        processor = new TextFileProcessor();
    }

    @Test
    public void testGetMinSeqNumAndDistance() {
        String filePath = "path/to/your/file.txt";
        String word1 = "word1";
        String word2 = "word2";

        // Assuming the method returns a Pair<Integer, Integer>
        Pair<Integer, Integer> result = processor.getMinSeqNumAndDistance(filePath, word1, word2);

        assertNotNull(result);
        assertTrue(result.getFirst() != null && result.getSecond() != null);
        System.out.println("Line Number: " + result.getFirst());
        System.out.println("Minimum Distance: " + result.getSecond());
    }
}