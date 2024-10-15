import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class CombinationGenerator {

    /**
     * Produces all combinations of numeric arrays for each key in the given map object
     * and returns them as a two-dimensional array.
     *
     * @param map A map where each key is a string, and each value is a list of integers.
     * @return A list of lists, where each sub-list is a unique combination of numbers from the map's values.
     */
    public List<List<Integer>> generateCombinations(Map<String, List<Integer>> map) {
        List<String> keys = new ArrayList<>(map.keySet());
        List<List<Integer>> values = new ArrayList<>(map.values());

        List<List<Integer>> combinations = new ArrayList<>();

        // Start the recursive combination generation.
        generate(values, keys, combinations, new ArrayList<>(), 0);
        return combinations;
    }

    /**
     * Helper function to recursively generate combinations.
     *
     * @param values            The list of values corresponding to each key in the map.
     * @param keys              The keys of the map.
     * @param combinations      The list to store the generated combinations.
     * @param currentCombination The current combination being built.
     * @param currentIndex      The current index in the keys/values lists.
     */
    private void generate(List<List<Integer>> values, List<String> keys, List<List<Integer>> combinations,
                          List<Integer> currentCombination, int currentIndex) {
        // Base case: If we've reached the end of the keys, add the combination to the results.
        if (currentIndex == keys.size()) {
            combinations.add(new ArrayList<>(currentCombination));
            return;
        }

        // Recursively generate combinations for the current key's values.
        List<Integer> currentValues = values.get(currentIndex);
        for (Integer value : currentValues) {
            currentCombination.add(value);
            generate(values, keys, combinations, currentCombination, currentIndex + 1);
            currentCombination.remove(currentCombination.size() - 1); // backtrack
        }
    }
}