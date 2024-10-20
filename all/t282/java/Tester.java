package org.real.temp;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testDeeplyNestedArray() {
        List<Object> nestedArray = Arrays.asList(1, Arrays.asList(2, Arrays.asList(3, Arrays.asList(4, Arrays.asList(5)))));
        List<Object> expectedResult = Arrays.asList(1, 2, 3, 4, 5);
        assertEquals(expectedResult, flattenArray(nestedArray));
    }

    @Test
    public void testMixedTypes() {
        List<Object> mixedArray = Arrays.asList("a", Arrays.asList("b", 2, Arrays.asList(true, Arrays.asList(3.14))), false);
        List<Object> expectedResult = Arrays.asList("a", "b", 2, true, 3.14, false);
        assertEquals(expectedResult, flattenArray(mixedArray));
    }

    @Test
    public void testEmptyArray() {
        List<Object> emptyArray = new ArrayList<>();
        List<Object> expectedResult = new ArrayList<>();
        assertEquals(expectedResult, flattenArray(emptyArray));
    }

    @Test
    public void testArrayWithEmptySubarrays() {
        List<Object> complexArray = Arrays.asList(1, new ArrayList<>(), Arrays.asList(2, new ArrayList<>(), 3), 
                                                  Arrays.asList(4, Arrays.asList(5, new ArrayList<>(), 6), 7), 
                                                  new ArrayList<>());
        List<Object> expectedResult = Arrays.asList(1, 2, 3, 4, 5, 6, 7);
        assertEquals(expectedResult, flattenArray(complexArray));
    }

    @Test
    public void testNoNestedArray() {
        List<Object> flatArray = Arrays.asList(1, 2, 3, 4, 5);
        List<Object> expectedResult = Arrays.asList(1, 2, 3, 4, 5);
        assertEquals(expectedResult, flattenArray(flatArray));
    }
    
}