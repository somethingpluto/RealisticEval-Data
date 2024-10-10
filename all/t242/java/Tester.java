package org.real.temp;

import org.junit.jupiter.api.Test;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class Tester {

    @Test
    public void testClassifyFilesByExtension() {
        List<String> fileNames = Arrays.asList("file1.txt", "file2.jpg", "file3.txt", "image.png");
        Map<String, List<String>> expectedOutput = new HashMap<>();
        expectedOutput.put("txt", Arrays.asList("file1.txt", "file3.txt"));
        expectedOutput.put("jpg", Arrays.asList("file2.jpg"));
        expectedOutput.put("png", Arrays.asList("image.png"));

        Map<String, List<String>> actualOutput = FileClassifier.classifyFilesByExtension(fileNames);

        assertEquals(expectedOutput, actualOutput);
    }
}