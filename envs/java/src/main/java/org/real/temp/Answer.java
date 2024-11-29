package org.real.temp;
import java.util.*;

public class Answer {

    private static final Set<String> defaultKeysToRemove = new HashSet<>(Arrays.asList(
            "email", "pc_conflicts", "metadata", "eligible_student_paper_prize", "talk_poster",
            "submitted_at", "decision", "status", "submitted", "submission"
    ));

    /**
     * Recursively sanitize a Map by removing specific keys.
     *
     * @param data           the input data to sanitize
     * @param keyToBeRemoved the set of keys to remove; if null, uses default keys
     * @return the sanitized data
     */
    public static Object sanitizeData(Object data, Set<String> keyToBeRemoved) {
        if (keyToBeRemoved == null) {
            keyToBeRemoved = defaultKeysToRemove;
        }
        if (data instanceof Map) {
            Map<?, ?> map = (Map<?, ?>) data;
            Map<String, Object> sanitizedMap = new HashMap<>();
            for (Map.Entry<?, ?> entry : map.entrySet()) {
                String key = (String) entry.getKey();
                if (!keyToBeRemoved.contains(key)) {
                    sanitizedMap.put(key, sanitizeData(entry.getValue(), keyToBeRemoved));
                }
            }
            return sanitizedMap;
        } else if (data instanceof List) {
            List<?> list = (List<?>) data;
            List<Object> sanitizedList = new ArrayList<>();
            for (Object item : list) {
                sanitizedList.add(sanitizeData(item, keyToBeRemoved));
            }
            return sanitizedList;
        } else {
            return data;
        }
    }

    // Example usage
    public static void main(String[] args) {
        Map<String, Object> sampleData = new HashMap<>();
        sampleData.put("name", "John Doe");
        sampleData.put("email", "john.doe@example.com");
        sampleData.put("age", 30);
        sampleData.put("metadata", "some metadata");

        Map<String, Object> sanitizedData = (Map<String, Object>) sanitizeData(sampleData, null);
        System.out.println(sanitizedData);
    }
}