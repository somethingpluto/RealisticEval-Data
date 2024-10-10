import static org.junit.Assert.assertEquals;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.junit.Test;

public class Tester {

    @Test
    public void testDictOfListsToListOfDicts() {
        // Arrange
        Map<String, List<Integer>> dictOfLists = new HashMap<>();
        dictOfLists.put("a", Arrays.asList(1, 2, 3));
        dictOfLists.put("b", Arrays.asList(4, 5, 6));

        // Act
        List<Map<String, Integer>> listOfDicts = dictOfListsToListOfDicts(dictOfLists);

        // Assert
        assertEquals(3, listOfDicts.size());
        assertEquals(1, listOfDicts.get(0).get("a"));
        assertEquals(4, listOfDicts.get(1).get("b"));
        assertEquals(2, listOfDicts.get(0).get("a"));
        assertEquals(5, listOfDicts.get(1).get("b"));
        assertEquals(3, listOfDicts.get(0).get("a"));
        assertEquals(6, listOfDicts.get(1).get("b"));
    }

    private List<Map<String, Integer>> dictOfListsToListOfDicts(Map<String, List<Integer>> dictOfLists) {
        int maxLength = dictOfLists.values().stream()
                                  .mapToInt(List::size)
                                  .max()
                                  .orElse(0);

        List<Map<String, Integer>> result = new ArrayList<>(maxLength);

        for (int i = 0; i < maxLength; i++) {
            Map<String, Integer> map = new HashMap<>();
            for (Map.Entry<String, List<Integer>> entry : dictOfLists.entrySet()) {
                if (i < entry.getValue().size()) {
                    map.put(entry.getKey(), entry.getValue().get(i));
                }
            }
            result.add(map);
        }

        return result;
    }
}