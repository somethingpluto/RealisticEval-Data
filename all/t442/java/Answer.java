package org.real.temp;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Answer {

    public static Object convertStringsToNumbers(Object data) {
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

    public static void main(String[] args) {
        // Example usage
        Map<String, Object> data = new HashMap<>();
        data.put("a", "123");
        data.put("b", List.of("456", "789.0"));
        data.put("c", "not_a_number");

        System.out.println(convertStringsToNumbers(data));
    }
}