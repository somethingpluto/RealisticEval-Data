package org.real.temp;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;



public class Tester {

    @Test
    public void testStandardCase() {
        List<List<String>> data = Arrays.asList(
            Arrays.asList("Name", "Age", "City"),
            Arrays.asList("Alice", "22", "New York"),
            Arrays.asList("Bob", "30", "San Francisco")
        );
        List<Integer> expected = Arrays.asList(5, 3, 13);
        assertEquals(expected, calculateColumnWidths(data));
    }

    @Test
    public void testSingleElement() {
        List<List<String>> data = Arrays.asList(
            Arrays.asList("Name")
        );
        List<Integer> expected = Arrays.asList(4);
        assertEquals(expected, calculateColumnWidths(data));
    }

    @Test
    public void testVariedLength() {
        List<List<String>> data = Arrays.asList(
            Arrays.asList("a", "bb", "ccc"),
            Arrays.asList("dddd", "ee", "f")
        );
        List<Integer> expected = Arrays.asList(4, 2, 3);
        assertEquals(expected, calculateColumnWidths(data));
    }

    @Test
    public void testAllEmptyStrings() {
        List<List<String>> data = Arrays.asList(
            Arrays.asList("", "", ""),
            Arrays.asList("", "", "")
        );
        List<Integer> expected = Arrays.asList(0, 0, 0);
        assertEquals(expected, calculateColumnWidths(data));
    }

    @Test
    public void testMixedContent() {
        List<List<String>> data = Arrays.asList(
            Arrays.asList("1234", "567", "890"),
            Arrays.asList("abc", "defg", "h")
        );
        List<Integer> expected = Arrays.asList(4, 4, 3);
        assertEquals(expected, calculateColumnWidths(data));
    }

    @Test
    public void testSingleColumnMultipleRows() {
        List<List<String>> data = Arrays.asList(
            Arrays.asList("one"),
            Arrays.asList("two"),
            Arrays.asList("three")
        );
        List<Integer> expected = Arrays.asList(5);
        assertEquals(expected, calculateColumnWidths(data));
    }

}