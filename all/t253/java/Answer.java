package org.real.temp;

import com.fasterxml.jackson.databind.ObjectMapper;
import java.util.List;
import java.util.Map;

public class Answer {

    public static Object log(Object item) {
        ObjectMapper mapper = new ObjectMapper();

        if (item instanceof String || item instanceof Number) {
            System.out.println(item);
        } else if (item instanceof List) {
            System.out.println(mapper.writeValueAsString((List<?>) item));
        } else if (item instanceof Map) {
            System.out.println(mapper.writeValueAsString((Map<?, ?>) item));
        } else {
            throw new IllegalArgumentException("Unsupported type: " + item.getClass().getName());
        }

        return item;
    }
}