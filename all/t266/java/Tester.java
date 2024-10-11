package org.real.temp;

import static org.junit.Assert.*;
import org.junit.Test;
import java.util.HashMap;
import java.util.Map;

public class Tester {

    @Test
    public void testHandleNestedData() {
        // Arrange
        Map<String, Object> input = new HashMap<>();
        input.put("key1", "value1".getBytes());
        input.put("key2", 42);
        input.put("key3", 3.14);

        Map<String, Object> expectedOutput = new HashMap<>();
        expectedOutput.put("key1", "value1");
        expectedOutput.put("key2", 42);
        expectedOutput.put("key3", 3.14);

        // Act
        Map<String, Object> actualOutput = handleNestedData(input);

        // Assert
        assertEquals(expectedOutput, actualOutput);
    }

    private Map<String, Object> handleNestedData(Map<String, Object> data) {
        Map<String, Object> result = new HashMap<>();

        for (Map.Entry<String, Object> entry : data.entrySet()) {
            String key = entry.getKey();
            Object value = entry.getValue();

            if (value instanceof byte[]) {
                value = new String((byte[]) value);
            } else if (value instanceof Number) {
                Number number = (Number) value;
                value = number.doubleValue(); // Assuming we want to keep it as double for simplicity
            }

            result.put(key, value);
        }

        return result;
    }
}