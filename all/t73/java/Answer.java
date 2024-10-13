package org.real.temp;

import java.util.*;

public class Answer {
    /**
     * Convert a map of lists into a list of maps.
     *
     * @param mapOfLists A map where each key has a list as its value.
     * @return A list where each item is a map formed by corresponding elements of lists in the input map.
     * @throws IllegalArgumentException If lists in the map are of different lengths.
     */
    public static List<Map<String, Integer>> dictOfListsToListOfDicts(Map<String, List<Integer>> mapOfLists) throws IllegalArgumentException {
        // Check if all lists are of the same length
        if (mapOfLists.isEmpty()) {
            return Collections.emptyList();
        }
        
        int expectedSize = -1;
        for (List<Integer> list : mapOfLists.values()) {
            if (expectedSize == -1) {
                expectedSize = list.size();
            } else if (list.size() != expectedSize) {
                throw new IllegalArgumentException("All lists in the map must have the same length.");
            }
        }

        // Using zip to iterate over lists simultaneously
        List<Map<String, Integer>> listOfDicts = new ArrayList<>();
        List<List<Integer>> values = new ArrayList<>(mapOfLists.values());

        for (int i = 0; i < expectedSize; i++) {
            Map<String, Integer> dict = new HashMap<>();
            for (Map.Entry<String, List<Integer>> entry : mapOfLists.entrySet()) {
                dict.put(entry.getKey(), entry.getValue().get(i));
            }
            listOfDicts.add(dict);
        }

        return listOfDicts;
    }

    public static void main(String[] args) {
        Map<String, List<Integer>> mapOfLists = new HashMap<>();
        mapOfLists.put("a", Arrays.asList(1, 2, 3));
        mapOfLists.put("b", Arrays.asList(4, 5, 6));

        try {
            List<Map<String, Integer>> listOfDicts = dictOfListsToListOfDicts(mapOfLists);
            System.out.println(listOfDicts);
        } catch (IllegalArgumentException e) {
            System.err.println(e.getMessage());
        }
    }
}