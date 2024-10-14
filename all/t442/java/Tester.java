package org.real.temp;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Tester {

    /**
     * Test the conversion of strings in nested structures to numbers.
     */
    @Test
    public void testConvertStringsToNumbers() {
        // Test with a dictionary
        Map<String, Object> dataDict = new HashMap<>();
        dataDict.put("a", "123");
        dataDict.put("b", Arrays.asList("456", "789.0"));
        dataDict.put("c", "not_a_number");

        Map<String, Object> expectedDict = new HashMap<>();
        expectedDict.put("a", 123);
        expectedDict.put("b", Arrays.asList(456, 789.0f));
        expectedDict.put("c", "not_a_number");

        assertEquals(expectedDict, convertStringsToNumbers(dataDict));

        // Test with a list
        List<Object> dataList = Arrays.asList("123", "456.7", "not_a_number");

        List<Object> expectedList = Arrays.asList(123, 456.7f, "not_a_number");

        assertEquals(expectedList, convertStringsToNumbers(dataList));

        // Test with a string
        String dataStr = "123";
        assertEquals(123, convertStringsToNumbers(dataStr));

        dataStr = "456.7";
        assertEquals(456.7f, convertStringsToNumbers(dataStr));

        dataStr = "not_a_number";
        assertEquals("not_a_number", convertStringsToNumbers(dataStr));
    }

    private Object convertStringsToNumbers(Object data) {
        if (data instanceof Map) {
            @SuppressWarnings("unchecked")
            Map<Object, Object> map = (Map<Object, Object>) data;
            Map<Object, Object> convertedMap = new HashMap<>();
            for (Map.Entry<Object, Object> entry : map.entrySet()) {
                convertedMap.put(entry.getKey(), convertStringsToNumbers(entry.getValue()));
            }
            return convertedMap;
        } else if (data instanceof List) {
            @SuppressWarnings("unchecked")
            List<Object> list = (List<Object>) data;
            List<Object> convertedList = new ArrayList<>();
            for (Object item : list) {
                convertedList.add(convertStringsToNumbers(item));
            }
            return convertedList;
        } else if (data instanceof String) {
            String str = (String) data;
            try {
                // Try converting to float first, then to int if possible
                if (str.contains(".")) {
                    return Float.parseFloat(str);
                } else {
                    return Integer.parseInt(str);
                }
            } catch (NumberFormatException e) {
                return data; // Return original string if conversion fails
            }
        } else {
            return data; // Return data unchanged if it's not a string
        }
    }
}
