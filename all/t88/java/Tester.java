import org.junit.Test;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;

public class Tester {

    @Test
    public void testSpecificHours() {
        assertTrue(isCronBetween2And4AM("0 2,3,4 * * *"));
    }

    @Test
    public void testRangeIncludes2To4AM() {
        assertFalse(isCronBetween2And4AM("0 1-5 * * *"));
    }

    @Test
    public void testRangeExcludes2To4AM() {
        assertFalse(isCronBetween2And4AM("0 0-1,5-23 * * *"));
    }

    @Test
    public void testWildcardInHourField() {
        assertFalse(isCronBetween2And4AM("0 * * * *"));
    }

    // Assuming the method is present in this class or imported
    public boolean isCronBetween2And4AM(String cronExpression) {
        // Implementation here
        return false; // Placeholder
    }
}