package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.*;

public class Tester {

    private static final String NAME = "name";
    private static final String AGE = "age";
    private static final String CITY = "city";

    /**
     * Test standard conversion with equal length lists.
     */
    @Test
    public void testStandardConversion() {
        Map<String, List<Object>> dictOfLists = new HashMap<>();
        dictOfLists.put(NAME, Arrays.asList("Alice", "Bob", "Charlie"));
        dictOfLists.put(AGE, Arrays.asList(25, 30, 35));
        dictOfLists.put(CITY, Arrays.asList("New York", "Los Angeles", "Chicago"));

        List<Map<String, Object>> expectedResult = Arrays.asList(
            new HashMap<String, Object>() {{
                put(NAME, "Alice");
                put(AGE, 25);
                put(CITY, "New York");
            }},
            new HashMap<String, Object>() {{
                put(NAME, "Bob");
                put(AGE, 30);
                put(CITY, "Los Angeles");
            }},
            new HashMap<String, Object>() {{
                put(NAME, "Charlie");
                put(AGE, 35);
                put(CITY, "Chicago");
            }}
        );

        List<Map<String, Object>> result = dictOfListsToListOfDicts(dictOfLists);
        assertEquals(expectedResult, result);
    }

    /**
     * Test the function with empty lists.
     */
    @Test
    public void testEmptyLists() {
        Map<String, List<Object>> dictOfLists = new HashMap<>();
        dictOfLists.put(NAME, Collections.emptyList());
        dictOfLists.put(AGE, Collections.emptyList());
        dictOfLists.put(CITY, Collections.emptyList());

        List<Map<String, Object>> expectedResult = Collections.emptyList();

        List<Map<String, Object>> result = dictOfListsToListOfDicts(dictOfLists);
        assertEquals(expectedResult, result);
    }

    /**
     * Test the function with single-element lists.
     */
    @Test
    public void testSingleElementLists() {
        Map<String, List<Object>> dictOfLists = new HashMap<>();
        dictOfLists.put(NAME, Collections.singletonList("Alice"));
        dictOfLists.put(AGE, Collections.singletonList(25));
        dictOfLists.put(CITY, Collections.singletonList("New York"));

        List<Map<String, Object>> expectedResult = Collections.singletonList(
            new HashMap<String, Object>() {{
                put(NAME, "Alice");
                put(AGE, 25);
                put(CITY, "New York");
            }}
        );

        List<Map<String, Object>> result = dictOfListsToListOfDicts(dictOfLists);
        assertEquals(expectedResult, result);
    }
}