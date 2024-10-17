package org.real.temp;

import java.util.HashMap;
import java.util.Map;

public class Answer {

    /**
     * Cleans the input map by removing entries with invalid values.
     * Valid values are non-null, non-blank strings, and numbers that are not NaN.
     *
     * @param inputMap A map to be cleaned.
     * @return A new map containing only valid values.
     */
    public static Map<String, Object> cleanDictionary(Map<String, Object> inputMap) {
        Map<String, Object> cleanedMap = new HashMap<>();

        for (Map.Entry<String, Object> entry : inputMap.entrySet()) {
            Object value = entry.getValue();

            // Check if the value is not null and not a blank string
            if (value instanceof String && !((String) value).trim().isEmpty()) {
                // Check if value is a number (Integer or Double) and is not NaN
                if (!(value instanceof Double && ((Double) value).isNaN())) {
                    cleanedMap.put(entry.getKey(), value);
                }
            }
        }

        return cleanedMap;
    }

    public static void main(String[] args) {
        // Example usage
        Map<String, Object> inputMap = new HashMap<>();
        inputMap.put("key1", "value1");
        inputMap.put("key2", "");
        inputMap.put("key3", 123);
        inputMap.put("key4", 123.0);
        inputMap.put("key5", Double.NaN);

        Map<String, Object> cleanedMap = cleanDictionary(inputMap);
        System.out.println(cleanedMap); // Output will contain only valid values
    }
}