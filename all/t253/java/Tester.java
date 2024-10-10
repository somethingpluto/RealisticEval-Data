package org.real.temp;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Tester {

    @Test
    public void testLogString() {
        String result = log("Hello, World!");
        assertEquals("Hello, World!", result);
    }

    @Test
    public void testLogNumber() {
        Integer result = log(42);
        assertEquals(42, result);
    }

    @Test
    public void testLogList() {
        List<String> list = Arrays.asList("apple", "banana", "cherry");
        String result = log(list);
        assertEquals("[\"apple\", \"banana\", \"cherry\"]", result);
    }

    @Test
    public void testLogDictionary() {
        Map<String, Object> map = new HashMap<>();
        map.put("name", "John");
        map.put("age", 30);
        String result = log(map);
        assertEquals("{\"name\":\"John\",\"age\":30}", result);
    }

    @Test
    public void testLogOtherType() {
        Date date = new Date();
        String result = log(date);
        assertNotNull(result); // Assuming we expect a non-null string representation
    }

    private <T> T log(T item) {
        if (item instanceof String) {
            System.out.println(item);
        } else if (item instanceof Number) {
            System.out.println(item);
        } else if (item instanceof List) {
            System.out.println(new Gson().toJson(item));
        } else if (item instanceof Map) {
            System.out.println(new Gson().toJson(item));
        } else {
            throw new IllegalArgumentException("Unsupported type: " + item.getClass());
        }
        return item;
    }
}