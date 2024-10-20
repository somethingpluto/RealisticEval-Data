package org.real.temp;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Answer {

    /**
     * Inverts the keys and values in a map. If multiple keys have the same value,
     * the new map's values will be a list of these keys.
     *
     * @param originalMap The map to invert.
     * @return A new map with values and keys inverted.
     */
    public static Map<String, Object> invertMap(Map<String, String> originalMap) {
        Map<String, Object> newMap = new HashMap<>();
        for (Map.Entry<String, String> entry : originalMap.entrySet()) {
            String key = entry.getKey();
            String value = entry.getValue();
            
            if (!newMap.containsKey(value)) {
                newMap.put(value, key);
            } else {
                // If the value already exists as a key, we need to append to or create a list
                Object existingValue = newMap.get(value);
                if (!(existingValue instanceof ArrayList)) {
                    ArrayList<String> list = new ArrayList<>();
                    list.add((String) existingValue); // Convert the existing value to a list
                    newMap.put(value, list);
                }
                ((ArrayList<String>) newMap.get(value)).add(key);
            }
        }
        return newMap;
    }

    public static void main(String[] args) {
        Map<String, String> originalMap = new HashMap<>();
        originalMap.put("a", "1");
        originalMap.put("b", "2");
        originalMap.put("c", "1");

        Map<String, Object> invertedMap = invertMap(originalMap);
        System.out.println(invertedMap);
    }
}