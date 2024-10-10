package org.real.temp;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Answer {

    public static List<Map<String, Object>> dictOfListsToListOfMaps(Map<String, List<Object>> dictOfLists) {
        List<Map<String, Object>> listOfMaps = new ArrayList<>();

        if (!dictOfLists.isEmpty()) {
            int maxListSize = dictOfLists.values().stream()
                    .mapToInt(List::size)
                    .max()
                    .getAsInt();

            for (int i = 0; i < maxListSize; i++) {
                Map<String, Object> map = new HashMap<>();
                for (Map.Entry<String, List<Object>> entry : dictOfLists.entrySet()) {
                    String key = entry.getKey();
                    List<Object> list = entry.getValue();
                    if (i < list.size()) {
                        map.put(key, list.get(i));
                    }
                }
                listOfMaps.add(map);
            }
        }

        return listOfMaps;
    }
}