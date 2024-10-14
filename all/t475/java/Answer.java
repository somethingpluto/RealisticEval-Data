package org.real.temp;

import java.util.HashMap;
import java.util.Map;

public class Answer {
    public static String safeFormat(String template, Map<String, Object> kwargs) {
        // Create a copy of the template string to avoid modifying the original
        StringBuilder result = new StringBuilder(template);

        // Iterate over each entry in the keyword arguments
        for (Map.Entry<String, Object> entry : kwargs.entrySet()) {
            String key = "{" + entry.getKey() + "}";
            int index = result.indexOf(key);

            // Replace all occurrences of the placeholder with its corresponding value
            while (index != -1) {
                result.replace(index, index + key.length(), entry.getValue().toString());
                index = result.indexOf(key, index); // Continue searching for subsequent occurrences
            }
        }

        return result.toString();
    }
}
