import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Tester {

    // Method to be tested
    private static List<Integer> convertToRingFormat(List<Integer> holes) {
        // Initialize the ring with all positions set to 1
        List<Integer> ring = new ArrayList<>();
        for (int i = 0; i < 32; i++) {
            ring.add(1);
        }

        // Mark the positions of holes as 0
        for (Integer hole : holes) {
            if (0 <= hole && hole < 32) {  // Ensure hole positions are within valid range
                ring.set(hole, 0);
            }
        }

        return ring;
    }

    @Test
    public void testNoHoles() {
        """ Test with no holes provided. """
        List<Integer> holes = new ArrayList<>();
        List<Integer> expected = new ArrayList<>(Arrays.asList(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1));
        List<Integer> result = convertToRingFormat(holes);
        assertEquals(expected, result);
    }

    @Test
    public void testSingleHole() {
        """ Test with a single hole position. """
        List<Integer> holes = new ArrayList<>(Arrays.asList(5));
        List<Integer> expected = new ArrayList<>(Arrays.asList(1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1));
        List<Integer> result = convertToRingFormat(holes);
        assertEquals(expected, result);
    }

    @Test
    public void testMultipleHoles() {
        """ Test with multiple hole positions. """
        List<Integer> holes = new ArrayList<>(Arrays.asList(0, 2, 4, 8, 16));
        List<Integer> expected = new ArrayList<>(Arrays.asList(0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1));
        List<Integer> result = convertToRingFormat(holes);
        assertEquals(expected, result);
    }

    @Test
    public void testHoleOutOfBounds() {
        """ Test with some hole positions out of bounds. """
        List<Integer> holes = new ArrayList<>(Arrays.asList(-1, 32, 5, 10));
        List<Integer> expected = new ArrayList<>(Arrays.asList(1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1));
        List<Integer> result = convertToRingFormat(holes);
        assertEquals(expected, result);
    }

    @Test
    public void testAllHoles() {
        """ Test with all positions as holes. """
        List<Integer> holes = new ArrayList<>();
        for (int i = 0; i < 32; i++) {
            holes.add(i);
        }
        List<Integer> expected = new ArrayList<>(Arrays.asList(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0));
        List<Integer> result = convertToRingFormat(holes);
        assertEquals(expected, result);
    }
}