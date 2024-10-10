import java.util.*;

public class Answer {
    public static Map<Object, List<Object>> invertDictionary(Map<Object, Object> originalDict) {
        Map<Object, List<Object>> invertedDict = new HashMap<>();

        for (Map.Entry<Object, Object> entry : originalDict.entrySet()) {
            Object key = entry.getKey();
            Object value = entry.getValue();

            if (!invertedDict.containsKey(value)) {
                invertedDict.put(value, new ArrayList<>());
            }

            invertedDict.get(value).add(key);
        }

        return invertedDict;
    }
}