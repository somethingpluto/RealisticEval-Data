package org.real.temp;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Answer {

    public static Object handleNestedData(Object data) {
        if (data instanceof Map) {
            // If it's a Map, apply the function recursively to each value
            Map<?, ?> map = (Map<?, ?>) data;
            Map<Object, Object> newMap = new HashMap<>();
            for (Map.Entry<?, ?> entry : map.entrySet()) {
                newMap.put(entry.getKey(), handleNestedData(entry.getValue()));
            }
            return newMap;
        } else if (data instanceof List) {
            // If it's a List, apply the function recursively to each item
            List<?> list = (List<?>) data;
            List<Object> newList = new ArrayList<>();
            for (Object item : list) {
                newList.add(handleNestedData(item));
            }
            return newList;
        } else if (data instanceof byte[]) {
            // If it's bytes, decode to a UTF-8 string
            byte[] bytes = (byte[]) data;
            return new String(bytes, java.nio.charset.StandardCharsets.UTF_8);
        } else if (data instanceof Integer || data instanceof Float || data instanceof Double) {
            // If it's already a number, return as is
            return data;
        } else if (data instanceof String) {
            // Try to convert strings that represent integers or floats to their numeric forms
            String str = (String) data;
            try {
                return Integer.parseInt(str);
            } catch (NumberFormatException e) {
                try {
                    return Double.parseDouble(str);
                } catch (NumberFormatException ex) {
                    return str;  // Return the original string if it's not a number
                }
            }
        }
        return data;  // Return the input as is for any other type
    }

    public static void main(String[] args) {
        // Example usage
        Map<String, Object> data = new HashMap<>();
        data.put("a", 1);
        data.put("b", "2");
        data.put("c", new byte[]{99, 111, 100, 101});
        data.put("d", List.of(3, "4", "5.0"));
        data.put("e", Map.of("f", "6", "g", 7));

        System.out.println(handleNestedData(data));
    }
}