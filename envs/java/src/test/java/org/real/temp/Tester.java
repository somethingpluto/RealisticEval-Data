package org.real.temp;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.*;
import static org.real.temp.Answer.*;

public class Tester {



    @Test
    public void testEmptyDict() {
        Map<String, Object> data = new HashMap<>();
        Set<String> keyToBeRemoved = new HashSet<>(Arrays.asList("email", "metadata"));

        Map<String, Object> expected = new HashMap<>();
        assertEquals(expected, sanitizeData(data, keyToBeRemoved));
    }

    @Test
    public void testRemoveDefaultKeys() {
        Map<String, Object> data = new HashMap<>();
        data.put("name", "John Doe");
        data.put("email", "johndoe@example.com");
        data.put("metadata", new HashMap<>(Map.of(
                "submitted_at", "2021-07-10",
                "status", "pending"
        )));
        data.put("comments", Arrays.asList("Good", "Needs review"));

        Set<String> keyToBeRemoved = new HashSet<>(Arrays.asList("email", "metadata"));
        Map<String, Object> expected = new HashMap<>();
        expected.put("name", "John Doe");
        expected.put("comments", Arrays.asList("Good", "Needs review"));

        assertEquals(expected, sanitizeData(data, keyToBeRemoved));
    }

    @Test
    public void testSpecifiedKeyToRemove() {
        Map<String, Object> data = new HashMap<>();
        data.put("name", "John Doe");
        data.put("location", "Earth");
        data.put("email", "johndoe@example.com");

        Set<String> keyToBeRemoved = new HashSet<>(Arrays.asList("email"));
        Map<String, Object> expected = new HashMap<>();
        expected.put("name", "John Doe");
        expected.put("location", "Earth");

        assertEquals(expected, sanitizeData(data, keyToBeRemoved));
    }
}