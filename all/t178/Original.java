import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Utils {
    public static List<Integer> getLongestNonDecreasingSubsequence(List<Integer> list) {
        int n = list.size();
        int[] dp = new int[n];
        Arrays.fill(dp, 1);

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (list.get(i) >= list.get(j)) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }

        int maxLengthIndex = 0;
        for (int i = 1; i < n; i++) {
            if (dp[i] > dp[maxLengthIndex]) {
                maxLengthIndex = i;
            }
        }

        List<Integer> longestSubsequence = new ArrayList<>();
        longestSubsequence.add(0, list.get(maxLengthIndex)); // Add the element at the beginning of the list
        int maxLength = dp[maxLengthIndex];
        for (int i = maxLengthIndex - 1; i >= 0; i--) {
            if (list.get(i) <= list.get(maxLengthIndex) && dp[i] == maxLength - 1) {
                longestSubsequence.add(0, list.get(i)); // Add the element at the beginning of the list
                maxLength--;
            }
        }

        return longestSubsequence;
    }
}
