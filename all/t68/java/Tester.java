package org.real.temp;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.Arrays;
import java.util.List;

public class Tester {

    private static final List<List<Integer>> divideList(List<Integer> lst, int n) {
        // Total number of elements in the list
        int L = lst.size();
        // Calculate the size of each part
        int baseSize = L / n;
        // Calculate the number of sections that will have an additional element
        int remainder = L % n;

        List<List<Integer>> result = new ArrayList<>();
        // Start index of the sublist
        int startIndex = 0;

        for (int i = 0; i < n; i++) {
            // Determine the size of the current part
            int partSize = baseSize + (i < remainder ? 1 : 0);
            // Append the sublist to the result list
            result.add(new ArrayList<>(lst.subList(startIndex, startIndex + partSize)));
            // Update the start index for the next part
            startIndex += partSize;
        }

        return result;
    }

    @Test
    public void testEvenDivision() {
        List<Integer> lst = Arrays.asList(1, 2, 3, 4, 5, 6);
        int n = 3;
        List<List<Integer>> expected = Arrays.asList(
            Arrays.asList(1, 2),
            Arrays.asList(3, 4),
            Arrays.asList(5, 6)
        );
        assertEquals(expected, divideList(lst, n));
    }

    @Test
    public void testUnevenDivision() {
        List<Integer> lst = Arrays.asList(1, 2, 3, 4, 5, 6, 7);
        int n = 3;
        List<List<Integer>> expected = Arrays.asList(
            Arrays.asList(1, 2, 3),
            Arrays.asList(4, 5),
            Arrays.asList(6, 7)
        );
        assertEquals(expected, divideList(lst, n));
    }

    @Test
    public void testMorePartsThanItems() {
        List<Integer> lst = Arrays.asList(1, 2, 3);
        int n = 5;
        List<List<Integer>> expected = Arrays.asList(
            Arrays.asList(1),
            Arrays.asList(2),
            Arrays.asList(3),
            Arrays.asList(),
            Arrays.asList()
        );
        assertEquals(expected, divideList(lst, n));
    }

    @Test
    public void testSingleElement() {
        List<Integer> lst = Arrays.asList(1);
        int n = 1;
        List<List<Integer>> expected = Arrays.asList(
            Arrays.asList(1)
        );
        assertEquals(expected, divideList(lst, n));
    }

    @Test
    public void testEmptyList() {
        List<Integer> lst = Arrays.asList();
        int n = 3;
        List<List<Integer>> expected = Arrays.asList(
            Arrays.asList(),
            Arrays.asList(),
            Arrays.asList()
        );
        assertEquals(expected, divideList(lst, n));
    }
}