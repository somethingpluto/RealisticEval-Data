import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Tester {

    private Map<String, Object> invertMap(Map<Object, Object> originalMap) {
        Map<String, Object> newMap = new HashMap<>();
        for (Map.Entry<Object, Object> entry : originalMap.entrySet()) {
            Object key = entry.getKey();
            Object value = entry.getValue();

            if (!newMap.containsKey(value)) {
                newMap.put((String) value, key);
            } else {
                // If the value already exists as a key, we need to append to or create a list
                Object existingValue = newMap.get(value);
                if (!(existingValue instanceof ArrayList)) {
                    ArrayList<String> list = new ArrayList<>();
                    list.add((String) existingValue); // Convert the existing value to a list
                    newMap.put((String) value, list);
                }
                ((ArrayList<String>) newMap.get(value)).add((String) key);
            }
        }
        return newMap;
    }

    @Test
    public void testNormalDictionary() {
        """Test inversion of a dictionary without duplicate values."""
        Map<Object, Object> originalDict = new HashMap<>();
        originalDict.put("a", 1);
        originalDict.put("b", 2);
        originalDict.put("c", 3);

        Map<String, Object> expected = new HashMap<>();
        expected.put("1", "a");
        expected.put("2", "b");
        expected.put("3", "c");

        Map<String, Object> result = invertMap(originalDict);
        assertEquals(expected, result);
    }

    @Test
    public void testDictionaryWithDuplicates() {
        """Test inversion of a dictionary with duplicate values."""
        Map<Object, Object> originalDict = new HashMap<>();
        originalDict.put("a", 1);
        originalDict.put("b", 1);
        originalDict.put("c", 2);

        Map<String, Object> expected = new HashMap<>();
        expected.put("1", new ArrayList<>(List.of("a", "b")));
        expected.put("2", "c");

        Map<String, Object> result = invertMap(originalDict);
        assertEquals(expected, result);
    }

    @Test
    public void testEmptyDictionary() {
        """Test inversion of an empty dictionary."""
        Map<Object, Object> originalDict = new HashMap<>();

        Map<String, Object> expected = new HashMap<>();

        Map<String, Object> result = invertMap(originalDict);
        assertEquals(expected, result);
    }

    @Test
    public void testNonStringKeys() {
        """Test inversion of a dictionary with non-string keys."""
        Map<Object, Object> originalDict = new HashMap<>();
        originalDict.put(1, "apple");
        originalDict.put(2, "banana");
        originalDict.put(3, "apple");

        Map<String, Object> expected = new HashMap<>();
        expected.put("apple", new ArrayList<>(List.of("1", "3")));
        expected.put("banana", "2");

        Map<String, Object> result = invertMap(originalDict);
        assertEquals(expected, result);
    }

    @Test
    public void testMixedTypes() {
        """Test inversion of a dictionary with mixed key and value types."""
        Map<Object, Object> originalDict = new HashMap<>();
        originalDict.put("a", 1);
        originalDict.put(2, "two");
        originalDict.put("three", 3);

        Map<String, Object> expected = new HashMap<>();
        expected.put("1", "a");
        expected.put("two", "2");
        expected.put("3", "three");

        Map<String, Object> result = invertMap(originalDict);
        assertEquals(expected, result);
    }
}