package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import static org.real.temp.Answer.*;

public class Tester {

    @Test
    public void testMultipleFileTypes() {
        List<String> files = Arrays.asList(
            "document.docx",
            "photo.jpeg",
            "report.pdf",
            "image.png",
            "archive.zip"
        );
        Map<String, List<String>> expectedResult = new HashMap<>();
        expectedResult.put("docx", Arrays.asList("document.docx"));
        expectedResult.put("jpeg", Arrays.asList("photo.jpeg"));
        expectedResult.put("pdf", Arrays.asList("report.pdf"));
        expectedResult.put("png", Arrays.asList("image.png"));
        expectedResult.put("zip", Arrays.asList("archive.zip"));

        Map<String, List<String>> result = classifyFilesByExtension(files.toArray(new String[0]));
        assertEquals(expectedResult, result);
    }

    @Test
    public void testEmptyList() {
        List<String> files = Arrays.asList();
        Map<String, List<String>> expectedResult = new HashMap<>();

        Map<String, List<String>> result = classifyFilesByExtension(files.toArray(new String[0]));
        assertEquals(expectedResult, result);
    }

    @Test
    public void testFilesWithSameExtension() {
        List<String> files = Arrays.asList(
                "file1.txt",
                "file2.txt",
                "file3.txt"
        );
        Map<String, List<String>> expectedResult = new HashMap<>();
        expectedResult.put("txt", Arrays.asList("file1.txt", "file2.txt", "file3.txt"));

        Map<String, List<String>> result = classifyFilesByExtension(files.toArray(new String[0]));
        assertEquals(expectedResult, result);
    }
}