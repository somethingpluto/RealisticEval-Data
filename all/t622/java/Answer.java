package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {
    /**
     * Generates all possible combinations of elements from a list of lists.
     *
     * @param lists A list of lists, where each inner list contains elements
     *              to combine with elements from other lists.
     * @return A list of combinations, where each combination is represented
     *         as a list of strings.
     */
    public List<List<String>> generateCombinations(List<List<String>> lists) {
        List<List<String>> result = new ArrayList<>();
        if (lists == null || lists.size() == 0) {
            return result;
        }
        backtrack(result, new ArrayList<>(), lists, 0);
        return result;
    }

    private void backtrack(List<List<String>> result, List<String> tempList, List<List<String>> lists, int index) {
        // If the current combination is the size of lists, add it to the results
        if (tempList.size() == lists.size()) {
            result.add(new ArrayList<>(tempList));
            return;
        }
        // Loop through the current list at the given index
        for (String item : lists.get(index)) {
            tempList.add(item); // Choose the current item
            backtrack(result, tempList, lists, index + 1); // Move to the next list
            tempList.remove(tempList.size() - 1); // Backtrack
        }
    }

    public static void main(String[] args) {
        Answer answer = new Answer();
        List<List<String>> inputLists = new ArrayList<>();

        // Example input
        inputLists.add(List.of("A", "B"));
        inputLists.add(List.of("1", "2"));
        inputLists.add(List.of("X", "Y"));

        List<List<String>> combinations = answer.generateCombinations(inputLists);

        // Print the combinations
        for (List<String> combination : combinations) {
            System.out.println(combination);
        }
    }
}
