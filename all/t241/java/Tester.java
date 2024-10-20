import org.junit.Before;
import org.junit.Test;
import java.nio.file.Path;
import java.nio.file.Files;
import java.io.IOException;
import java.nio.file.Files;
import java.util.List;
import java.nio.file.Files;

import static org.junit.Assert.assertEquals;

public class Tester {

    private Path tempFile;

    @Before
    public void setUp() throws IOException {
        // Create a temporary file in the system's temporary directory
        tempFile = Files.createTempFile("dummy_file", ".txt");
        tempFile.toFile().deleteOnExit(); // Ensure it gets deleted after the test
    }

    @Test
    public void testBasicFunctionality() throws IOException {
        // Test basic functionality with expected input
        String mockContent = "hello world\napple banana apple\norange apple banana";
        Files.write(tempFile, List.of(mockContent.split("\n")));
        
        Tuple result = Answer.getMinSeqNumAndDistance(tempFile.toString(), "apple", "banana");
        assertEquals(new Tuple(2, 1), result);
    }

    @Test
    public void testWordsNotPresent() throws IOException {
        // Test case where one or both words are not present
        String mockContent = "apple orange pear\norange pear apple";
        Files.write(tempFile, List.of(mockContent.split("\n")));
        
        Tuple result = Answer.getMinSeqNumAndDistance(tempFile.toString(), "apple", "banana");
        assertEquals(new Tuple(null, Integer.MAX_VALUE), result);
    }

    @Test
    public void testEmptyFile() throws IOException {
        // Test an empty file
        Files.write(tempFile, List.of(""));
        
        Tuple result = Answer.getMinSeqNumAndDistance(tempFile.toString(), "apple", "banana");
        assertEquals(new Tuple(null, Integer.MAX_VALUE), result);
    }

    @Test
    public void testMultipleLinesWithVaryingDistances() throws IOException {
        // Test multiple lines with varying distances between words
        String mockContent = "apple banana\napple orange orange banana\napple orange orange orange banana";
        Files.write(tempFile, List.of(mockContent.split("\n")));
        
        Tuple result = Answer.getMinSeqNumAndDistance(tempFile.toString(), "apple", "banana");
        assertEquals(new Tuple(1, 1), result);
    }
}
