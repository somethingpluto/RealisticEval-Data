import java.util.ArrayList;
import java.util.List;

public class Answer {

    public static List<List<Integer>> divideList(List<Integer> lst, int n) {
        List<List<Integer>> result = new ArrayList<>();

        if (lst == null || lst.isEmpty()) {
            return result;
        }

        int size = lst.size();
        int batchSize = (size + n - 1) / n; // Round up division

        for (int i = 0; i < size; i += batchSize) {
            int end = Math.min(i + batchSize, size);
            result.add(lst.subList(i, end));
        }

        return result;
    }
}