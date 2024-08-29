package com.real.t349;

import java.util.ArrayList;
import java.util.List;

public class Adapted<T> {

    public List<List<T>> generateCombinations(List<List<T>> inputLists) {
        if (inputLists == null || inputLists.isEmpty()) {
            return new ArrayList<>(); // Return an empty list if input is null or empty
        }

        List<List<T>> combinations = new ArrayList<>();
        generateCombinationsRecursive(inputLists, 0, new ArrayList<>(), combinations);
        return combinations;
    }

    private void generateCombinationsRecursive(List<List<T>> inputLists, int currentIndex,
                                               List<T> currentCombination, List<List<T>> combinations) {
        if (currentIndex == inputLists.size()) {
            combinations.add(new ArrayList<>(currentCombination)); // Snapshot of currentCombination
            return;
        }

        List<T> currentList = inputLists.get(currentIndex);
        for (T element : currentList) {
            currentCombination.add(element);
            generateCombinationsRecursive(inputLists, currentIndex + 1, currentCombination, combinations);
            currentCombination.remove(currentCombination.size() - 1); // Remove the last element for backtracking
        }
    }
}
