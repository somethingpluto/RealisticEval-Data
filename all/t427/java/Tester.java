import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.Map;

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

    // Utility method to read sequences from a file
    private static List<List<Integer>> readSequencesFromFile(String filename) {
        List<List<Integer>> sequences = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = reader.readLine()) != null) {
                // Assuming sequences are comma-separated in the file
                List<Integer> seq = new ArrayList<>();
                String[] parts = line.strip().split(",");
                for (String part : parts) {
                    seq.add(Integer.parseInt(part.trim()));
                }
                sequences.add(seq);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return sequences;
    }

    // Utility method to check if a sequence is a Munodi sequence
    private static boolean isMunodiSequence(List<Integer> sequence) {
        if (sequence.size() < 2) {
            return false;  // A sequence with less than 2 elements cannot be a Munodi sequence
        }

        for (int i = 1; i < sequence.size(); i++) {
            int current = sequence.get(i);
            int previous = sequence.get(i - 1);

            if (previous % 2 == 0 && current != previous / 2) {
                return false;  // Even number condition failed
            } else if (previous % 2 != 0 && current != 3 * previous + 1) {
                return false;  // Odd number condition failed
            }
        }
        return true;  // All conditions met
    }
}