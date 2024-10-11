import static org.junit.Assert.assertEquals;
import java.util.Arrays;
import java.util.List;
import org.junit.Before;
import org.junit.Test;

public class Tester {
    private List<Integer> inputList;
    private int numberOfParts;
    private List<List<Integer>> expectedResult;

    @Before
    public void setUp() {
        // Initialize your data here for each test method
        inputList = Arrays.asList(1, 2, 3, 4, 5);
        numberOfParts = 3;
        expectedResult = Arrays.asList(
            Arrays.asList(1, 2),
            Arrays.asList(3, 4),
            Arrays.asList(5)
        );
    }

    @Test
    public void testDivideList() {
        // Call the function to be tested
        List<List<Integer>> result = divideList(inputList, numberOfParts);

        // Verify the results
        assertEquals(expectedResult, result);
    }

    // Define your divideList method here if it's not in another file
    public static List<List<Integer>> divideList(List<Integer> lst, int n) {
        // Your implementation goes here
        return null; // Replace with actual implementation
    }
}