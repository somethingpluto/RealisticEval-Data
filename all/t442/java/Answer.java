package org.real.temp;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Answer {

    public static Object convertStringsToNumbers(Object data) {
        if (data instanceof Map) {
            @SuppressWarnings("unchecked")
            Map<String, Object> map = (Map<String, Object>) data;
            Map<String, Object> newMap = new HashMap<>();
            for (Map.Entry<String, Object> entry : map.entrySet()) {
                newMap.put(entry.getKey(), convertStringsToNumbers(entry.getValue()));
            }
            return newMap;
        } else if (data instanceof List) {
            @SuppressWarnings("unchecked")
            List<Object> list = (List<Object>) data;
            List<Object> newList = new ArrayList<>();
            for (Object item : list) {
                newList.add(convertStringsToNumbers(item));
            }
            return newList;
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
                return str;  // Return original string if conversion fails
            }
        } else {
            return data;  // Return data unchanged if it's not a string
        }
    }

    public static void main(String[] args) {
        // Example usage
        Map<String, Object> data = new HashMap<>();
        data.put("a", "123");
        data.put("b", "456.789");
        data.put("c", "hello");

        List<Object> listData = List.of("100", "200.5", "world");

        System.out.println(convertStringsToNumbers(data));
        System.out.println(convertStringsToNumbers(listData));
    }
}