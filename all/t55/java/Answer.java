import java.util.Arrays;
import java.util.HashMap;

public class Answer {
    public static int minRemovalsToMakeUnique(int[] nums) {
        Arrays.sort(nums);
        HashMap<Integer, Integer> map = new HashMap<>();
        int count = 0;

        for (int i : nums) {
            if (map.containsKey(i)) {
                count++;
                i++;
                while (map.containsKey(i)) {
                    i++;
                    count++;
                }
            }
            map.put(i, 1);
        }
        return count;
    }
}