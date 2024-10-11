import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Answer {
    public static Map<String, Object> sanitizeData(Map<String, Object> data, List<String> keyToRemove) {
        if (keyToRemove == null || keyToRemove.isEmpty()) {
            return data;
        }

        Map<String, Object> result = new HashMap<>();
        for (Map.Entry<String, Object> entry : data.entrySet()) {
            if (!keyToRemove.contains(entry.getKey())) {
                result.put(entry.getKey(), entry.getValue());
            }
        }

        return result;
    }
}