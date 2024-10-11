import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TesterTest {

    @Test
    public void testFindLargestDivisible() {
        assertEquals(Integer.valueOf(30), Tester.findLargestDivisible(30));
        assertEquals(Integer.valueOf(25), Tester.findLargestDivisible(29));
        assertEquals(Integer.valueOf(5), Tester.findLargestDivisible(7));
        assertNull(Tester.findLargestDivisible(1));
    }
}